import math

nodes, edges = map(int, input().split())

count = 0
graph = [[] for x in range(nodes)]
ids = [math.inf] * nodes 
lows = [math.inf] * nodes 
bridges = []
articulations = []
visited = [False] * nodes 
visited2 = [False] * nodes 

for x in range(edges):
  a, b = map(int, input().split())
  graph[a].append(b) 
  graph[b].append(a)

def dfs(at, parent):
  global count
  visited[at] = True 
  ids[at] = count
  lows[at] = count  
  count += 1 
  for nextNode in graph[at]:
    if nextNode == parent: continue
    if not visited[nextNode]:
      dfs(nextNode, at) 
      lows[at] = min(lows[at], lows[nextNode])
      if ids[at] < lows[nextNode]: 
        bridges.append((at, nextNode))
    else: 
      lows[at] = min(lows[at], ids[nextNode])

#articulations
def dfs2(at, parent):
  visited2[at] = True
  temp = 0
  for nextNode in graph[at]: 
    if visited2[nextNode]: continue
    temp += 1
    if at not in articulations:
      if ids[at] < lows[nextNode] and parent != None: 
        print(at, "A")
        articulations.append(at) 
      if ids[at] == lows[nextNode] and parent != None and lows[parent] != lows[at]:
        print(at, "B")
        articulations.append(at) 
      if temp == 2: 
        print(at, "C")
        articulations.append(at) 
    dfs2(nextNode, at)

for x in range(nodes): 
  if not visited[x]:
    dfs(x, None)

for x in range(nodes): 
  if not visited2[x]:
    dfs2(x, None)

print(bridges)
print(articulations)


'''
9 10
0 1 
0 2
1 2
2 3
2 5
3 4
5 6
5 8
6 7
7 8
'''

'''
5 6
0 2
0 1
1 2
2 3
2 4
3 4
'''

'''
4 4
0 1
1 2
1 3
2 3
'''