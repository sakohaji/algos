#Sako Haji
#04/21/2019


avail_edges = {"0": ["1", "2", "3"],"1": ["4", "5"], "2": ["5"], "3": ["6"], "4": ["7"], "5": ["7"], "6": ["7"], "7": []}
graph = {}

def flow():
        counter = 0
        graph = avail_edges
        pointer = "0"
        while BFS(pointer, graph):
            
            next_child = graph[pointer][0]
            #print(graph,"pointer",pointer, "child",next_child)
            graph[pointer].remove(next_child)
            graph[next_child].append(pointer)
            pointer = next_child
            if pointer == "7":
                pointer = "0"
                counter += 1
                if counter == 3:
                    print("You have reached optimal flow!")
                    print(graph)
                
        
        
def BFS(start, graph):
    visited = []
    next_node = [start]
    while next_node != []:
        pointer = next_node.pop(0)
        visited.append(pointer)
        for i in graph[pointer]:
            if i == "7":
                return True
            if i not in visited and i not in next_node:
                next_node.append(i)
                
    return False
flow()
        
        
    
    
            
