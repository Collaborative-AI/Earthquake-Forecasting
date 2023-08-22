import torch
import torch.nn as nn
from config import cfg
from .utils import init_param, normalize, loss_fn


class LeNet(nn.Module):
    def __init__(self, data_shape, sneak):
        super().__init__()
        blocks = [nn.Conv2d(data_shape[0], 6, kernel_size=5), nn.ReLU(),
                  nn.MaxPool2d(kernel_size=(2, 2), stride=2),
                  nn.Conv2d(6, 16, kernel_size=5), nn.ReLU(),
                  nn.MaxPool2d(kernel_size=(2, 2), stride=2),
                  nn.Conv2d(16, 120, kernel_size=5), nn.ReLU(), nn.Flatten(),
                  nn.Linear(120, 84), nn.ReLU(), nn.Linear(84, 10)]
        self.blocks = nn.Sequential(*blocks)
        self.sneak = sneak

    def forward(self, input):
        output = {'loss': torch.tensor(0, device=cfg['device'], dtype=torch.float32)}
        x = input['data']
        if 'norm' not in input or ('norm' in input and input['norm']):
            x = normalize(x, *cfg['stats'][cfg['data_name']])
        out = self.blocks(x)
        output['target'] = out
        output['loss'] = loss_fn(input, output)
        return output


def lenet(sneak=False):
    data_shape = cfg['data_shape']
    model = LeNet(data_shape, sneak)
    model.apply(init_param)
    return model
