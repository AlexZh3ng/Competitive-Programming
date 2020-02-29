n = int(input())
grid = [list(map(int, input().split())) for x in range(n)]

def isGood(grid):
  if sorted(grid[0]) != grid[0]: return False
  a = list(zip(*grid))[0]
  if list(a) != sorted(a): return False
  return True 

def rotate(grid):
  return [list(x) for x in zip(*reversed(grid))]

while not isGood(grid):
  grid = rotate (grid)

for x in grid:
  for y in x:
    print(y, end = " ")
  print()

