
#========= A*-ALORITHM ==========

import networkx as nx
import heapq


G = nx.DiGraph()
G.add_weighted_edges_from([
    ('S','A',9), 
    ('S','B',2),
    ('A','G',9),
    ('B','C',2),
    ('C','G',2)
])


heuristic = {
    'S': 6, 
    'A': 3, 
    'B': 4, 
    'C': 2, 
    'G': 0
}


def a_star(G, start, goal, h):
    
    pq = [(h[start], 0, start, [start])]
    visited = {}
    
    while pq:
        
        f_val, g_cost , node, path = heapq.heappop(pq)
        
        if node in visited and visited[node] <= g_cost: 
            continue
        
        if node == goal:
            return path, g_cost
        
        for neighbor in G.neighbors(node):
            edge_cost = G[node][neighbor]['weight']
            new_g = g_cost + edge_cost
            new_f = new_g + h[neighbor]
            heapq.heappush(pq, (new_f, new_g, neighbor, path + [neighbor]))
            
    
    return None, None
                
                
path, cost = a_star(G, 'S', 'G', heuristic)
print(path)
print(cost)












