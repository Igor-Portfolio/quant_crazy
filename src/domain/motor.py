import numpy as np




def extrem(intervalo: list) -> list | None:
    if len(intervalo) >= 2:
        return [intervalo[0], intervalo[- 1]]
    return None

def maximuns(x: np.ndarray, y:np.ndarray) -> list:

