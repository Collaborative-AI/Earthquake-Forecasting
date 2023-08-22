import torch
import torch.nn as nn
import numpy as np
from config import cfg
from .utils import init_param, normalize, loss_fn


class Linear(nn.Module):
    def __init__(self, data_shape, target_size, sneak):
        super().__init__()
        self.linear = nn.Linear(np.prod(data_shape).item(), target_size)
        self.sneak = sneak

    def forward(self, input):
        output = {}
        x = input['data']
        if 'norm' not in input or ('norm' in input and input['norm']):
            x = normalize(x, *cfg['stats'][cfg['data_name']])
        x = x.view(x.size(0), -1)
        output['target'] = self.linear(x)
        output['loss'] = loss_fn(input, output)
        return output


def linear(sneak=False):
    data_shape = cfg['data_shape']
    target_size = cfg['target_size']
    model = Linear(data_shape, target_size, sneak)
    model.apply(init_param)
    return model
