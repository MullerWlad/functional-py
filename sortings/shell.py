import math
from random import randrange
import quick
from typing import List

def set_steps(i: int, count: int) -> List[int]:
    match (i, count):
        case (i, 0):
            return [int(i ** count)]
        case (i, count):
            return set_steps(i, count - 1) + [int(i ** count)]

def n_step(n: int, step: int) -> List[int]:
    match (n, step):
        case (n, 1):
            return [1]
    match (math.log(n - 1, step) % 1):
        case 0:
            return set_steps(step, math.log(n - 1, step))
        case k:
            return []

def rev(list: List[int]) -> List[int]:
    match list:
        case []:
            return []
        case list:
            return rev(list[1:]) + list[:1]

def steps(n: int, step: int) -> List[int]:
    return rev(n_step(n, step))

def n_point(list: List[float], step: int) -> List[float]:
    match(list, step):
        case ([], step):
            return []
        case (list, step):
            return [list[0]] + n_point(list[step:], step)

def sorted_points(list: List[float], step: int) -> List[float]:
    return quick.quick(n_point(list, step))

def _insorted_points(list: List[float], step: int, period: int) -> List[float]:
    match (list, step, period):
        case (list, step, -1):
            return []
        case (list, step, period):
            return _insorted_points(list, step, period - 1) + list[period * step + 1: (period + 1) * step]

def insorted_points(list: List[float], step: int) -> List[float]:
    return _insorted_points(list, step, step - 1)

def inserter(s_list: List[float], i_list: List[float], step) -> List[float]:
    match(s_list, i_list, step):
        case ([], [], step):
            return []
        case (s_list, i_list, step):
            return [s_list[0]] + i_list[:step - 1] + inserter(s_list[1:], i_list[step - 1:], step)

def shell_helper(list: List[float], steps: List[int]) -> List[float]:
    match (list, steps):
        case (list, []):
            return list
        case (list, steps):
            return shell_helper(inserter(sorted_points(list, steps[0]), insorted_points(list, steps[0]), steps[0]), steps[1:])

def shell(list: List[float], step: int) -> List[float]:
    match (steps(len(list), step)):
        case []:
            return []
        case ready:
            return shell_helper(list, ready)