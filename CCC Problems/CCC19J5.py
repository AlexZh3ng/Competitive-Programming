rules = []
for x in range(3):
    rules.append(input().split())
    
steps, start, end = input().split()
steps = int(steps)
output = []

def substitute(string, end, count, steps):
    if count > steps:
        return False
    if string == end:
        return True
    for char in range(len(string)):
        for rule in range(len(rules)):
            if string[char:char+len(rules[rule][0])] == rules[rule][0]:
                newString = string[0:char] + rules[rule][1] + string[char + len(rules[rule][0]):]
                if substitute(newString, end, count + 1, steps):     
                    output.append([rule + 1, char + 1, newString])
                    return True

substitute(start, end, 0, steps)

for x in reversed(output):
    print(x[0], x[1], x[2])