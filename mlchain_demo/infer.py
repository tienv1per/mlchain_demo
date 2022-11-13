import torch
import numpy as np
from typing import Tuple
from torch.nn.functional import softmax

class Model():
    def __init__(self, weight_path: str):
        self.model = torch.jit.load(weight_path)

    def predict(self, x: np.ndarray) -> Tuple[str, float]:
        x = torch.from_numpy(x).float()
        x = x.unsqueeze(0)
        x = x.to(torch.device("cpu"))
        x = x.permute(0, 3, 1, 2)
        output = self.model(x)
        _, pred = torch.max(output, 1)
        return pred.item(), softmax(output, dim=1)[0][pred.item()].item()
