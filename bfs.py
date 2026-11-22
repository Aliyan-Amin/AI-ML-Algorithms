
#=========== breadth first search ===========

from collections import deque
import networkx as nx

G = nx.DiGraph()
G.add_edges_from([
    ('S','A'), ('S','B'),
    ('A','C'), ('A','D'),
    ('B','K'), ('B','H'),
    ('C','E'), ('D','F'),
    ('H','I'), ('I','K')
])


def bfs(G, start, goal):
    queue = deque([(start, [start])])
    
    visited = set()
    
    while deque:
        
        node, path = queue.popleft()
        
        #print(f'Visited {node} with path: {path}')
        
        if node == goal:
            return path
            
        for neighbor in G.neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
            
    return None
    
    
result = bfs(G, 'S', 'F')
print(result)
            
            
            
            
            
            
            
            
            