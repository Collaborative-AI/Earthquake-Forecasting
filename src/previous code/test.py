from config import cfg
from data import fetch_dataset, make_data_loader
from utils import collate, process_dataset, save_img, process_control, resume, to_device
import torch
import models

# if __name__ == "__main__":
#     input = torch.randn(10, 3, 32, 32)
#     model = torch.nn.Conv2d(3, 3, 3, 1, 1)
#     output = model(input)
#     print(output.requires_grad)
#     with torch.no_grad():
#         input = torch.randn(10, 3, 32, 32)
#         model = torch.nn.Conv2d(3, 3, 3, 1, 1)
#         output = model(input)
#         print(output.requires_grad)


# if __name__ == "__main__":
#     data_name = 'Hymenoptera'
#     subset = 'label'
#     cfg['batch_size'] = {'train': 100, 'test': 100}
#     dataset = fetch_dataset(data_name, subset)
#     data_loader = make_data_loader(dataset)
#     for i, input in enumerate(data_loader['train']):
#         input = collate(input)
#         print(input['img'].size())
#         print(input[subset].size())
#         break
#     save_img(input['img'], './output/vis/test.png')
#     exit()


# if __name__ == "__main__":
#     data_name = 'Adult'
#     subset = 'label'
#     cfg['batch_size'] = {'train': 10, 'test': 10}
#     dataset = fetch_dataset(data_name, subset)
#     data_loader = make_data_loader(dataset)
#     for i, input in enumerate(data_loader['train']):
#         input = collate(input)
#         print(input['feature'].size())
#         print(input[subset].size())
#         break
#     exit()

# import models
# import torch.nn.functional as F
# import numpy as np
# from scipy.stats import entropy
#
# from utils import resume, process_control, process_dataset, to_device


# def inception_score(output_scores):
#     output_pred_np = F.softmax(output_scores, dim=-1).cpu().numpy()
#     py = np.mean(output_pred_np, axis=0)
#     scores = []
#     for i in range(output_pred_np.shape[0]):
#         pyx = output_pred_np[i, :]
#         scores.append(entropy(pyx, py))
#     scores = np.exp(np.mean(scores))
#     print(scores)
#     output_pred_pt = F.softmax(output_scores, dim=-1)
#     py = torch.mean(output_pred_pt, dim=0)
#     # scores = []
#     # for i in range(output_pred_pt.size(0)):
#     #     pyx = output_pred_pt[i, :].cpu().numpy()
#     #     kld = entropy(pyx, py.cpu().numpy())
#     #     kld_pt = F.kl_div(py.view(1,-1).log(), output_pred_pt[[i], :], reduction='batchmean')
#     #     kld_2 = torch.sum(output_pred_pt[i, :] * torch.log(output_pred_pt[i, :] / py), dim=0)
#     #     print(kld, kld_pt, kld_2)
#     #     exit()
#     #     scores.append(kld)
#     # scores = F.kl_div(F.log_softmax(output_scores, dim=-1), py, reduction='batchmean')
#     # scores = torch.exp(scores)
#     # scores = np.exp(np.mean(scores))
#     scores = F.kl_div(py.log().view(1, -1).expand_as(output_pred_pt), output_pred_pt, reduction='batchmean').exp()
#     print(scores)
#     exit()
#     return scores
#
#
# def Accuracy(output, target, topk=1):
#     with torch.no_grad():
#         batch_size = target.size(0)
#         pred_k = output.topk(topk, 1, True, True)[1]
#         correct_k = pred_k.eq(target.view(-1, 1).expand_as(pred_k)).float().sum()
#         acc = (correct_k * (100.0 / batch_size)).item()
#     return acc


# if __name__ == "__main__":
#     # a = torch.randn(1,10)
#     # b = torch.randn(1,10)
#     # pa = torch.softmax(a, dim=-1)
#     # logpa = torch.log_softmax(a, dim=-1)
#     # pb = torch.softmax(b, dim=-1)
#     # logpb = torch.log_softmax(b, dim=-1)
#     # kld_pt = F.kl_div(logpb, pa, reduction='none')
#     # kld_my = pa * torch.log(pa / pb)
#     # print(kld_pt)
#     # print(kld_my)
#     # exit()
#     cfg['control'] = {}
#     process_control()
#     cfg['batch_size'] = {'train': 128, 'test': 128}
#     dataset = fetch_dataset(cfg['data_name'], cfg['subset'])
#     process_dataset(dataset['train'])
#     data_loader = make_data_loader(dataset)
#     model = eval('models.{}().to(cfg["device"])'.format(cfg['model_name']))
#     model_tag_list = [str(0), cfg['data_name'], cfg['subset'], cfg['model_name']]
#     cfg['model_tag'] = '_'.join([x for x in model_tag_list if x])
#     last_epoch, model, optimizer, scheduler, logger = resume(model, cfg['model_tag'], load_tag='best')
#     model.train(False)
#     scores = []
#     accs = []
#     with torch.no_grad():
#         for i, input in enumerate(data_loader['train']):
#             input = collate(input)
#             input = to_device(input, cfg['device'])
#             output = model(input)
#             scores.append(output['score'])
#             accs.append(Accuracy(output['score'], input['label']))
#     scores = torch.cat(scores, dim=0)
#     accs = torch.tensor(accs)
#     print(accs.mean())
#     print(inception_score(scores))

import torch.nn.functional as F
import copy

# if __name__ == "__main__":
# cfg['control_name'] = '_'.join([cfg['control'][k] for k in cfg['control']]) if 'control' in cfg else ''
# process_control()
# seed = 0
# model_tag_list = [str(seed), cfg['data_name'], cfg['model_name'], cfg['control_name']]
# cfg['model_tag'] = '_'.join([x for x in model_tag_list if x])
# target_model_tag_list = [str(seed), cfg['data_name'], cfg['target_model_name']]
# cfg['target_model_tag'] = '_'.join([x for x in target_model_tag_list if x])
# dataset = fetch_dataset(cfg['data_name'])
# process_dataset(dataset)

# flat_prob = torch.ones(1, cfg['target_size']) / cfg['target_size']
# flat_entropy = -torch.sum(flat_prob * torch.log(flat_prob), dim=1)
# print(flat_entropy)
#
# target_model = eval('models.{}().to(cfg["device"])'.format(cfg['target_model_name']))
# _, target_model, _, _, _ = resume(target_model, cfg['target_model_tag'], load_tag='best')
# N = 100
# data = torch.rand((N, 1, 28, 28))
# target = torch.zeros((N,)).long()
# input = {'data': data, 'target': target}
# input = to_device(input, cfg['device'])
# output = target_model(input)
# prob = output['target'].softmax(dim=-1)
# entropy = -torch.sum(prob * torch.log(prob), dim=1)
# entropy_mean = entropy.mean()
# entropy_std = entropy.std()
# print(entropy_mean, entropy_std)
#
# target_model = eval('models.{}().to(cfg["device"])'.format(cfg['target_model_name']))
# N = 100
# output = target_model(input)
# prob = output['target'].softmax(dim=-1)
# entropy = -torch.sum(prob * torch.log(prob), dim=1)
# entropy_mean = entropy.mean()
# entropy_std = entropy.std()
# print(entropy_mean, entropy_std)

# model = eval('models.{}().to(cfg["device"])'.format(cfg['target_model_name']))
# target_model = eval('models.{}().to(cfg["device"])'.format(cfg['target_model_name']))
# _, target_model, _, _, _ = resume(target_model, cfg['target_model_tag'], load_tag='best')
# data = torch.randint(0, 255, (1, *cfg['data_shape'])) / 255.
# # data = torch.zeros((1, *cfg['data_shape']), dtype=torch.float)
# init_data = copy.deepcopy(data)
# for i in range(60):
#     data.requires_grad = True
#     target = torch.zeros((1,)).long()
#     input = {'data': data, 'target': target}
#     input = to_device(input, cfg['device'])
#     output = target_model(input)
#     output_c = model(input)
#     if i < 20 or i > 40:
#         target = torch.zeros(1, cfg['target_size'], device=cfg['device'])
#         target[0, 0] = 1
#         target[0, 1:] = 1e-10
#     else:
#         target = torch.ones(1, cfg['target_size'], device=cfg['device']).softmax(dim=-1)
#     loss = F.kl_div(output['target'].log_softmax(dim=-1), target, reduction='batchmean')
#     loss.backward()
#     print(output['target'].softmax(dim=-1))
#     print(output_c['target'].softmax(dim=-1))
#     print(loss.item())
#     new_data = data - 1*data.grad
#     new_data = ((new_data * 255).round()) / 255
#     new_data = torch.clamp(new_data, 0, 1)
#     data = copy.deepcopy(new_data.detach())
#     print(F.l1_loss(init_data, data) * 255)
#     save_img(new_data, './output/vis/test_{}.png'.format(i))

# # output = torch.ones(1, cfg['target_size'], device=cfg['device']).softmax(dim=-1)
# output = torch.zeros(1, cfg['target_size'], device=cfg['device'])
# output[0, 0] = 1
# output[0, 1:] = 1e-10
# output = output.log()
# target = torch.ones(1, cfg['target_size'], device=cfg['device']).softmax(dim=-1)
# # target = torch.zeros(1, cfg['target_size'], device=cfg['device'])
# # target[0, 1] = 1
# # target[0, 0] = 1e-10
# # target[0, 2:] = 1e-10
# print(output, target)
# loss = F.kl_div(output, target, reduction='batchmean')
# print(loss)

# model = eval('models.{}().to(cfg["device"])'.format(cfg['target_model_name']))
# target_model = eval('models.{}().to(cfg["device"])'.format(cfg['target_model_name']))
# _, target_model, _, _, _ = resume(target_model, cfg['target_model_tag'], load_tag='best')
# # data = torch.randint(0, 255, (1, *cfg['data_shape'])) / 255.
# data = torch.zeros((1, *cfg['data_shape']), dtype=torch.float)
# init_data = copy.deepcopy(data)
# for i in range(20):
#     data.requires_grad = True
#     target = torch.zeros((1,)).long()
#     input = {'data': data, 'target': target}
#     input = to_device(input, cfg['device'])
#     output = target_model(input)
#     output_c = model(input)
#     target = torch.zeros(1, cfg['target_size'], device=cfg['device'])
#     target[0, 0] = 1
#     target[0, 1:] = 1e-10
#     target_c = torch.zeros(1, cfg['target_size'], device=cfg['device'])
#     target_c[0, 1] = 1
#     target_c[0, 0] = 1e-10
#     target_c[0, 2:] = 1e-10
#     loss = F.kl_div(output['target'].log_softmax(dim=-1), target, reduction='batchmean')
#     loss_c = F.kl_div(output_c['target'].log_softmax(dim=-1), target_c, reduction='batchmean')
#     loss = loss + loss_c
#     loss.backward()
#     print(output['target'].softmax(dim=-1))
#     print(output_c['target'].softmax(dim=-1))
#     print(loss.item())
#     new_data = data - 1*data.grad
#     new_data = ((new_data * 255).round()) / 255
#     new_data = torch.clamp(new_data, 0, 1)
#     data = copy.deepcopy(new_data.detach())
#     print(F.l1_loss(init_data, data) * 255)
#     save_img(new_data, './output/vis/test_{}.png'.format(i))

# torch.manual_seed(0)
# torch.cuda.manual_seed(0)
# target_model = eval('models.{}().to(cfg["device"])'.format(cfg['target_model_name']))
# _, target_model, _, _, _ = resume(target_model, cfg['target_model_tag'], load_tag='best')
# data = torch.randint(0, 255, (1, *cfg['data_shape']), device=cfg['device']) / 255.
# data.requires_grad = True
# target = torch.zeros((1,)).long()
# input = {'data': data, 'target': target}
# input = to_device(input, cfg['device'])
# output = target_model(input)
# target = torch.ones(1, cfg['target_size'], device=cfg['device']).softmax(dim=-1)
# loss = F.kl_div(output['target'].log_softmax(dim=-1), target, reduction='none').sum(dim=-1)
# loss.backward()
# grad = data.grad
# print(grad)
# m = 100
# u = (torch.randint(0, 2, (m, *cfg['data_shape']), device=cfg['device']) * 2 - 1) / 255.
# smooth = 1
# data = data.detach()
# m_data = data + smooth * u
# m_data = torch.clamp(m_data, 0, 1)
# target = torch.zeros((m,)).long()
# input = {'data': m_data, 'target': target}
# input = to_device(input, cfg['device'])
# output = target_model(input)
# target = torch.ones(m, cfg['target_size'], device=cfg['device']).softmax(dim=-1)
# m_loss = F.kl_div(output['target'].log_softmax(dim=-1), target, reduction='none').sum(dim=-1)
# est_grad = ((m_loss - loss).view(-1,1,1,1) / (smooth * u))
# print(est_grad.size(), u.size())
# est_grad = (est_grad).mean(dim=0)
# est_sign = (est_grad.sign()!=grad.sign()).float().abs().mean()
# est_error = (est_grad - grad).abs().mean()
# print(est_grad)
# print(est_sign)
# print(est_error)
from scipy.stats import beta
import numpy as np


def denormalize(input):
    broadcast_size = [1] * input.dim()
    broadcast_size[1] = input.size(1)
    m, s = cfg['stats'][cfg['data_name']]
    m, s = torch.tensor(m, dtype=input.dtype).view(broadcast_size).to(input.device), \
           torch.tensor(s, dtype=input.dtype).view(broadcast_size).to(input.device)
    input = input.mul(s).add(m)
    return input


def make_sample(m, s, size):
    m, s = np.array(m), np.array(s)
    a = m ** 2 * ((1 - m) / s ** 2 - 1 / m)
    b = a * (1 / m - 1)
    r = beta.rvs(a, b, size=size)
    return r


if __name__ == "__main__":
    cfg['control_name'] = '_'.join([cfg['control'][k] for k in cfg['control']]) if 'control' in cfg else ''
    process_control()
    seed = 0
    model_tag_list = [str(seed), cfg['data_name'], cfg['model_name'], cfg['control_name']]
    cfg['model_tag'] = '_'.join([x for x in model_tag_list if x])
    target_model_tag_list = [str(seed), cfg['data_name'], cfg['target_model_name']]
    cfg['target_model_tag'] = '_'.join([x for x in target_model_tag_list if x])
    dataset = fetch_dataset(cfg['data_name'])
    process_dataset(dataset)
    np.random.seed(0)
    torch.manual_seed(0)
    torch.cuda.manual_seed(0)
    N = 10000
    m, s = cfg['stats'][cfg['data_name']]
    print(m, s)
    # data = make_sample(m, s, [N, *cfg['data_shape'][1:], cfg['data_shape'][0]])
    # data = torch.tensor(data.transpose(0, 3, 1, 2), dtype=torch.float).contiguous()
    data = torch.randn((N, *cfg['data_shape']))
    data = denormalize(data)
    # data = torch.rand((N, *cfg['data_shape']))
    # data = torch.clamp(data, 0, 1)
    # data = (data * 255).round() / 255
    # data_0 = torch.randint(0, 127, (N // 2, *cfg['data_shape'])) / 255.
    # data_1 = torch.randint(128, 256, (N // 2, *cfg['data_shape'])) / 255.
    # data = torch.cat([data_0, data_1], dim=0)
    # data = torch.randint(0, 256, (N, *cfg['data_shape'])) / 255.
    # data = torch.rand((N, *cfg['data_shape']))
    target_model = eval('models.{}().to(cfg["device"])'.format(cfg['target_model_name']))
    _, target_model, _, _, _ = resume(target_model, cfg['target_model_tag'], load_tag='best')
    input = {'data': data}
    input = to_device(input, cfg['device'])
    with torch.no_grad():
        target_model.train(False)
        output = target_model(input)
        import matplotlib.pyplot as plt

        plt.hist(output['target'].max(-1)[1].cpu().numpy())
        plt.show()
        print(output['target'].max(-1))
        exit()
    model = eval('models.{}().to(cfg["device"])'.format(cfg['target_model_name']))
    optimizer = torch.optim.SGD(model.parameters(), lr=1e-1)
    dataset['train'] = torch.utils.data.TensorDataset(data, output['target'].cpu().detach())
    data_loader = make_data_loader(dataset, tag=cfg['model_name'])
    for epoch in range(1, 20):
        model.train(True)
        for i, input in enumerate(data_loader['train']):
            input = {'data': input[0], 'target': input[1]}
            input_size = input['data'].size(0)
            input = to_device(input, cfg['device'])
            optimizer.zero_grad()
            output = model(input)
            output['loss'].backward()
            optimizer.step()
        with torch.no_grad():
            model.train(False)
            loss = 0
            acc = 0
            for i, input in enumerate(data_loader['test']):
                input = collate(input)
                input_size = input['data'].size(0)
                input = to_device(input, cfg['device'])
                output = model(input)
                loss += output['loss'].item()
                pred_k = output['target'].topk(1, 1, True, True)[1]
                correct_k = pred_k.eq(input['target'].view(-1, 1).expand_as(pred_k)).float().sum()
                acc += (correct_k * (100.0 / input_size)).item()
            loss /= len(data_loader['test'])
            acc /= len(data_loader['test'])
            print(epoch, loss, acc)
