import queue

l, w = map(int, input().split())

cameraList = [] 
grid = []
visited = [] 
blacklist = [[False] * w for x in range(l)]  
vr = [1, -1, 0, 0]
vc = [0, 0, 1, -1]
conveyors = ["D", "U", "R", "L"]

for x in range(l):
  a = input() 
  grid.append(list(a))
  for y in range(len(a)): 
    if a[y] == "S":
      s = (x,y)
    elif a[y] == "C":
      cameraList.append((x,y))
      blacklist[x][y] = True
    elif a[y] == "W":
      blacklist[x][y] = True

def markCameras():  
  for camera in cameraList: 
    for x in range(4): 
      rr = camera[0] 
      cc = camera[1] 
      while grid[rr][cc] != "W":
        rr += vr[x]
        cc += vc[x]
        if grid[rr][cc] == "." or grid[rr][cc] == "S": 
          blacklist[rr][cc] = True  

def conveyor(x, y):
  if blacklist[x][y]: return False 
  if (x, y) in visited: return False 
  node = grid[x][y]
  visited.append((x, y))
  if node in conveyors: 
    a = conveyors.index(node)
    return conveyor(x + vr[a], y + vc[a])
  if grid[x][y] == ".":
    return (x, y)

def bfs(): 
  if blacklist[s[0]][s[1]]: return
  q = queue.Queue() 
  q.put((s[0], s[1], 0))
  visited.append((s))
  while not q.empty(): 
    node = q.get()
    r = node[0]
    c = node[1]
    count = node[2]
    if count > 0 and grid[r][c] == ".":
      grid[r][c] = count
    for x in range(4): 
      rr = r + vr[x]
      cc = c + vc[x]
      #if rr < 0 or rr >= l: continue 
      #if cc < 0 or cc >= w: continue
      if (rr, cc) in visited: continue 
      if blacklist[rr][cc]: continue
      if grid[rr][cc] in conveyors:
        f = conveyor(rr, cc)
        if f: 
          rr = f[0]
          cc = f[1]
        else:
          blacklist[rr][cc] = True
      q.put((rr, cc, count + 1))
      visited.append((rr, cc))


markCameras() 
bfs() 
for x in grid:
  for y in x: 
    if type(y) == int: 
      print(y)
    elif y == ".":
      print(-1)
