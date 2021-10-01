import time
# NOT
import sys
sys.setrecursionlimit(2500)

def dfs(now, neig, subsize, visited):
    visited[now] = True
    best = 1
    max1 = -1
    max2 = -1
    subsize[now] = 1
    for next in neig[now]:
        if not visited[next]:
            best = max(dfs(next, neig, subsize, visited), best)
            if subsize[next] > max1:
                max2 = max1
                max1 = subsize[next]
            elif subsize[next] > max2:
                max2 = subsize[next]

    best = max(best, max1 + 1, max1 + max2 + 1)
    subsize[now] = max(subsize[now], max1 + 1)
    return best

n = int(input())
neig = [[] for i in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, input().split())
    neig[a].append(b)
    neig[b].append(a)

subsize = [0] * (n + 1)
visited = [False] * (n + 1)

print(dfs(1, neig, subsize, visited))


# print("HARD: ", time.time() - start_time)
