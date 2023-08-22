import numpy as np
from config import cfg
from torchvision import transforms
from torch.utils.data import DataLoader
from torch.utils.data.dataloader import default_collate


def fetch_dataset(data_name, verbose=True):
    import datasets
    dataset = {}
    if verbose:
        print('fetching data {}...'.format(data_name))
    root = './data/{}'.format(data_name)
    if data_name in ['MNIST', 'FashionMNIST']:
        dataset['train'] = eval('datasets.{}(root=root, split=\'train\', '
                                'transform=datasets.Compose([transforms.ToTensor()]))'.format(data_name))
        dataset['test'] = eval('datasets.{}(root=root, split=\'test\', '
                               'transform=datasets.Compose([transforms.ToTensor()]))'.format(data_name))
        cfg['transform'] = {
            'train': datasets.Compose([transforms.Resize((32, 32)), transforms.ToTensor()]),
            'test': datasets.Compose([transforms.Resize((32, 32)), transforms.ToTensor()])
        }
    elif data_name in ['SVHN']:
        dataset['train'] = eval('datasets.{}(root=root, split=\'train\', '
                                'transform=datasets.Compose([transforms.ToTensor()]))'.format(data_name))
        dataset['test'] = eval('datasets.{}(root=root, split=\'test\', '
                               'transform=datasets.Compose([transforms.ToTensor()]))'.format(data_name))
        if cfg['aug']:
            cfg['transform'] = {
                'train': datasets.Compose([transforms.RandomCrop(32, padding=4), transforms.ToTensor()]),
                'test': datasets.Compose([transforms.ToTensor()])
            }
        else:
            cfg['transform'] = {
                'train': datasets.Compose([transforms.ToTensor()]),
                'test': datasets.Compose([transforms.ToTensor()])
            }
    elif data_name in ['CIFAR10']:
        dataset['train'] = eval('datasets.{}(root=root, split=\'train\', '
                                'transform=datasets.Compose([transforms.ToTensor()]))'.format(data_name))
        dataset['test'] = eval('datasets.{}(root=root, split=\'test\', '
                               'transform=datasets.Compose([transforms.ToTensor()]))'.format(data_name))
        if cfg['aug']:
            cfg['transform'] = {
                'train': datasets.Compose([transforms.RandomCrop(32, padding=4),
                                           transforms.RandomHorizontalFlip(), transforms.ToTensor()]),
                'test': datasets.Compose([transforms.ToTensor()])
            }
        else:
            cfg['transform'] = {
                'train': datasets.Compose([transforms.ToTensor()]),
                'test': datasets.Compose([transforms.ToTensor()])
            }
    else:
        raise ValueError('Not valid dataset name')
    dataset['train'].transform = cfg['transform']['train']
    dataset['test'].transform = cfg['transform']['test']
    if verbose:
        print('data ready')
    return dataset


def input_collate(batch):
    if isinstance(batch[0], dict):
        output = {key: [] for key in batch[0].keys()}
        for b in batch:
            for key in b:
                output[key].append(b[key])
        return output
    else:
        return default_collate(batch)


def make_data_loader(dataset, tag, shuffle=None):
    data_loader = {}
    for k in dataset:
        _shuffle = cfg[tag]['shuffle'][k] if shuffle is None else shuffle[k]
        data_loader[k] = DataLoader(dataset=dataset[k], shuffle=_shuffle, batch_size=cfg[tag]['batch_size'][k],
                                    pin_memory=True, num_workers=cfg['num_workers'], collate_fn=input_collate,
                                    worker_init_fn=np.random.seed(0))
    return data_loader
