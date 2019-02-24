graph = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C']}

############BFS normal version###################
#visit all nodes of a graph (connected component)
def bfs_connected_component(graph, start):
    #keep track of all the nodes visited
    explored = []
    #keep track of nodes to be checked
    queue = [start]

    #iterate over nodes till all nodes are explored
    while queue:
        #pop node at the lowest level from the queue
        node = queue.pop(0)
        if node not in explored:
            #add node to the list of checked nodes
            explored.append(node)
            neighbours = graph[node]

            for n in neighbours:
                queue.append(neighbour)
        return explored

############BFS shortest path version###################
def bfs_connected_component(graph, start,goal):
    #keep track of all the nodes visited
    explored = []
    #keep track of nodes to be checked
    queue = [[start]]

    #return path if start is the goal
    if start == goal:
        return "start=goal"

    #iterate over nodes till all nodes are explored
    while queue:
        #pop node at the lowest level from the queue
        path = queue.
        #get the last node from the path
        node = path[-1]
        if node not in explored:
            #add node to the list of checked nodes
            neighbours = graph[node]
            for n in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                #return path if neighbour is goal
                if neighbour == goal:
                    return new_path

            explored.append(node)

        return explored
