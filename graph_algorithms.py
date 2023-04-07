import copy     # used in dijkstra
discovered = [] # global variable for DFS & SCC

# BFS - BFS - BFS - BFS - BFS - BFS - BFS - BFS - BFS - BFS - BFS - BFS - BFS - BFS - BFS - BFS
# append the neighbors to the queue
# input may be an array or dict
def bfs_queue_helper(queue, nodes):
    for node in nodes: queue.append(node)
    return queue

def bfs(graph, start_node, search_node=None):
    visited = [] # visited and path may be the same for bfs, test later!
    path = []
    # attach to path once the node is explored
    queue = [start_node]
    # use a list as a queue
    # pop top of the queue and add neighbors
    while len(queue) > 0:
        cur_node = queue.pop(0)
        if cur_node not in visited:
            visited.append(cur_node)
            queue = bfs_queue_helper(queue, graph[cur_node])
            path.append(cur_node)

        if  search_node == cur_node:
            return 1  # search node found

    if search_node is not None:
        return 0      # search node not found
    
    # return path
    return path 

# DFS - DFS - DFS - DFS - DFS - DFS - DFS - DFS - DFS - DFS - DFS - DFS - DFS - DFS
dfs_flag = False    # flag used to check if the search node was found
def dfs(graph, start_node, search_node=None):
    global discovered, dfs_flag
    discovered = [start_node]
    dfs_flag = False

    # recursive version of DFS
    # loop through the neighbors of the starting node
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

    discovered.append(cur_node)     # append to discovered
    for node in graph[cur_node]:
        if node not in discovered:  # only make another recursive DFS call if the node is not in the discovered list
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
    # if node was not found on bfs traversal, return 0
    if end_node not in visited:
        return 0
    # 2 dicts, hold the weights and paths of each node
    node_weight = {}
    node_path = {}

    for node in visited:
        node_weight[node] = 999 # initialize the weights to 999
        node_path[node] = []    # initialize all paths as an empty array
        
    node_weight[start_node] = 0
    
    # pseudo dijstra algo -  or something similar :\
    for cur_node in visited:
        for neigh in graph[cur_node]:
            # calculate the edge cost from the current node to the target node
            edge_cost = graph[cur_node][neigh]
            # calculate the new possible weight 
            new_weight = copy.deepcopy(node_weight[cur_node]) + edge_cost
            cur_weight = node_weight[neigh]
            # calculate the new possible path 
            new_path = copy.deepcopy(node_path[cur_node])
            new_path.append(cur_node)
            # if the new weight is less than the current weight, replace the current path and weight
            if cur_weight > new_weight:
                node_weight[neigh] = new_weight
                node_path[neigh] = new_path
    # DEEP COPY --> Used deep copy, if not python make a reference to the path
    # thus multiple nodes will have the same path

    goal_path = node_path[end_node]
    goal_path.append(end_node)
    ret = [goal_path, node_weight[end_node], len(node_path[end_node])-1]
    return ret[0], ret[1], ret[2]

# SCC - SCC - SCC - SCC - SCC - SCC - SCC - SCC - SCC - SCC - SCC - SCC - SCC - SCC - SCC - SCC - SCC
# first pass of DFS, return the discovered order of the ndoes
# to use as a stack
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

# transpose of the grap
# create an graph with the same keys with empty values
# loop through the original graph and reverse the edges
def graph_transpose(graph):
    transpose = {}
    for key in graph: transpose[key] = {}
    
    for node in graph:
        for key in graph[node]:
            transpose[key][node] = graph[node][key]
            
    return transpose

# SCC, DFS1, transpose, DFS2, return components
def kosaraju(graph):
    stack = scc_dfs(graph)
    transpose = graph_transpose(graph)
    components = scc_second(transpose, stack)
    return components