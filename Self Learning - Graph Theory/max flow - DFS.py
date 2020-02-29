n, m = map(int, input().split()) 

capacity = [[0] * n for x in range(n)] 
flow = [[0] * n for x in range(n)]
path = [-1] * n
for x in range (m):
  a,b,c = map(int, input().split())
  capacity[a][b] = c

s, e = map(int, input().split())

maxFlow = 0 
stack = [] 
def updatePath():
  global maxFlow
  nodes = []
  parents = [] 
  flows = [] 
  node = e 
  parent = path[node]
  while parent != -1: 
    nodes.append(node)
    parents.append(parent)
    flows.append(capacity[parent][node] - flow[parent][node])
    node = parent  
    parent = path[node] 
  bottleneck = min(flows)
  if bottleneck == 0: return  
  for x in range(len(nodes)):
    flow[nodes[x]][parents[x]] -= bottleneck 
    flow[parents[x]][nodes[x]] += bottleneck 
  maxFlow += bottleneck


def dfs(node, parent): 
  path[node] = parent
  if node == e:
    updatePath() 
    return 
  stack.append(node)
  for x in range(n):
    if x in stack: continue
    newBottle = capacity[node][x] - flow[node][x]
    if newBottle == 0: continue 
    dfs(x, node)
  stack.pop(-1)
    

dfs(s, -1)
print(maxFlow)
'''
s1:
6 7
0 1 10
0 2 10
1 3 25
2 4 15
3 5 10
4 1 6
4 5 10
0 5
s2: 
11 17
0 1 7
0 2 2
0 3 1
1 4 2
1 5 4
2 5 5
2 6 6
3 8 8
3 4 4
4 7 7
4 8 1
5 6 8
5 9 3
6 9 3
7 10 1
8 10 3
9 10 4
0 10
'''