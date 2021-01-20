import torch
import torch.nn as nn
from config import cfg
from .utils import init_param


class GenResBlock(nn.Module):
    def __init__(self, input_size, output_size, stride):
        super().__init__()
        self.conv = nn.Sequential(
            nn.BatchNorm2d(input_size),
            nn.ReLU(),
            nn.Upsample(scale_factor=stride, mode='nearest'),
            nn.Conv2d(input_size, output_size, 3, 1, 1),
            nn.BatchNorm2d(output_size),
            nn.ReLU(),
            nn.Conv2d(output_size, output_size, 3, 1, 1),
        )
        if stride > 1:
            self.shortcut = nn.Sequential(
                nn.Upsample(scale_factor=stride, mode='nearest'),
                nn.Conv2d(input_size, output_size, 1, 1, 0)
            )
        elif input_size != output_size:
            self.shortcut = nn.Sequential(
                nn.Conv2d(input_size, output_size, 1, 1, 0)
            )
        else:
            self.shortcut = nn.Identity()

    def forward(self, input):
        shortcut = self.shortcut(input)
        x = self.conv(input)
        output = x + shortcut
        return output


class Generator(nn.Module):
    def __init__(self, data_shape, latent_size, hidden_size):
        super().__init__()
        self.data_shape = data_shape
        self.latent_size = latent_size
        self.hidden_size = hidden_size
        self.linear = nn.Linear(latent_size, hidden_size[0] * data_shape[1] // (2 ** (len(hidden_size) - 1)) *
                                data_shape[2] // (2 ** (len(hidden_size) - 1)))
        blocks = []
        for i in range(len(hidden_size) - 1):
            blocks.append(GenResBlock(hidden_size[i], hidden_size[i + 1], 2))
        blocks.extend([
            nn.BatchNorm2d(hidden_size[-1]),
            nn.ReLU(),
            nn.Conv2d(hidden_size[-1], data_shape[0], 3, 1, 1),
            nn.Tanh()
        ])
        self.blocks = nn.Sequential(*blocks)
        self.normalizer = nn.BatchNorm2d(data_shape[0], affine=False, track_running_stats=False)

    def generate(self, input):
        pass
    
    def forward(self, input):
        x = input
        x = self.linear(x)
        x = x.view(x.size(0), -1, self.data_shape[1] // (2 ** (len(self.hidden_size) - 1)),
                   self.data_shape[1] // (2 ** (len(self.hidden_size) - 1)))
        x = self.blocks(x)
        x = self.normalizer(x)
        return x


def generator():
    data_shape = cfg['data_shape']
    latent_size = cfg['generator']['latent_size']
    hidden_size = cfg['generator']['hidden_size']
    model = Generator(data_shape, latent_size, hidden_size)
    model.apply(init_param)
    return model
