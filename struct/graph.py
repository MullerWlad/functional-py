from dis import dis
from tkinter import N
from typing import NewType
v = NewType('v', dict)

def Node(name: str, data: dict) -> v:
    return {
        'name': name,
        'data': data
    }

def Bond(fst: v, snd: v, data: dict, orient: bool) -> dict:
    match orient:
        case True:
            return {
                'tag': fst['name'] + ' -> ' + snd['name'],
                'from': fst['name'],
                'to': snd['name'],
                'data': data
            }
        case False:
            return {
                'tag': fst['name'] + ' - ' + snd['name'],
                'binding': {fst['name'], snd['name']},
                'data': data
            }

def V(nodes: list[v]) -> set:
    match nodes:
        case []:
            return set()
        case nodes:
            return {nodes[0]['name']} | V(nodes[1:])

def E(bonds: list[dict]) -> set:
    match bonds:
        case []:
            return set()
        case bones:
            return {bones[0]['tag']} | E(bonds[1:])

def G(name: str, data: dict, V: set, E: set) -> dict:
    return {
        'name': name,
        'data': data,
        'V': V,
        'E': E
    }

def V_finder(list_: list[v], name: str) -> list[v]:
    return list(map(lambda x: x['data'], filter(lambda x: x['name'] == name, list_)))

def E_finder(list_: list[dict], tag: str) -> list[dict]:
    return list(map(lambda x: x['data'], filter(lambda x: x['tag'] == tag), list_))