# https://github.com/ultralytics/yolov5/issues/6417
#def strip_optimizer(f='best.pt', s=''):  # from utils.general import *; strip_optimizer() 
# Strip optimizer from 'f' to finalize training, optionally save as 's'
import torch
import os
f="best - 2epoch.pt"
s="best - 2epoch - Stripped.pt"
x = torch.load(f, map_location=torch.device('cpu')) 
if x.get('ema'): 
 x['model'] = x['ema']  # replace model with ema 
for k in 'optimizer', 'best_fitness', 'wandb_id', 'ema', 'updates':  # keys 
 x[k] = None 
x['epoch'] = -1 
x['model'].half()  # to FP16 
for p in x['model'].parameters(): 
 p.requires_grad = False 
torch.save(x, s or f) 
mb = os.path.getsize(s or f) / 1E6  # filesize 
print(f"Optimizer stripped from {f},{(' saved as %s,' % s) if s else ''} {mb:.1f}MB") 

