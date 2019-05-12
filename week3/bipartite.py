# Uses python3

import sys
import queue


def bipartite(adj):
    c = [-1] * len(adj)
    c[0] = 1

    q = []
    q.append(0)

    while q:
        u = q.pop(0)
        for v in adj[u]:
            if c[v] == -1:
                c[v] = 1 - c[u]
                q.append(v)
            elif c[v] == c[u]:
                return 0

    return 1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
