import queue, math

n, e = map(int, input().split())
grid = [[] for x in range(n)]
visited = [False] * n
dist = [math.inf] * n
for x in range(e):
  a = list(map(int, input().split()))
  grid[a[0]].append((a[1], a[2]))

s = 0 
dist[s] = 0 
q = queue.PriorityQueue()
q.put((0, s))
while not q.empty(): 
  minValue, i = q.get() 
  if visited[i]: continue
  visited[i] = True 
  for x in grid[i]: 
    j, weight = x 
    if visited[j]: continue
    newMin = dist[i] + weight
    if newMin < dist[j]: 
      dist[j] = newMin 
      q.put((newMin, j))

print(dist)




'''
5 6
0 1 4 
0 2 1
1 3 1
2 1 2
2 3 5
3 4 3
'''