import sys 
sys.setrecursionlimit(1000000000)

n, m = map(int, input().split())
pho = list(map(int, input().split()))
tree = [[] for x in range(n)]
subtree = [False] * n
path = [0] * n

for x in pho:
    subtree[x] = True

for x in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def findSubtree(node, parentNode):
    for x in tree[node]:
        if x == parentNode: continue
        findSubtree(x, node)
        if subtree[x]:
            subtree[node] = True        

def longestPath(node, parentNode, step):
    path[node] = step 
    for x in tree[node]:
        if x == parentNode or not subtree[x]: continue
        longestPath(x, node, step + 1)

findSubtree(pho[0], -1)
longestPath(pho[0], -1, 0)
longestPath(path.index(max(path)), -1, 0)
print((subtree.count(True) - 1)* 2 - max(path))

