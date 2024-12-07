# Day 3 : Parsing


ans = 0

# Part 1
"""
Building a lexer for "mul(XXX,XXX)" where XXX is a number

with open("day3.txt", "r") as f:
    data = list(f.read())

buff = ""
for ch in data :
    #print(ch, " and ", buff)
    if ch == "m" :
        buff = ch
    elif buff == "m" and ch == "u" :
        buff += ch
    elif buff == "mu" and ch == "l" :
        buff += ch
    elif buff == "mul" and ch == "(" :
        buff += ch
    elif buff == "mul(" and ch.isdigit() :
        buff += ch
    elif 4 < len(buff) < 7 \
        and buff[:4] == "mul(" and buff[4:].isdigit() \
        and ch.isdigit :
        buff += ch
    elif 4 < len(buff) <= 7 \
        and buff[:4] == "mul(" and buff[4:].isdigit() \
        and ch == "," :
        buff += ch
    elif 5 < len(buff) < 9 \
        and buff[:4] == "mul(" and buff[-1] == "," \
        and ch.isdigit() :
        buff += ch
    elif 5 < len(buff) < 11 \
        and ch.isdigit() :
        buff += ch
    elif len(buff) <= 11 \
        and ch == ")" :
        print(buff)
        for i in range(4, len(buff)):
            if buff[i] == ",":
                a = int(buff[4:i])
                b = int(buff[i+1:])
                print(a*b)
                ans += a*b
                break
    else :
        buff = ""

or use a regex...

Should work but answer is too high ?
"""

import re

with open("anewo_o/inputs/day03.in", "r") as f:
    data = f.read()

# Regex pattern to match "mul(XXX,XXX)" where XXX is a number
pattern = re.compile(r"mul\(\d{1,3},\d{1,3}\)")
matches = pattern.findall(data)


for match in matches:
    a, b = map(int, match[4:-1].split(","))
    ans += a*b


print("Answer 1: ", ans)

ans = 0


# Part 2

pattern = re.compile(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)")
matches = pattern.findall(data)

"""
range(n) doesn't update...
n = len(matches)
for i in range(n):
    if matches[i] == "do()":
        for j in range(i,n):
            if matches[j] == "don't()":
                break
            elif matches[j] == "do()":
                del matches[j]
                n -= 1
            else :
                a, b = map(int, matches[j][4:-1].split(","))
                ans += a*b
"""

"""
i = 0
n = len(matches)
while i < n:
    if matches[i] == "do()":
        j = i+1
        while j < n:
            print(matches[j])
            if matches[j] == "don't()":
                # ignore the following
                break
            elif matches[j] == "do()":
                # ignore new do()
                del matches[j]
                n -= 1
            else : 
                # normal procedure
                a, b = map(int, matches[j][4:-1].split(","))
                ans += a*b
                j += 1
        i = j # skip past the don't()

    elif matches[i] == "don't()":
        # skip it
        k = i+1
        while k < n:
            if matches[k] == "do()":
                break
            k += 1
        i = k

    else : 
        # normal procedure
        a, b = map(int, matches[i][4:-1].split(","))
        ans += a*b
    i += 1
"""

i = 0
n = len(matches)
while i < n:
    if matches[i] == "do()":
        # multiply until don't()
        j = i+1
        while j < n:
            if matches[j] == "don't()":
                break
            elif matches[j] == "do()":
                j += 1
            else :
                a, b = map(int, matches[j][4:-1].split(","))
                ans += a*b
                j += 1
        i = j
    elif matches[i] == "don't()":
        # ignrore until do()
        k = i+1
        while k < n:
            if matches[k] == "do()":
                break
            k += 1
        i = k
    else :
        a, b = map(int, matches[i][4:-1].split(","))
        ans += a*b
        i += 1


print("Answer 2: ", ans)
