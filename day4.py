# PART 1
inp = open('input4.txt', 'r').read().split('\n')
dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
total = 0
for i in range(len(inp)):
    for j in range(len(inp[0])):
        if inp[i][j] == '@':
            countat = 0
            for dx, dy in dirs:
                ni, nj = i + dx, j + dy
                if 0 <= ni < len(inp) and 0 <= nj < len(inp[0]) and inp[ni][nj] == '@':
                    countat += 1
            if countat < 4:
                total += 1
print(total)

# PART 2
total2 = 0
changed = True
while changed:
    changed = False
    removes = []
    for i in range(len(inp)):
        for j in range(len(inp[0])):
            if inp[i][j] == '@':
                countat = 0
                for dx, dy in dirs:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < len(inp) and 0 <= nj < len(inp[0]) and inp[ni][nj] == '@':
                        countat += 1
                if countat < 4:
                    total2 += 1
                    removes.append((i, j))
    if removes:
        changed = True
        for i, j in removes:
            inp[i] = inp[i][:j] + '.' + inp[i][j+1:]
print(total2)