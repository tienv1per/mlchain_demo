from mlchain.base import ServeModel
from mlchain import mlconfig
from infer import Model

model = Model(weight_path=mlconfig.weight_path)


serve_model = ServeModel(model)
