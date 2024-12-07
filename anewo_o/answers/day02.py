# Day 2: Directed inner-Connexity-Congruence of lists

with open("anewo_o/inputs/day02.in", "r") as f:
    data = f.read().splitlines()

# preprocessing
n = len(data)
for i in range(n):
    data[i] = data[i].split()
    m = len(data[i])
    for j in range(m):
        data[i][j] = int(data[i][j])


ans = 0

# Part 1

"""
for i in range(n):
    m = len(data[i])
    for j in range(m-1):
        _ = True
        diff = data[i][j] - data[i][j+1]
        if diff >= -3 and diff <= -1 and (_ == 1 or _):
            _ = 1
        elif diff <= 3 and diff >= 1 and (_ == -1 or _):
            _ = -1
        else :
            _ = False
            break
    if _ == 1 or _ == -1:
        ans += 1
"""


safe = [0]*n

# The levels are either all increasing or all decreasing
for i in range(n):
    m = len(data[i])-1
    if all(data[i][j] < data[i][j+1] for j in range(m)) \
    or all(data[i][j] > data[i][j+1] for j in range(m)):  
        # Any two adjacent levels differ by at least one and at most three.
        if all(1 <= abs(data[i][j] - data[i][j+1]) <= 3 for j in range(m)):
            ans += 1
            safe[i] = 1

print("Answer 1: ", ans)


# Part 2

for i in range(n):
    m = len(data[i])
    if safe[i] == 0:
        for j in range(m-1):
            _data = data[i][:j] + data[i][j+1:]
            if all(_data[j] < _data[j+1] for j in range(m-2)) \
            or all(_data[j] > _data[j+1] for j in range(m-2)):
                if all(1 <= abs(_data[j] - _data[j+1]) <= 3 for j in range(m-2)):
                    ans += 1
        
print("Answer 2: ", ans)