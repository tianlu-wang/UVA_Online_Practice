import os, sys, copy

"""
This code is for UVA online judge 103 problem
by Tianlu Wang
"""


def parse_input(lines):
    boxes = list()
    i = 0
    while i < len(lines):
        box = list()
        line = lines[i]
        tmp = line.strip().split()
        num_list = tmp[0]
        dimension = tmp[1]
        for j in range(num_list):
            j += 1
            line = lines[j + i]
            box.append(line.strip().split())
        boxes.append(box)
        i = i + num_list + 1
    return boxes


def sort_box(box):
    for line in box:
        line.sort()


def if_nest(linea, lineb):
    for i in range(len(linea)):
        if linea[i] >= lineb[i]:
            return False
    return True  # linea is nested by lineb


def construct_graph(box):
    # also return roots
    roots = range(len(box))
    graph = dict()
    index = range(len(box))
    for i in index:
        key_graph = i
        value_graph = set()
        for j in index:
            if j == i:
                continue
            else:
                if if_nest(box[i], box[j]):
                    roots.remove(j)
                    value_graph.add(j)
        graph[key_graph] = value_graph
    return graph, roots


def DFS(G, v, path=None):
    if path is None:
        path = [v]
    paths = []
    if v in G:
        for item in G[v]:
            t_path = copy.deepcopy(path)
            t_path.append(item)
            paths.extend(DFS(G, item, t_path))
        return paths
    else:
        paths.append(path)
        return paths


def main():
    lines = sys.stdin.readlines()
    boxes = parse_input(lines)
    print('there are %d boxes in the input file' % len(boxes))
    for i in range(len(boxes)):
        print('this is the %d box' % i)
        print boxes[i]
    print('**********finish input parse************')

    for box in boxes:
        sort_box(box)
        graph, roots = construct_graph(box)
        longest_paths = []
        for root in roots:
            paths = DFS(graph, root)
            longest_paths.append(max([(v, i) for i, v in enumerate(paths)]))
        max_len = 0
        max_list = list()
        for item in longest_paths:
            if max_len < item[1]:
                max_len = item[1]
                max_list = item[0]
        print(max_len)
        print(max_list)
if __name__ == '__main__':
    main()





