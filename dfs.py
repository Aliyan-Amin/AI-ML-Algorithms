#============ depth first search ===========

import networkx as nx

G = nx.DiGraph()
G.add_edges_from([
    ('S','A'), ('S','C'),
    ('A','B'), ('B','D'), ('B','E'),
    ('C','G')
])

def dfs(G, node, goal, visited=None, path=None):
    
    if visited is None:
        visited = set()
        
    if path is None:
        path = [node]
        
    visited.add(node)
    
    if node == goal:
        return path
        
    for neighbor in G.neighbors(node):
        if neighbor not in visited:
            result = dfs(G, neighbor, goal, visited, path + [neighbor])
            if result:
                return result
                
    return None
    
    
final_result = dfs(G, 'A', 'G')
print(f'Path will be: {final_result}')