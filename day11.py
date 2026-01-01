from collections import defaultdict
from functools import lru_cache

inp = open('input11.txt', 'r').read().split('\n')
adjlist = defaultdict(list)
for l in inp:
    source, out = l.split(':')
    outl = out.split(' ')[1:]
    adjlist[source] = outl

# PART 1
# count number of paths in graph from x to y (you -> out) - dfs dp
@lru_cache(None)
def dfs(u):
    if u == 'out':
        return 1
    return sum(dfs(v) for v in adjlist[u])
print(dfs('you'))

# PART 2
# same dfs but track dp states with dac and fft asw
@lru_cache(None)
def dfs2(u, dacs, ffts):
    if u == 'out':
        return int(dacs and ffts)
    total = 0
    for v in adjlist[u]:
        total += dfs2(v, dacs or v == 'dac', ffts or v == 'fft')
    return total
print(dfs2('svr', False, False))