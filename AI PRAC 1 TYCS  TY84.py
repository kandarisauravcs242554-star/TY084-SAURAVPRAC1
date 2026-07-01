from collections import deque
import time

# Graph Representation
graph = {
    "Malad West": ["Link Road", "SV Road", "WE Highway"],
    "Link Road": ["Goregaon West"],
    "SV Road": ["Jogeshwari West"],
    "WE Highway": ["Malad East"],
    "Goregaon West": ["Oshiwara"],
    "Jogeshwari West": ["Andheri West"],
    "Malad East": ["Jogeshwari East"],
    "Oshiwara": ["Andheri West"],
    "Jogeshwari East": ["Chakala"],
    "Andheri West": ["Andheri East", "Andheri Station"],
    "Chakala": ["Andheri East"],
    "Andheri Station": ["Andheri East"],
    "Andheri East": []
}

# -------------------- BFS --------------------

def bfs(graph, start, goal):
    visited = set()
    queue = deque([(start, [start])])

    print("BFS Traversal:\n")

    while queue:
        node, path = queue.popleft()

        if node not in visited:
            print(node)
            visited.add(node)

            if node == goal:
                print("\nShortest Path:")
                print(" -> ".join(path))
                return path

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

source = "Malad West"
destination = "Andheri East"

print("Source:", source)
print("Destination:", destination)
print("-" * 40)

bfs(graph, source, destination)

# -------------------- DFS --------------------

def iterative_dfs(graph, start, goal):
    visited = set()
    stack = [(start, [start])]

    print("\nDFS Traversal:\n")

    while stack:
        node, path = stack.pop()

        if node not in visited:
            print(node)
            visited.add(node)

            if node == goal:
                print("\nPath Found:")
                print(" -> ".join(path))
                return path

            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))

print("\nSource      :", source)
print("Destination :", destination)
print("-" * 40)

iterative_dfs(graph, source, destination)

# -------------------- Comparison --------------------

def bfs_compare(graph, start, goal):
    visited = set()
    queue = deque([(start, [start])])

    while queue:
        node, path = queue.popleft()

        if node not in visited:
            visited.add(node)

            if node == goal:
                return path

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

def dfs_compare(graph, start, goal):
    visited = set()
    stack = [(start, [start])]

    while stack:
        node, path = stack.pop()

        if node not in visited:
            visited.add(node)

            if node == goal:
                return path

            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))

# Measure BFS Time
start_time = time.time()
bfs_path = bfs_compare(graph, source, destination)
bfs_time = time.time() - start_time

# Measure DFS Time
start_time = time.time()
dfs_path = dfs_compare(graph, source, destination)
dfs_time = time.time() - start_time

print("\n===== BFS vs DFS Comparison =====\n")

print("BFS Path:", " -> ".join(bfs_path))
print("DFS Path:", " -> ".join(dfs_path))

print("\nExecution Time:")
print("BFS Time:", bfs_time)
print("DFS Time:", dfs_time)

print("\nConclusion:")
print("BFS gives the shortest path from Malad West to Andheri East, whereas DFS explores one route completely before backtracking and may not return the shortest path.")