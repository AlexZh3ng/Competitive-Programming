import queue 

l, w = map(int, input().split())

grid = []
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]
visited = [[False] * w for x in range(l)]
path = [[None] * w for x in range(l)]
for x in range(l):
  i = input() 
  grid.append(list(i))
  if "S" in i:
    s = (x, i.index("S"))
  if "E" in i:
    e = (x, i.index("E"))

def bfs(): 
  q = queue.Queue()
  q.put((s[0], s[1], 0, None))
  while not q.empty():
    node = q.get()
    r = node[0]
    c = node[1]
    count = node[2]
    prevNode = node[3]
    path[r][c] = prevNode
    if grid[r][c] == "E":
        return count 
    for x in range(4):
      rr = r + dr[x]
      cc = c + dc[x]
      if rr < 0 or rr >= l: continue 
      if cc < 0 or cc >= w: continue 
      if visited[rr][cc]: continue
      if grid[rr][cc] == "#": continue
      q.put((rr, cc, count+1, (r, c)))
      visited[rr][cc] = True

count = bfs()
print(count)
output = []
node = e
for x in range(count + 1):
  output.append(node)
  node = path[node[0]][node[1]]

output.reverse() 
print(output)

'''
ex input: 
5 7
S..#...
.#...#.
.#.....
..##...
#.#E.#.
'''