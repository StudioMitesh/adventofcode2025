# PART 1
inp = open('input3.txt', 'r').read().split('\n')
joltage = 0
for l in inp:
    bestr = [0] * len(l)
    bestsofar = 0
    for i in range(len(l)-1, -1, -1):
        bestsofar = max(bestsofar, int(l[i]))
        bestr[i] = bestsofar
    bestj = 0
    for i in range(len(l)-1):
        f = int(l[i])
        s = bestr[i+1]
        bestj = max(bestj, f * 10 + s)
    joltage += bestj
print(joltage)

# PART 2
joltage2 = 0
for l in inp:
    removen = len(l) - 12
    stack = []
    for i in range(len(l)):
        while removen > 0 and stack and stack[-1] < l[i]:
            stack.pop()
            removen -= 1
        stack.append(l[i])
    joltage2 += int(''.join(stack[:12]))
print(joltage2)