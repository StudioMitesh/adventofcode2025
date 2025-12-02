# PART 1
inp = open('input2.txt', 'r').read().split(',')
total = 0
for rang in inp:
    s, e = rang.split('-')
    s = int(s)
    e = int(e)
    for i in range(s, e + 1):
        n = str(i)
        if n[:len(n)//2] == n[len(n)//2:]:
            total += i
print(total)

# PART 2
total2 = 0
for rang in inp:
    s, e = rang.split('-')
    s = int(s)
    e = int(e)
    for i in range(s, e + 1):
        n = str(i)
        if n in (n + n)[1:-1]:
            total2 += i
print(total2)