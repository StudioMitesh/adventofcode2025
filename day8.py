inp = open('input8.txt', 'r').read().split('\n')
pts = []
for l in inp:
    x, y, z = l.split(',')
    pts.append((x,y,z))
print(pts)