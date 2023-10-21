import torch as th


def batched_tensor(x: th.Tensor, batch_size: int) -> th.Tensor:
    for i in range(0, x.shape[0], batch_size):
        yield x[i:i + batch_size]
