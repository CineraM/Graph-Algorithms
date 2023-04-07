# BFS - BFS - BFS - BFS - BFS - BFS - BFS - BFS - BFS - BFS - BFS - BFS - BFS - BFS - BFS - BFS

def bfs_queue_helper(queue, nodes):
    for node in nodes: queue.append(node)
    return queue

def bfs(graph, start_node, search_node=None):
    visited = []
    path = []
    queue = [start_node]

    while len(queue) > 0:
        cur_node = queue.pop(0)
        if cur_node not in visited:
            visited.append(cur_node)
            queue = bfs_queue_helper(queue, graph[cur_node])
            path.append(cur_node)

        if  search_node == cur_node:
            return 1  # search node found

    if search_node is not None:
        return 0  # search node not found

    return path 

# DFS - DFS - DFS - DFS - DFS - DFS - DFS - DFS - DFS - DFS - DFS - DFS - DFS - DFS - DFS  
discovered = []
dfs_flag = False
def dfs(graph, start_node, search_node=None):
    global discovered, dfs_flag
    discovered = [start_node]
    dfs_flag = False

    for key in graph[start_node]:
        if key not in discovered:
            dfs_recursion(graph, start_node, search_node)

    if dfs_flag: return 1
    if search_node is not None: return 0
    
    return discovered

def dfs_recursion(graph, cur_node, search_node):
    global discovered, dfs_flag
    if dfs_flag: return         # search node found
    if search_node == cur_node: # search node found, exit out of all dfs
        dfs_flag = True

    discovered.append(cur_node)
    for node in graph[cur_node]:
        if node not in discovered:
            dfs_recursion(graph, node, search_node)

# dijkstra - dijkstra - dijkstra - dijkstra - dijkstra - dijkstra - dijkstra - dijkstra - dijkstra - dijkstra 
def dijkstra(graph, start_node, end_node):
    return
    # graph: a dictionary representing the graph where the keys are the nodes and the values
            # are dictionaries representing the edges and their weights.
    # start_node: the starting node to begin the search.
    # end_node: the node that we want to reach.

    # Outputs:
        #1. If the end_node is not reachable from the start_node, the function returns 0.

        #2. If the end_node is reachable from the start_node, the function returns a list containing three elements:
                #2.1 The first element is a list representing the shortest path from start_node to end_node.
                     #[list of nconst values in the visited order]
                #2.2 The second element is the total distance of the shortest path.
                     #(summation of the distances or edge weights between minimum visited nodes)
                #2.3 The third element is Hop Count between start_node and end_node.

    # Return the shortest path and distances
    return [path, distance, hop_count]


# SCC - SCC - SCC - SCC - SCC - SCC - SCC - SCC - SCC - SCC - SCC - SCC - SCC - SCC - SCC - SCC - SCC
scc_stack = []
scc_visited = []
def scc_dfs(graph):
    global scc_stack, scc_visited
    scc_visited = []

    for key in graph:
        if key not in scc_visited:
            scc_dfs_recursion(graph, key)

    return scc_stack

def scc_dfs_recursion(graph, cur_node):
    global scc_stack, scc_visited

    if cur_node not in scc_visited:
        scc_visited.append(cur_node)
    else:
        return
    
    for node in graph[cur_node]:
        if node not in scc_visited:
            scc_dfs_recursion(graph, node)
    scc_stack.append(cur_node)

###### second pass
discovered = []
def scc_dfs(graph):
    global discovered
    discovered = []
    for key in graph:
        if key not in discovered:
            scc_dfs_recursion(graph, key)
    return discovered

def scc_dfs_recursion(graph, cur_node):
    global discovered
    discovered.append(cur_node) # discovered
    for node in graph[cur_node]:
        if node not in discovered:
            scc_dfs_recursion(graph, node)

###### second pass################
cur_components = []
def scc_second(graph, stack):
    global discovered, cur_components
    discovered = []
    components = []
    count = 0
    for key in stack:
        if key not in discovered:
            count+=1
            if len(cur_components) > 0:
                components.append(cur_components)
                cur_components = []
            second_recursion(graph, key)
    if len(cur_components) > 0:
        if cur_components not in components:
            components.append(cur_components)

    return components

def second_recursion(graph, cur_node):
    global discovered, cur_components

    discovered.append(cur_node)
    cur_components.append(cur_node)

    for node in graph[cur_node]:
        if node not in discovered:
            second_recursion(graph, node)


def graph_transpose(graph):
    transpose = {}
    for key in graph: transpose[key] = {}
    
    for node in graph:
        for key in graph[node]:
            transpose[key][node] = graph[node][key]
            
    return transpose

def kosaraju(graph):
    stack = scc_dfs(graph)
    transpose = graph_transpose(graph)
    components = scc_second(transpose, stack)
    return components