import torch
import torch.nn as nn
import torch.nn.functional as F
from config import cfg


def init_param(m):
    if isinstance(m, (nn.BatchNorm1d, nn.BatchNorm2d)) and m.weight is not None:
        nn.init.normal_(m.weight.data, 1.0, 0.02)
        nn.init.constant_(m.bias.data, 0.0)
    return m


def normalize(input, m, s):
    broadcast_size = [1] * input.dim()
    broadcast_size[1] = input.size(1)
    m, s = torch.tensor(m, dtype=input.dtype).view(broadcast_size).to(input.device), \
           torch.tensor(s, dtype=input.dtype).view(broadcast_size).to(input.device)
    input = input.sub(m).div(s)
    return input


def denormalize(input, m, s):
    broadcast_size = [1] * input.dim()
    broadcast_size[1] = input.size(1)
    m, s = torch.tensor(m, dtype=input.dtype).view(broadcast_size).to(input.device), \
           torch.tensor(s, dtype=input.dtype).view(broadcast_size).to(input.device)
    input = input.mul(s).add(m)
    return input


def loss_fn(input, output):
    if 'target' in input:
        if input['target'].dtype == torch.int64:
            loss = F.cross_entropy(output['target'], input['target'])
        else:
            loss_type = input['loss_type'] if 'loss_type' in input else cfg['loss_type']
            if loss_type == 'mae':
                loss = mae_loss(output['target'], input['target'], input['weight'])
            elif loss_type == 'mse':
                loss = mse_loss(output['target'], input['target'], input['weight'])
            elif loss_type == 'ce':
                loss = cross_entropy_loss(output['target'], input['target'], input['weight'])
            elif loss_type == 'bce':
                loss = binary_cross_entropy_loss(output['target'], input['target'], input['weight'])
            elif loss_type == 'focal':
                loss = focal_loss(output['target'], input['target'], input['weight'])
            elif loss_type == 'kld':
                loss = kld_loss(output['target'], input['target'], input['weight'])
            elif loss_type == 'kld-ce':
                alpha = 0.95
                loss = alpha * kld_loss(output['target'], input['target'], input['weight']) + (
                        1.0 - alpha) * cross_entropy_loss(output['target'], input['target'], input['weight'])
            elif loss_type == 'kld-bce':
                alpha = 0.95
                loss = alpha * kld_loss(output['target'], input['target'], input['weight']) + (
                        1.0 - alpha) * binary_cross_entropy_loss(output['target'], input['target'], input['weight'])
            elif loss_type == 'kld-focal':
                alpha = 0.95
                loss = alpha * kld_loss(output['target'], input['target'], input['weight']) + (
                        1.0 - alpha) * focal_loss(output['target'], input['target'], input['weight'])
            else:
                raise ValueError('Not valid loss type')
    else:
        return None
    return loss


def mae_loss(output, target, weight):
    mae = F.l1_loss(output, target, reduction='none')
    mae = weight * mae if weight is not None else mae
    mae = torch.sum(mae)
    mae /= output.size(0)
    return mae


def mse_loss(output, target, weight):
    mse = F.mse_loss(output, target, reduction='none')
    mse = weight * mse if weight is not None else mse
    mse = torch.sum(mse)
    mse /= output.size(0)
    return mse


def cross_entropy_loss(output, target, weight=None):
    target = (target.topk(1, 1, True, True)[1]).view(-1)
    ce = F.cross_entropy(output, target, reduction='mean', weight=weight)
    return ce


def binary_cross_entropy_loss(output, target, weight=None):
    target = (target.topk(1, 1, True, True)[1]).view(-1)
    target = F.one_hot(target, cfg['target_size']).float()
    bce = F.binary_cross_entropy_with_logits(output, target, reduction='mean', weight=weight)
    return bce


def focal_loss(output, target, weight=None, gamma=1.0):
    target = (target.topk(1, 1, True, True)[1]).view(-1)
    target = F.one_hot(target, cfg['target_size']).float()
    bce = F.binary_cross_entropy_with_logits(output, target, reduction="none")
    modulator = 1.0 if gamma == 0.0 else torch.exp(
        -gamma * target * output - gamma * torch.log1p(torch.exp(-1.0 * output)))
    focal = modulator * bce
    focal = weight * focal if weight is not None else focal
    focal = torch.sum(focal)
    focal /= torch.sum(target)
    return focal


def kld_loss(output, target, weight=None, T=1):
    kld = F.kl_div(F.log_softmax(output / T, dim=-1), F.softmax(target, dim=-1), reduction='none') * (T * T)
    kld = weight * kld if weight is not None else kld
    kld = torch.sum(kld)
    kld /= output.size(0)
    return kld
