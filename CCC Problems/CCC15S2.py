sizes = {"S": 1, "M": 2, "L": 3}
n = int(input())
a = int(input())

used = [False] * n
jerseys = [input() for x in range(n)]

good = 0 
def getInput(i): 
  try: 
    return int(i) - 1 
  except: 
    return i 
for x in range(a): 
  a, b = map(getInput, input().split())
  if not used[b] and sizes[a] <= sizes[jerseys[b]]:
    used[b] = True
    good += 1

print(good)