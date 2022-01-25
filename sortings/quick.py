from typing import List

def tail(list: List[float]) -> List[float]: return list[1:]
def head(list: List[float]) -> float: return list[0]
def more(n: float, list: List[float]) -> List[float]:
    match (n, list):
        case (n, []):
            return []
        case (n, list):
            if n <= head(list):
                return [head(list)] + more(n, tail(list))
            if n > head(list):
                return more(n, tail(list))
def less(n: float, list: List[float]) -> List[float]:
    match (n, list):
        case (n, []):
            return []
        case (n, list):
            if n >= head(list):
                return [head(list)] + less(n, tail(list))
            if n < head(list):
                return less(n, tail(list))
def quick(list: List[float]) -> List[float]:
    match list:
        case []:
            return []
        case list:
            return quick(less(head(list), tail(list))) + [head(list)] + quick(more(head(list), tail(list)))