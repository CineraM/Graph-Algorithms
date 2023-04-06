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

dfs_path = []
dfs_flag = False
def dfs(graph, start_node, search_node=None):
    global dfs_path, dfs_flag
    dfs_path = []
    dfs_flag = False

    dfs_recursion(graph, start_node, search_node)

    if dfs_flag: return 1
    if search_node is not None:
        return 0
    
    return dfs_path

def dfs_recursion(graph, cur_node, search_node):
    global dfs_path, dfs_flag

    if dfs_flag: return # search node found
    if search_node == cur_node: # search node found, exit out of all dfs
        dfs_flag = True

    if cur_node not in dfs_path:
        dfs_path.append(cur_node)
    else:
        return

    for node in graph[cur_node]:
        dfs_recursion(graph, node, search_node)



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




# (strongly connected components)
def kosaraju(graph):
    return
    # graph: a dictionary representing the graph where the keys are the nodes and the values
            # are dictionaries representing the edges and their weights.
    #Note: Here you need to call dfs function multiple times so you can Implement seperate
         # kosaraju_dfs function if required.

    #The output:
        #list of strongly connected components in the graph,
          #where each component is a list of nodes. each component:[nconst2, nconst3, nconst8,...] -> list of nconst id's.
    return components
