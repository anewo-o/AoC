# Day 1: Sorted Manhattan Distance?


# Part 1

with open("anewo_o/inputs/day01.in", "r") as f:
    data = f.read().split()
    L1 = sorted([int(i) for i in data[::2]])
    L2 = sorted([int(i) for i in data[1::2]])

ans = 0

n = len(L1)
for _ in range(n) :
    ans += abs(L1[_] - L2[_])

print("Sum of sorted elements: ", ans)


# Part 2

sim = 0

occ = {}
for i in range(n) :
    if L2[i] not in occ :
        occ[L2[i]] = 1
    else :
        occ[L2[i]] += 1

for i in range(n) :
    if L1[i] in occ :
        sim += L1[i]*occ[L1[i]]

print("Similarity: ", sim)
