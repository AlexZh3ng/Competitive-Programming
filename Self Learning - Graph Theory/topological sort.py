import math 

n, e= map(int, input().split())
graph = [[] for x in range(n)]
visited = [False] * n 
order = []
distance = [math.inf] * n  
for x in range(e):
  i = list(map(int, input().split()))
  graph[i[0]].append((i[1], i[2]))

def dfs(i):
  visited[i] = True 
  for x in graph[i]: 
    if not visited[x[0]]:
      dfs(x[0]) 
  order.append(i)

while False in visited: 
  i = visited.index(False) 
  dfs(i) 

order.reverse()

distance[order[0]] = 0 
for i in order: 
  connected = graph[i]
  for edge in connected: 
    index = edge[0]
    weight = edge[1]
    if weight + distance[i] < distance[index]:
      distance[index] = weight + distance[i]

print(distance)



'''
8 13 
0 1 3
0 2 6 
1 2 4
1 3 4
1 4 11
2 3 8 
2 6 11
3 4 -4
3 5 5
3 6 2
4 7 9
5 7 1
6 7 2
'''