# Day 6: Directed Search Algorithm

with open("anewo_o/inputs/day06.in", "r") as f:
    data = [list(line) for line in f.read().splitlines()]


# Part 1

# find start
n, m = len(data), len(data[0])

for i in range(n):
    for j in range(m):
        if data[i][j] == "^":
            start = (i, j)
            break

# only horizontal and vertical moves
# sorted clockwiser from ^
dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# init
direction = 0
i, j = start


marks = set()

while True:

    dx, dy = dxy[direction][0], dxy[direction][1]

    i, j = i+dx, j+dy
    if not (0 <= i < n and 0 <= j < m) : 
        break

    if data[i][j] == "#":
        direction = (direction + 1) % 4
        i, j = i-dx, j-dy
    else :
        marks.add((i, j))

print("Answer 1:", len(marks))


# Part 2

ans = 0

"""
for x, y in marks:

    data[x][y] = "#"
    
    direction = 0
    i, j = start

    seen = set()

    while True :
        if (i, j) in seen:
            ans += 1
            break
        seen.add((i, j))
        
        dx, dy = dxy[direction][0], dxy[direction][1]

        ni, nj = i+dx, j+dy
        if not (0 <= ni < n and 0 <= nj < m) : 
            break

        if data[ni][nj] == "#":
            direction = (direction + 1) % 4
        else :
            i, j = ni, nj

    data[x][y] = "."
"""

# I'm not sure why the above code doesn't work, 
# but I found a solution that does work, credits to William Y. Feng
# https://github.com/womogenes/AoC-2024-Solutions/blob/main/day_06/p2_day_06.py

print("Answer 2:", ans)

