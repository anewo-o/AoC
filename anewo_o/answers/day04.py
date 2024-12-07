"""
import numpy as np
import scipy.ndimage as ndi
with open("anewo_o/inputs/day4.txt", "r") as file:
    horiz = np.array([ list(line) for line in file.read().splitlines()])
    vert = horiz.transpose()
    ...rotate 45° ??
"""

with open("anewo_o/inputs/day04.in", "r") as f:
    data = f.read().splitlines()


"""
dxy = pos(X)
        where 
            X X X
            X O X
            X X X
"""
dxy = []
for dx in [-1, 0, 1]:
    for dy in [-1, 0, 1]:
        if dx == 0 and dy == 0:
            continue
        dxy.append((dx, dy))


def directed_search(str, data, x, y, dx, dy):
    n, m = len(data), len(data[0])

    if not (0 <= x < n and 0 <= y < m) :
        return False
    current_letter = data[x][y]
    

    if current_letter == str[0]:
        for i in range(1, len(str)):
            x += dx; y += dy
            if not (0 <= x < n and 0 <= y < m) :
                return False
            next_letters = data[x][y]
            if next_letters != str[i]:
                return False
        return True


ans = 0
n, m = len(data), len(data[0])

# for each letter
for x in range(n):
    for y in range(m):
        # for each direction
        for dx, dy in dxy:
            if directed_search("XMAS", data, x, y, dx, dy):
                ans += 1

print("Answer 1: ", ans)


# Part 2

def cross_search(data, x, y):
    n, m = len(data), len(data[0])

    if not (1 <= x < n-1 and 1 <= y < m-1):
        return False
    if not (data[x][y] == "A"):
        return False
    
    diags = ["MS", "SM"]
    diag1 = data[x-1][y-1]+data[x+1][y+1]
    diag2 = data[x-1][y+1]+data[x+1][y-1]
    if diag1 in diags and diag2 in diags:
        return True
    return False

ans = 0
for x in range(n):
    for y in range(m):
        if cross_search(data, x, y):
            ans += 1
                    


print("Answer 2: ", ans)

"""
trop général...
def cross_search(str, data, x, y):
    n, m = len(data), len(data[0])
    s = len(str)

    if not (0 <=  x  < n and 0 <=  y  < m)\
    or not (0 <= x+1 < n and 0 <= y+1 < m)\
    or not (0 <= x-1 < n and 0 <= y-1 < m)\
    or not (0 <= x+1 < n and 0 <= y-1 < m)\
    or not (0 <= x-1 < n and 0 <= y+1 < m):
        return False
    if s%2 != 1:
        return False

    if data[x][y] == str[s//2+1]:
        for i in range(1, s//2):
            if data[x][y] != str[i]:
                return False
        return True
"""

"""
dxy = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

for x in range(n):
    for y in range(m):
        # for each direction
        for dx, dy in dxy:
            if directed_search("MAS", data, x, y, dx, dy) :
                xa, ya = x+dx, y+dy
                xms, yms = x+dx, y-dy
                xsm, ysm = x-dx, y+dy
                if not (0 <= xa < n and 0 <= ya < m) \
                or not (0 <= xms < n and 0 <= yms < m) \
                or not (0 <= xsm < n and 0 <= ysm < m):
                    continue
                if data[xms][yms] == "M" and data[xsm][ysm] == "S"\
                or data[xms][yms] == "S" and data[xsm][ysm] == "M":
                    ans += 1
"""