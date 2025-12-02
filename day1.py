# PART 1 and PART 2
inp = open('input1.txt', 'r').read().split('\n')
total = 0
total2 = 0
pos = 50
for l in inp:
    dir = l[0]
    n = int(l[1:])
    if dir == 'L':
        if n >= pos:
            total2 += (100 - pos + n) // 100
            if pos == 0:
                total2 -= 1
        pos -= n
    else:
        pos += n
        total2 += (pos // 100)
    pos %= 100
    if pos == 0:
        total += 1
print(total)
print(total2)
