from collections import deque, defaultdict

def BFS_SP(graph, start, goal):
    explored = []

    # Queue for traversing the
    # graph in the BFS
    queue = [[start]]

    # If the desired node is
    # reached
    if start == goal:
        print("Same Node")
        return

    # Loop to traverse the graph
    # with the help of the queue
    while queue:
        path = queue.pop(0)
        node = path[-1]

        # Condition to check if the
        # current node is not visited
        if node not in explored:
            neighbours = graph[node]

            # Loop to iterate over the
            # neighbours of the node
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                # Condition to check if the
                # neighbour node is the goal
                if neighbour == goal:
                    print("Shortest path = ", *new_path)
                    return
            explored.append(node)

    return

def MITM_SP(n: int , start: str , finish: str ) -> int:
    visited, D, src = defaultdict( lambda : False ), defaultdict(
    lambda : 0 ), defaultdict( lambda : '')
    visited[start] = visited[finish] = True
    D[start] = D[finish] = 0
    src[start], src[finish] = start, finish
    q = deque()
    q.append(start)
    q.append(finish)
    while q:
        u = q[0]
        q.popleft()
    for i in range (n):
        v = list (u)
        v[i], v[i - 1 ] = v[i - 1 ], v[i]
        v = ''.join(v)
    if not visited[v]:
        visited[v] = True
        src[v] = src[u]
        D[v] = D[u] + 1
        q.append(v)
    elif u in src and src[u] != src[v]:
        return D[u] + D[v] + 1


graph = {}
for i in range(-1998, 2001):
    for j in range(-1998, 2001):
        for k in range(-1998, 2001):
            graph[i - 1][j - 1][k - 1] = [i, i - 2, j, j - 2, k, k - 2]
print(len(' '.join(BFS_SP(graph, [239, 239, 239], [566, 566, 566]))) *
      len(' '.join(MITM_SP(graph, [239, 239, 239], [566, 566, 566]))))
