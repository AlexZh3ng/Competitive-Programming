import queue, math

n, m = map(int, input().split()) 

capacity = [[0] * n for x in range(n)] 
flow = [[0] * n for x in range(n)]

for x in range (m):
  a,b,c = map(int, input().split())
  capacity[a][b] = c

s, e = map(int, input().split())

def bfs(): 
  q = queue.Queue() 
  levels = [-1] * n 
  levels[s] = 0 
  q.put((s, 1))
  while not q.empty():
    node, level = q.get() 
    for x in range(n):
      if flow[node][x] < capacity[node][x] and levels[x] == -1: 
        levels[x] = level 
        q.put((x, level+1))
  if levels[e] == -1: return False 
  return levels 

levelGraph = bfs()

def dfs(node, bottleneck):
  if node == e:
    return bottleneck 
  for x in range(n):
    if levelGraph[x] == levelGraph[node] + 1 and flow[node][x] < capacity[node][x]: 
      newBottleneck = dfs(x, min(bottleneck, capacity[node][x]-flow[node][x]))
      if newBottleneck and newBottleneck != math.inf:
        flow[node][x] += newBottleneck
        flow[x][node] -= newBottleneck
        return newBottleneck

total = 0 

while(levelGraph): 
  bn = dfs(s, math.inf)
  while bn:
    total += bn 
    bn = dfs(s, math.inf)
  levelGraph = bfs()

print(total)

  
