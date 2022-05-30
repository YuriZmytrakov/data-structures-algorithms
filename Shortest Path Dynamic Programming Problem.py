import numpy as np


def ShortestPathDP(nodes, edges, n_source, n_target):
    M_table = np.zeros(shape=(len(edges), len(nodes)))
    for n in range(len(nodes)):
        M_table[0, n] = np.inf
    M_table[0, n_target-1] = 0
    for i in range(1, len(edges)):
        for n in range(len(nodes)):
            M_table[i, n] = M_table[i-1, n]
        for vertix, weight in edges.items():
            M_table[i, vertix[0]-1] = min(M_table[i, vertix[0]-1],
                                          M_table[i-1, vertix[1]-1] + weight)
    print('Dynamic programming table:')
    print(M_table)

    visited = []
    visited.append(n_source)
    while(visited[-1] != n_target):
        temp = None
        temp_w = 100000000
        for v, w in edges.items():
            if v[0] == visited[-1] and M_table[n_target-1, v[1]-1] + w <= temp_w:
                temp = v[1]
                temp_w = M_table[n_target-1, v[1]-1] + w
        visited.append(temp)

    l2 = []
    for i in range(len(visited)-1):
        temp_l = []
        temp_l.append(visited[i])
        temp_l.append(visited[i+1])
        l2.append(temp_l)
    visited_nodes_tuple = tuple(map(tuple, l2))

    return M_table[n_target-1, n_source-1], visited_nodes_tuple


n_source = 1
n_target = 6
nodes = [1, 2, 3, 4, 5, 6]
edges = {(1, 2): 4, (1, 3): 2, (3, 2): 1, (3, 4): 8, (2, 4): 5,
         (3, 5): 10, (4, 5): 2, (5, 6): 5, (4, 6): 6}

# function returns target (14, ((1,3),(3,2),(2,4),(4,6)))
print(ShortestPathDP(nodes, edges, n_source, n_target))
