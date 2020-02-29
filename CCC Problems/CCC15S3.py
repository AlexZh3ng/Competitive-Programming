import itertools as iter

g = int(input())
p = int(input())

gates = [False] * g
allPlanes = [int(input()) for x in range(p)]

for plane in allPlanes:
  if g < plane:
    plane = g
  try:
    i = list(iter.islice(gates, plane))[::-1].index(False)
    gates[plane-i-1] = True
  except:
    break
print(gates.count(True))
