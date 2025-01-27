graph = {
    'James': {'Heuston': 4},
    'Heuston': {'Arran': 5, 'James': 4, 'Museum': 6}, 
    'Museum': {'Heuston': 6, 'Smithfield': 8}, 
    'Smithfield': {'Four': 3, 'Museum': 8, 'Jervis': 4}, 
    'Jervis': {'Smithfield': 4, 'Abbey_Street': 4}, 
    'Abbey_Street': {'GPO': 5, 'Marlborough': 3, 'Jervis': 4, 'Busarast': 5}, 
    'Busarast': {'Custom': 5, 'Abbey_Street': 5, 'George': 4}, 
    'George': {'Busarast': 4}, 
    'Connell': {'GPO': 5, 'Marlborough': 3}, 
    'GPO': {'Abbey_Street': 5, 'Connell': 5, 'Westmoreland': 5}, 
    'Westmoreland': {'GPO': 5}, 
    'Marlborough': {'Abbey_Street': 3, 'Connell': 3}, 
    'Arran': {'Heuston': 5, 'Four': 3}, 
    'Four': {'Smithfield': 3, 'Arran': 3, 'Custom': 5}, 
    'Custom': {'Busarast': 5, 'Four': 5}
}


def dijkstra(graph, start):
    # Initializing distances and sets of untracked vertices
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())

    while unvisited:
        # Finding the vertex with the smallest distance among the undetected
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        # If the current distance is infinity, then we have completed the work
        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight

            # If the new distance is shorter, then update the shortest path
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        # Remove the current vertex from the set of unanswered
        unvisited.remove(current_vertex)

    return distances


print(dijkstra(graph, "GPO"))