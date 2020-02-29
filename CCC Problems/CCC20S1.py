n = int(input()) 
times = [list(map(int, input().split())) for x in range(n)] 

times.sort() 

time = times[0][0]
speed = times[0][1]
maxSpeed = 0
for x in range(1, len(times)):
    newTime = times[x][0]
    newSpeed = times[x][1]
    if abs(newSpeed-speed)/(newTime-time) > maxSpeed:
        maxSpeed = abs(newSpeed-speed)/(newTime-time) 
    time = newTime 
    speed = newSpeed

print(maxSpeed)

    