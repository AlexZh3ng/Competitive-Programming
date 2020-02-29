n, m = map(int, input().split())
graph = [[] for x in range(n)]
visited = [False] * n 
low = [0] * n  
ids = [0] * n
count = 0 
stack = []

for x in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)

def dfs(node, parent):
  global count  
  stack.append(node)
  visited[node] = True   
  low[node] = count   
  ids[node] = count
  count += 1 
  for x in graph[node]: 
    if not visited[x]:
      dfs(x, node) 
      low[node] = min(low[node], low[x])
    elif visited[x] and x in stack:
      low[node] = min(low[node], low[x]) 
  if low[node] == ids[node]: 
    print(stack, node)
    while stack[-1] != node:
      low[stack[-1]] = low[node]
      stack.pop(-1)  
    stack.pop(-1)

for x in range(n):
  if not visited[x]: 
    dfs(x, None)

print(low)
'''
8 13
0 1 
1 2 
2 0 
3 4
3 7 
4 5 
5 0 
5 6 
6 0 
6 4 
6 2 
7 3
7 5
'''
