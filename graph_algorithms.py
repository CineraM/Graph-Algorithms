import copy 
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
    # bfs traversal to get the possible nodes from starting node
    visited = []
    queue = [start_node]

    while len(queue) > 0:
        cur_node = queue.pop(0)
        if cur_node not in visited:
            visited.append(cur_node)
            queue = bfs_queue_helper(queue, graph[cur_node])
    
    if end_node not in visited:
        return 0
    
    node_weight = {}
    node_path = {}

    for node in visited:
        node_weight[node] = 999
        node_path[node] = []
        
    node_weight[start_node] = 0
    
    # pseudo dijstra algo -  or something similar :\
    for cur_node in visited:
        for neigh in graph[cur_node]:

            edge_cost = graph[cur_node][neigh]

            new_weight = copy.deepcopy(node_weight[cur_node]) + edge_cost
            cur_weight = node_weight[neigh]

            new_path = copy.deepcopy(node_path[cur_node])
            new_path.append(cur_node)

            if cur_weight > new_weight:
                node_weight[neigh] = new_weight
                node_path[neigh] = new_path
            

    goal_path = node_path[end_node]
    goal_path.append(end_node)
    ret = [goal_path, node_weight[end_node], len(node_path[end_node])-1]
    return ret[0], ret[1], ret[2]


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