DEBUG = False

with open("anewo_o/inputs/day5.txt", "r") as f:
    data = f.read().split("\n\n")
    rules = [[int(page) for page in rule.split("|")]\
              for rule in data[0].splitlines()]
    if DEBUG : print(rules[0]+"\n", rules[1]+"\n", rules[2]+"\n")
    updates = [[int(page) for page in update.split(",")]\
                for update in data[1].splitlines()]
    if DEBUG : print(updates[0]+"\n", updates[1]+"\n", updates[2]+"\n")
    

# Part 1

mids = []
respects = True
# check if each update respects the rules
for update in updates:
    # for a given page...
    for i, page1 in enumerate(update):
        # are all next pages in the rules?
        for page2 in update[i+1:]:
            if [page1, page2] not in rules: respects = False
    # if every page is so, then get the middle element
    if respects : mids.append(update[len(update) // 2])
    respects = True

print("Answer 1:", sum(mids))


# Part 2

ans = 0

###

print("Answer 2: ", ans)
