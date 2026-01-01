from collections import defaultdict, deque

inp = open('input9.txt', 'r').read().split('\n')
coords = []
maxw, maxh = 0, 0
for c in inp:
    a, b = c.split(',')
    coords.append((int(a),int(b)))
    maxw = max(maxw, int(a))
    maxh = max(maxh, int(b))
maxw += 1
maxh += 1

# PART 1
area = 0
for i in range(len(coords)):
    for j in range(i+1, len(coords)):
        x1, y1 = coords[i]
        x2, y2 = coords[j]
        area = max(area, (abs(x1-x2)+1) * (abs(y1-y2)+1))
print(area)

# PART 2
perimeter = set()
n = len(coords)

for i in range(n):
    x1, y1 = coords[i]
    x2, y2 = coords[(i+1) % n]

    if x1 == x2:
        lo, hi = sorted([y1, y2])
        for y in range(lo, hi + 1):
            perimeter.add((x1, y))
    else:
        lo, hi = sorted([x1, x2])
        for x in range(lo, hi + 1):
            perimeter.add((x, y1))

filled = set(perimeter)
rows = defaultdict(list)

for x, y in perimeter:
    rows[y].append(x)

for y, xs in rows.items():
    xs.sort()
    for i in range(0, len(xs) - 1, 2):
        for x in range(xs[i], xs[i + 1] + 1):
            filled.add((x, y))

row_interval = {}
for x, y in filled:
    if y not in row_interval:
        row_interval[y] = [x, x]
    else:
        row_interval[y][0] = min(row_interval[y][0], x)
        row_interval[y][1] = max(row_interval[y][1], x)

best = 0
for i in range(len(coords)):
    for j in range(i + 1, len(coords)):
        x1, y1 = coords[i]
        x2, y2 = coords[j]
        xmin, xmax = sorted([x1, x2])
        ymin, ymax = sorted([y1, y2])
        ok = True
        for y in range(ymin, ymax + 1):
            if y not in row_interval:
                ok = False
                break
            L, R = row_interval[y]
            if xmin < L or xmax > R:
                ok = False
                break
        if ok:
            area = (xmax - xmin + 1) * (ymax - ymin + 1)
            best = max(best, area)
print(best)
