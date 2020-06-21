from enum import Enum

from fastapi import APIRouter


class Models(Enum):
    alex_net = "alex_net"
    le_net = "le_net"
    res_net = "res_net"


models_router = APIRouter()


@models_router.get("/{model_name}")
async def get_model(model_name: Models):
    responses = {
        Models.alex_net: {"model_name": model_name, "message": "Deep Learning FTW!"},
        Models.le_net: {"model_name": model_name, "message": "LeCNN all the images"},
        Models.res_net: {"model_name": model_name, "message": "Have some residuals"},
    }

    return responses[model_name]
