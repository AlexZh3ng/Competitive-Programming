h = input() 
n = input() 
newN = sorted(h)

perms = [] 

def isPerm(s):
    if s in perms: return False 
    if sorted(s) == newN:
        perms.append(s) 
    
for x in range(0, len(n) - len(h) + 1):
    isPerm(n[x:x+len(h)]) 
    
print(len(perms))
