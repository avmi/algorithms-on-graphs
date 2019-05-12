# Uses python3

import sys
import queue


def get_min(visited, dist):
    l = len(dist)
    min = float('inf')

    for v in range(l):
        if not visited[v] and dist[v] < min:
            l = v
            min = dist[v]

    return l


def distance(adj, cost, s, t):
    inf = float('inf')

    l = len(adj)
    d = [inf] * l
    d[s] = 0
    visited = [False] * l

    for _ in range(l - 1):
        v = get_min(visited, d)

        if v == l:
            break

        visited[v] = True
        i = 0
        for u in adj[v]:
            if not visited[u] and d[u] > d[v] + cost[v][i]:
                d[u] = d[v] + cost[v][i]
            i += 1

    if d[t] == inf:
        return -1

    return d[t]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
