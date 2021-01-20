import torch
import torch.nn as nn
import numpy as np
from .utils import init_param, normalize, loss_fn
from config import cfg


class MLPBlock(nn.Module):
    def __init__(self, input_size, output_size):
        super().__init__()
        self.activation = nn.ReLU()
        self.linear = nn.Linear(input_size, output_size)

    def forward(self, input):
        output = self.linear(self.activation(input))
        return output


class MLP(nn.Module):
    def __init__(self, data_shape, hidden_size, target_size, sneak):
        super().__init__()
        blocks = [nn.Linear(np.prod(data_shape).item(), hidden_size[0])]
        for i in range(len(hidden_size) - 1):
            blocks.append(MLPBlock(hidden_size[i], hidden_size[i + 1]))
        blocks.extend([
            nn.ReLU(),
            nn.Linear(hidden_size[-1], target_size),
        ])
        self.blocks = nn.Sequential(*blocks)
        self.sneak = sneak

    def forward(self, input):
        output = {}
        x = input['data']
        if 'norm' not in input or ('norm' in input and input['norm']):
            x = normalize(x, *cfg['stats'][cfg['data_name']])
        x = x.view(x.size(0), -1)
        output['target'] = self.blocks(x)
        output['loss'] = loss_fn(input, output)
        return output


def mlp(sneak=False):
    data_shape = cfg['data_shape']
    target_size = cfg['target_size']
    hidden_size = cfg['mlp']['hidden_size']
    model = MLP(data_shape, hidden_size, target_size, sneak)
    model.apply(init_param)
    return model
