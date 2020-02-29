import queue 

n, m, d = map(int, input().split()) 
used = False
graph = [[] for x in range(n+1)]
visited = [False] * (n+1)
MST = [[] for x in range(n+1)]

for x in range(n-1):
  a,b,c = map(int, input().split()) 
  graph[a].append((b,c, True))
  graph[b].append((a,c, True))

for x in range(m-(n-1)):
  a,b,c = map(int, input().split()) 
  graph[a].append((b,c, False))
  graph[b].append((a,c, False))
  

plan = 0 
q = queue.PriorityQueue() 
#weight, node, parent
q.put((0, 1, None, True))
while not q.empty():
  weight, node, parent, inPlan = q.get() 
  if visited[node]: continue
  visited[node] = True
  #if parent:
  #  MST[parent].append(node)
  if not inPlan: 
    plan +=  1
  for to, edge, inPlan in graph[node]: 
     if visited[to]: continue
     if to == parent: continue
     if not inPlan:
       edge += 0.01
     q.put((edge, to, node, inPlan))

print(plan)