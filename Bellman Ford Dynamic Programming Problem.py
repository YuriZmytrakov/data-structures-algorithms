import numpy as np
import pandas as pd

def ShortestPathDP(nodes, edges, n_source, n_target):
    # implementation
    M = np.zeros(shape=(len(edges),len(nodes)))

    for n in range(len(nodes)):
        M[0,n] = np.inf

    M[0,n_target-1] = 0

    for i in range(1, len(edges)):  

        for n in range(len(nodes)):
            M[i,n] = M[i-1, n]
            print(M[i,n])

        for v, w in edges.items():
            M[i,v[0]-1] = min(M[i,v[0]-1], M[i-1, v[1]-1] + w)
            print(M[i,v[0]-1])
    print(M)

    # return path chosen 
    visited_nodes = []
    visited_nodes.append(n_source)
    while(visited_nodes[-1] != n_target):
        temp_chosen_node = None
        temp_chosen_weight = 100000000
        for v, w in edges.items():
            #print(v, w, M[n_target-1, v[1]-1])
            if v[0] == visited_nodes[-1] and M[n_target-1, v[1]-1] + w <= temp_chosen_weight:
                temp_chosen_node = v[1] 
                temp_chosen_weight = M[n_target-1, v[1]-1] + w 
        visited_nodes.append(temp_chosen_node)

    return M[n_target-1, n_source-1], visited_nodes

nodes = [1, 2, 3, 4, 5, 6]
edges = {(1,2):4, (1,3):2, (3,2):1, (3,4):8, (2,4):5, 
         (3,5):10, (4,5):2, (5,6):5, (4,6):6}
n_source = 1
n_target = 6

print(ShortestPathDP(nodes, edges, n_source, n_target)) # returns (14, (1,3,2,4,6))