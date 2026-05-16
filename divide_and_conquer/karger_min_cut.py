"""
Karger's Randomized Contraction Algorithm
Minimum Cut Problem

"""
import random
import copy

# Load graph from adjacency list file
graph = {}

with open('karger_min_cut_input.txt') as file:
    for line in file:
        row = list(map(int, line.split()))
        vertex = row[0]
        neighbors = row[1:]
        graph[vertex] = neighbors

# Compute a random minimum cut using Karger's algorithm
def karger_min_cut(graph):
    while len(graph) > 2:
        # Choose random edge (u, v)
        u = random.choice(list(graph.keys()))
        v = random.choice(list(graph[u]))

        # Merge vertices
        graph[u] = graph[u] + graph[v]
        del graph[v]

        # Replace all references to v with u
        for item in graph.values():
                for i in range(len(item)):
                    if item[i] == v:
                        item[i] = u

        # Remove self-loops
        graph[u] = [item for item in graph[u] if item != u]

    # Remaining edges represent the cut size
    remaining = list(graph.keys())
    cut_size = len(graph[remaining[0]])

    return cut_size

# Run algorithm multiple times
best_cut = float('inf')
for _ in range(100):
    trial_graph = copy.deepcopy(graph)
    current_cut = karger_min_cut(trial_graph)

    if current_cut < best_cut:
        best_cut = current_cut

print("Minimum cut found:", best_cut)


