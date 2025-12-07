# PART 1
fullinp = open('input5.txt', 'r').read().split('\n\n')
ranges = fullinp[0].split('\n')
nums = fullinp[1].split('\n')
total = 0
for n in nums:
    n = int(n)
    for r in ranges:
        a, b = map(int, r.split('-'))
        if a <= n <= b:
            total += 1
            break
print(total)

# PART 2
total2 = 0
ranges = sorted(ranges, key=lambda x: int(x.split('-')[0]))
unmerged = []
for r in ranges:
    a, b = map(int, r.split('-'))
    unmerged.append((a, b))
merged = []
for a, b in unmerged:
    if not merged or merged[-1][1] < a - 1:
        merged.append([a, b])
    else:
        merged[-1][1] = max(merged[-1][1], b)
for m, n in merged:
    m = int(m)
    n = int(n)
    print(m, n)
    total2 += (n - m + 1)
print(total2)