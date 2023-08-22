import torch
from utils import recur
from config import cfg


def Accuracy(output, target, topk=1):
    with torch.no_grad():
        batch_size = target.size(0)
        if target.dtype == torch.float32:
            target = target.topk(1, 1, True, True)[1].view(-1)
        pred_k = output.topk(topk, 1, True, True)[1]
        correct_k = pred_k.eq(target.view(-1, 1).expand_as(pred_k)).float().sum()
        acc = (correct_k * (100.0 / batch_size)).item()
    return acc


class Metric(object):
    def __init__(self, metric_name):
        self.metric_name = self.make_metric_name(metric_name)
        self.pivot, self.pivot_name, self.pivot_direction = self.make_pivot()
        self.metric = {'Loss': (lambda input, output: output['loss'].item()),
                       'Loss_C': (lambda input, output: output['loss_c'].item()),
                       'Loss_G': (lambda input, output: output['loss_g'].item()),
                       'Accuracy': (lambda input, output: recur(Accuracy, output['target'], input['target']))}

    def make_metric_name(self, metric_name):
        for split in metric_name:
            if cfg['data_name'] in ['MNIST', 'FashionMNIST', 'SVHN', 'CIFAR10']:
                metric_name[split] += ['Accuracy']
            else:
                raise ValueError('Not valid data name')
        return metric_name

    def make_pivot(self):
        if cfg['data_name'] in ['MNIST', 'FashionMNIST', 'SVHN', 'CIFAR10']:
            pivot = -float('inf')
            pivot_name = 'Accuracy'
            pivot_direction = 'up'
        else:
            raise ValueError('Not valid data name')
        return pivot, pivot_name, pivot_direction

    def evaluate(self, metric_names, input, output):
        evaluation = {}
        for metric_name in metric_names:
            evaluation[metric_name] = self.metric[metric_name](input, output)
        return evaluation

    def compare(self, val):
        if self.pivot_direction == 'up':
            compared = self.pivot < val
        else:
            raise ValueError('Not valid pivot direction')
        return compared

    def update(self, val):
        self.pivot = val
        return
