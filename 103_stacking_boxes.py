import os, sys, copy

"""
This code is for UVA online judge 103 problem
by Tianlu Wang
"""


def parse_input(line):
    box = list()
    tmp = line.strip().split()
    num_list = tmp[0]
    dimension = tmp[1]
    for j in range(int(num_list)):
        j += 1
        line = sys.stdin.readline()
        box.append([int(item) for item in line.strip().split()])
    return box


def sort_box(box):
    for line in box:
        line.sort()


def if_nest(linea, lineb):
    for i in range(len(linea)):
        if int(linea[i]) >= int(lineb[i]):
            return False
    return True  # linea is nested by lineb


def construct_graph(box):
    # also return roots
    roots = range(len(box))
    graph = dict()
    index = range(len(box))
    for i in index:
        key_graph = i
        value_graph = list()
        for j in index:
            if j == i:
                continue
            else:
                if if_nest(box[i], box[j]):
                    if j in roots:
                        roots.remove(j)
                    value_graph.append(j)
        graph[key_graph] = value_graph
    return graph, roots


def DFS(G,v,path=None):
    if path is None: path = [v]
    paths = []
    if v in G and not G[v] == []:
        for item in G[v]:
            t_path = copy.deepcopy(path)
            t_path.append(item)
            paths.extend(DFS(G, item, t_path))
        return paths
    else:
        paths.append(path)
        return paths


def get_longest_path(paths):
    max_len = 0
    max_list = list()
    for item in paths:
        if max_len < len(item):
            max_len = len(item)
            max_list = item
    result = (max_list, max_len)
    return result


def main(box):
    sort_box(box)
    graph, roots = construct_graph(box)
    longest_paths = []
    for root in roots:
        paths = DFS(graph, root, path=None)
        longest_paths.append(get_longest_path(paths))
    max_len = 0
    max_list = list()
    for item in longest_paths:
        if max_len < item[1]:
            max_len = item[1]
            max_list = item[0]
    print(max_len)
    out_put = ""
    for item in max_list:
        out_put += str(int(item)+1) + ' '
    print(out_put)
    return

if __name__ == '__main__':
    while True:
        line = sys.stdin.readline()
        # print(line)
        if line == "":
            break
        else:
            box = parse_input(line)
            main(box)





