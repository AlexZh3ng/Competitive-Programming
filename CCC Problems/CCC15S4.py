import queue, math

hp, n, m = map(int, input().split()) 

blacklist = [False] * n 
graph = [[] for x in range(n + 1)]
minPath = math.inf 

for x in range(m): 
  a = list(map(int, input().split()))
  graph[a[0]].append((a[1], a[2], a[3]))
  graph[a[1]].append((a[0], a[2], a[3]))

s, e = map(int, input().split())

q = queue.PriorityQueue() 

q.put((0, s, hp, None))
while not q.empty():
  time, node, curHp, prevNode = q.get()
  if node == e:
    minPath = time
    break
  for node2, time2, dmg in graph[node]: 
    if curHp - dmg <= 0: continue 
    if node2 == prevNode: continue 
    q.put((time+time2, node2, curHp-dmg, node))

if minPath == math.inf:
  print(-1)
else:
  print(minPath)

    


  