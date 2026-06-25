import numpy as np


def divide_interval(interval: list | np.ndarray, n: int) -> list | np.ndarray | None:
    result = []
    if len(interval) < n:
        return None

    for i in range(0, len(interval), n):
        piece = interval[i: i + n]
        result.append(piece)

    return result


def extrem(intervalo: list) -> list | None:
    if len(intervalo) >= 2:
        return [intervalo[0], intervalo[- 1]]
    return None


def maximuns_minumus(x: np.ndarray, y: np.ndarray, n: int) -> list | None | np.ndarray:
    if len(x) < n or n == 0:
        return None
    if len(y) != len(x):
        raise ValueError('x and y must have same length, dont be dumy')
    values = []
    pos_max = []
    pos_min = []
    intervals_x = divide_interval(x, n)
    intervals_y = divide_interval(y, n)
    for idx, sublist in enumerate(intervals_y):
        extremes = extrem(sublist)
        if extremes is None:
            continue
        if max(sublist) > extremes[0] and max(sublist) > extremes[1]:
            pos_max = list(sublist).index(max(sublist))
            values.append(intervals_x[idx][pos_max])
        elif min(sublist) < extremes[0] and min(sublist) < extremes[1]:
            pos_min = list(sublist).index(min(sublist))
            values.append(intervals_x[idx][pos_min])
    return values
