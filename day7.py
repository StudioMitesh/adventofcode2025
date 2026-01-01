from collections import defaultdict

inp = open('input7.txt', 'r').read().split('\n')
sidx = inp[0].index('S')

# PART 1
indxs = set()
indxs.add(sidx)
splits = 0
for i in range(len(inp)-1):
    indxsi = indxs.copy()
    for ci in indxsi:
        # split
        if ci-1 >= 0 and ci+1 < len(inp[0]) and inp[i][ci] == '^':
            if ci in indxs:
                indxs.remove(ci)
            if ci-1 >= 0:
                indxs.add(ci-1)
            if ci+1 < len(inp[0]):
                indxs.add(ci+1)
            splits += 1
print(splits)

# PART 2
dp = {sidx: 1}
for i in range(len(inp)-1):
    nxt = defaultdict(int)
    for j, n in dp.items():
        cell = inp[i][j]
        if cell == '^':
            if j-1 >= 0:
                nxt[j-1] += n
            if j+1 < len(inp[0]):
                nxt[j+1] += n
        else:
            nxt[j] += n
    dp = nxt
print(sum(dp.values()))

