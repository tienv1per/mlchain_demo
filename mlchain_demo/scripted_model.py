import torch
from torchvision.models import resnet18

model = resnet18()

scripted_model = torch.jit.script(model)
scripted_model.save('resnet18_scripted.pt')
