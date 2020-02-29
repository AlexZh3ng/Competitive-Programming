import queue

n, m, p, q = map(int, input().split())

planets = [[] for x in range(n + 1)]
cities = [[] for x in range (m + 1)]
visited = [[False] * (m+1) for x in range(n+1)]
total = 0
cur = 0

for x in range(p): 
  a, b, cost = map(int, input().split())
  cities[a].append((b, cost))
  cities[b].append((a, cost))
  total += cost * n  

for x in range(q):
  a, b, cost = map(int, input().split())
  planets[a].append((b, cost))
  planets[b].append((a, cost))
  total += cost *  m  
q = queue.PriorityQueue() 

#cost, planet, city, true = came from same planet, false otherwise
q.put((0, 1, 1))
while not q.empty(): 
  cost, planet, city= q.get() 
  if visited[planet][city]: continue 
  visited[planet][city] = True  
  cur += cost 
  for to, weight in cities[city]:
    if visited[planet][to]: continue 
    q.put((weight, planet, to))
  for to, weight in planets[planet]:
    if visited[to][city]: continue 
    q.put((weight, to, city))

print(total-cur)