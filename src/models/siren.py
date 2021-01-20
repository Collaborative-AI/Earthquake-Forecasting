import torch
import torch.nn as nn
import math
from config import cfg
from .utils import init_param


class Sine(nn.Module):
    def __init__(self, w0=1.):
        super().__init__()
        self.w0 = w0

    def forward(self, input):
        return torch.sin(self.w0 * input)


class Siren(nn.Module):
    def __init__(self, input_size, output_size, w0, c, is_first, activation=None):
        super().__init__()
        self.input_size = input_size
        self.output_size = output_size
        self.w0 = w0
        self.c = c
        self.is_first = is_first
        self.activation = Sine(w0) if activation is None else activation

    def init(self, data_size):
        self.register_buffer('weight', torch.zeros(*data_size, self.output_size, self.input_size))
        self.register_buffer('bias', torch.zeros(*data_size, self.output_size))
        w_std = (1 / self.input_size) if self.is_first else (math.sqrt(self.c / self.input_size) / self.w0)
        nn.init.uniform_(self.weight, -w_std, w_std)
        nn.init.uniform_(self.bias, -w_std, w_std)
        return

    def forward(self, input):
        self.init(input.size()[:-1])
        out = (input.unsqueeze(-2) * self.weight.to(input.device)).sum(-1) + self.bias.to(input.device)
        out = self.activation(out)
        return out


class SirenNet(nn.Module):
    def __init__(self, input_size, hidden_size, output_size, num_layers, w0=1., w0_initial=30., c=6.):
        super().__init__()
        layers = []
        for i in range(num_layers):
            is_first = i == 0
            layer_w0 = w0_initial if is_first else w0
            layer_size = input_size if is_first else hidden_size
            layers.append(Siren(layer_size, hidden_size, layer_w0, c, is_first))
        layers.append(Siren(hidden_size, output_size, w0, c, False, nn.Sigmoid()))
        self.layers = nn.Sequential(*layers)

    def forward(self, x):
        x = self.layers(x)
        return x


def siren():
    data_shape = cfg['data_shape']
    hidden_size = cfg['siren']['hidden_size']
    num_layers = cfg['siren']['num_layers']
    model = SirenNet(len(data_shape[1:]), hidden_size, data_shape[0], num_layers)
    model.apply(init_param)
    return model
