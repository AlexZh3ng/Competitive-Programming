t = int(input())
output = []

for x in range(t):
  n = int(input())
  if n <= 2: 
    output.append("Y")
    continue
  line = [int(input()) for y in range(n)]
  positions = []
  lastIndex = line.index(1)
  curIndex = line.index(2) 
  good = True 
  #just make a list before instead of this
  for num in range(2, n):
    nextIndex = line.index(num + 1)
    if lastIndex < nextIndex < curIndex: 
      good = False
      output.append("N")
      break
    lastIndex = curIndex 
    curIndex = nextIndex 
  if good:
    output.append("Y")
for x in output:
  print(x)
    