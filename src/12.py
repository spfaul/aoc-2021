"""
See: https://adventofcode.com/2021/day/12
"""
from typing import *

class PathNode:
    def __init__(self, name: str, paths: List):
        self.name = name
        self.paths = paths

    def is_small(self) -> bool:
        return self.name.islower()

    def __repr__(self) -> str:
        return f"< name={self.name} paths={self.paths} >"

def parse_input() -> List[List[str]]:
    with open('input/12.txt', 'r') as file:
        return [line.split('-') for line in file.read().split('\n')]

def part2() -> int:
    data: List[List[str]] = parse_input()

    # generate path nodes
    node_pool: Dict[str, PathNode] = {}
    for from_node, to_node in data:
        if from_node not in node_pool.keys():
            node_pool[from_node] = PathNode(from_node, [to_node])
        else:
            node_pool[from_node].paths.append(to_node)
        if to_node not in node_pool.keys():
            node_pool[to_node] = PathNode(to_node, [from_node])
        else:
            node_pool[to_node].paths.append(from_node)

    paths = traverse_paths_2(node_pool, "start")
    
    return paths

def traverse_paths_2(pool: Dict[str, PathNode], node_name: str, restricted_nodes: Union[Dict[str, int], None] = None) -> int:
    if restricted_nodes == None:
        restricted_nodes = {}

    path_count: int = 0
    if node_name == "end":
        return 1

    node: PathNode = pool[node_name]
    if node.is_small() and node_name != "start":
        restricted_nodes[node.name] += 1

    for connected_node in node.paths:
        if connected_node == "start":
            continue
    
        if connected_node.isupper():
            path_count += traverse_paths_2(pool, connected_node, restricted_nodes.copy())
            continue
        elif connected_node not in restricted_nodes.keys():
            restricted_nodes[connected_node] = 0
    
        if 2 not in restricted_nodes.values() and restricted_nodes[connected_node] < 2:
            path_count += traverse_paths_2(pool, connected_node, restricted_nodes.copy())
        elif restricted_nodes[connected_node] < 1:
            path_count += traverse_paths_2(pool, connected_node, restricted_nodes.copy())
    return path_count

def part1() -> int:
    data: List[List[str]] = parse_input()

    # generate path nodes
    node_pool: Dict[str, PathNode] = {}
    for from_node, to_node in data:
        if from_node not in node_pool.keys():
            node_pool[from_node] = PathNode(from_node, [to_node])
        else:
            node_pool[from_node].paths.append(to_node)
        if to_node not in node_pool.keys():
            node_pool[to_node] = PathNode(to_node, [from_node])
        else:
            node_pool[to_node].paths.append(from_node)

    paths = traverse_paths_1(node_pool, "start")
    
    return paths

def traverse_paths_1(pool: Dict[str, PathNode], node_name: str, restricted_nodes: Union[List[str], None] = None) -> int:
    if restricted_nodes == None:
        restricted_nodes = ["start"]

    path_count: int = 0
    if node_name == "end":
        if len(restricted_nodes) > 1:
            return 1
        return 0

    node: PathNode = pool[node_name]
    if node.is_small():
        restricted_nodes.append(node.name)

    for connected_node in node.paths:
        if connected_node not in restricted_nodes:
            path_count += traverse_paths_1(pool, connected_node, restricted_nodes.copy())

    return path_count
    

if __name__ == '__main__':
    print(part2())
