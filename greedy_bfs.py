
#=========== GREEDY ALGORITHM ==========



import networkx as nx
import heapq

G = nx.DiGraph()
G.add_weighted_edges_from([
    ('S','A',1), 
    ('S','B',10),
    ('A','C',2), 
    ('A','D',1),
    ('C','G',3),
    ('B','E',4),
    ('E','G',5)
])
    

heuristic = {
    'S': 6,
    'A': 4,
    'B': 5,
    'C': 2,
    'D': 3,
    'E': 3,
    'G': 0
}



def greedy_best_first(G, start, goal, h):
    
    pq = [(h[start], start, [start])]
    visited = set()
    
    
    while pq:
        
        h_value, node, path = heapq.heappop(pq)
        
        if node == goal:
            return path
            
        if node in visited:
            continue
        visited.add(node)
        
        for neighbor in G.neighbors(node):
            if neighbor not in visited:
                heapq.heappush(pq, (h[neighbor], neighbor, path + [neighbor]))
                print(f'Node:{neighbor} with path: {path} having h values {h[neighbor]}')
                
        
    return None



print('========= GREEDY ALGORITHM =========')

result = greedy_best_first(G, 'S', 'G', heuristic)
print(result)





                
    
    
    
    
    
    
    
    
    