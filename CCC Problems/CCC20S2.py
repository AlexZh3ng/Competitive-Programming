import queue 

m = int(input())
n = int(input()) 

grid = [[" "] + list(map(int, input().split())) for x in range(m)]
grid.insert(0, [" "] * n)
visited = [[False] * (n+1) for x in range(m+1)] 
checked = [] 
goal = m * n
good = False 
def getFactors(n): 
    return [(x, n//x) for x in range(1, int(n**(1/2))+1) if n % x == 0] 


q = queue.Queue() 
q.put((1, 1)) 

while not q.empty():
    row, col = q.get() 
    value = grid[row][col] 
    if value == goal:
        good = True 
        break 
    if value in checked: continue 
    factors = getFactors(value)
    for nr, nc in factors: 
        if nr <= m and nc <= n and not visited[nr][nc]: 
            visited[nr][nc] = True
            q.put((nr, nc)) 
        if nc <= m and nr <= n and not visited[nc][nr]: 
            visited[nc][nr] = True
            q.put((nc, nr))
    
if good: 
    print("yes") 
else:
    print("no")