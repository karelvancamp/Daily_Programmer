from collections import defaultdict
from itertools import product
from math import ceil
from itertools import chain, combinations, combinations_with_replacement as cwr
from time import time, sleep

def solve(X, Y, solution=[]):
    """
    A variation of the dancing links alogrithm for the exact cover problem.
    X is a dict containing sets of objects contained per node
    Y is a dict containing a list of all nodes contained in an object
    It returns an iterable of the solutions to the exact cover problem.
    """
    if not X:
        yield list(solution)
    else:
        c = min(X, key=lambda c: len(X[c]))
        for r in list(X[c]):
            solution.append(r)
            cols = select(X, Y, r)
            for s in solve(X, Y, solution):
                yield s
            deselect(X, Y, r, cols)
            solution.pop()
            
def select(X, Y, r):
        cols = []
        for j in Y[r]:
            for i in X[j]:
                for k in Y[i]:
                    if k != j:
                        X[k].remove(i)
            cols.append(X.pop(j))
        return cols
def deselect(X, Y, r, cols):
        for j in reversed(Y[r]):
            X[j] = cols.pop()
            for i in X[j]:
                for k in Y[i]:
                    if k != j:
                        X[k].add(i)
						
def positions_in_square(objects, square_size):
    """
    Translates an iterable of rectangles
    to all valid posistions in a square.
    
    The rectangles are an iterable of tiles,
    each described by a coordinate tuple. 
    It is assumed a (0,0) coordinate is included for each rectangle.
    
    Projects coordinates to integers.
    """
    region_set = set(product(range(square_size), repeat=2))
    max_ = square_size**2
    region = list(region_set)
    positions = defaultdict(set)
    for ix, tiles in enumerate(objects):
        for (oi, oj), rk in product(region, (0, 1)):
            # Reflect diagonally if rk = 1
            placing = []
            for t in tiles:
                p = t[rk] + oi, t[1-rk] + oj
                if p not in region_set:
                    break
                placing.append(p[0]*square_size+p[1])
            else:
                placing = tuple(sorted(placing))
                positions[ix].add(placing)
                
    return positions

def positions_to_constraints(positions):
    """
    Takes a dict of positions of objects
    Returns the positions as cover constraints, 
    where the same objects can not coexist with an alternate position.
    """
    nodes = defaultdict(set)
    objects = defaultdict(tuple)
    
    c = 0
    for x,y in positions.items():
        for z in y:
            c += 1
            for i in z:
                nodes[i].add(c)
            nodes[-x-1].add(c)
            objects[c] = (-x-1,)+z
        # allow not-used objects
        # c += 1
        # nodes[-x-1].add(c)
        # objects[c] = (-x-1,)
    return nodes, objects

def solution(objects,square_size):
    """
    Takes a list of objects and a square size, 
    and retuns an exact cover if there eixsts one.
    """
    p = positions_in_square(objects,square_size)
    X,Y = positions_to_constraints(p)
    try: 
        return [[divmod(x,square_size) for x in Y[y][1:]] 
                for y in next(solve(X,Y, solution=[]))]
    except: 
        return False

def mulx(x):
    return x[0]*x[1]

def minx(x):
    return x[0]-x[1]

def upper_bound(n):
    mx = ceil(((n**2)/3)**0.5)
    return (mx,mx),(n,n-mx),(n-mx,mx)

def limits_bound(n):
    a,b,c = map(mulx,upper_bound(n))
    return max(a,b,c), min(a,b,c)

def rectangles(n):
    a,b = limits_bound(n)
    return [x for x in cwr(range(1,n+1),2) if mulx(x) <= a]

def rectangles_to_tiles(R):
    return [list(product(range(x),range(y))) for x,y in R]

def cover_cost(a_solution):
    c = [len(x) for x in a_solution if x]
    return max(c)-min(c)

	
def surface_ranges(n):   
    r = sorted(rectangles(n),key = lambda x:mulx(x))
    p = []
    for ix,_ in enumerate(r):
        for iy,_ in enumerate(r):
            v = r[ix:iy+1]
            if sum(mulx(x) for x in v) >= n**2:
                p.append(sorted(v,key = lambda x:mulx(x), reverse=True))
    return p

def run(n):
    p = surface_ranges(n)
    p = [(mulx(x[0])-mulx(x[-1]),x) for x in p]
    limit = minx(limits_bound(n))
    d = defaultdict(list)
    for x,y in p:
        if 0 < x <= limit:
            d[x].append(tuple(y))
    for x,y in d.items():
        y.sort(key=lambda x:(1/len(x),mulx(x[0])), reverse=True)
    return d
	
def give_change(change, coins):
    subsets = (combinations(coins, x) for x in range(1,len(coins)+1))
    changes = (a_set for a_range in subsets for a_set in a_range if sum(mulx(y) for y in a_set) == change)
    return changes
	
def mondriaan(n):
    a,b = limits_bound(n)
    limit = a-b
    ranges = run(n)
    limits = sorted([x for x in ranges.keys() if x <= limit], reverse=True)
    seen = set()
    s = n**2
    
    while limits:
        limit = limits.pop()
        for a_range in ranges[limit]:
            for x in give_change(s, a_range):
                if x not in seen:
                    seen.add(x)
                    try:
                        b = rectangles_to_tiles(x)
                        v = solution(b,n)
                    except:
                        v = None
                    if v:
                        last_sol = cover_cost(v)
                        return n,last_sol,x

for x in range(3,18):
    t = time()
    b = mondriaan(x)
    print(f"{time()-t:.3f} s",b)
    sleep(0.001)