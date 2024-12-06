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

"""
    my idea:
        - define a partial order in Python
        - sort accordingly: topological sort? 
                                (ChatGPT + William Y.Feng)
"""

from collections import defaultdict
# avoid key errors when accessing or updating the in-degree of nodes


def topological_sort(update):
    """
    Credits to William Y.Feng for inspo
    - applied rules
    - in-degree
    - topo sort
    """

    # select useful rules
    applied_rules = []
    for [page1, page2] in rules:
        if page1 in update and page2 in update:
            applied_rules.append([page1, page2])
    # count the number of incoming "edges" for each node
    in_degree = defaultdict(int)
    for [page1, page2] in applied_rules:
        in_degree[page2] += 1
    
    new = []
    # topological sort
    while len(new) < len(update):
        for page in update:
            if page in new:
                continue
            if in_degree[page] <= 0:
                new.append(page)
                for [page1, page2] in applied_rules:
                    if page1 == page:
                        in_degree[page2] -= 1

    return new


mids = []
for update in updates:
    new = topological_sort(update)
    if update == new :
        continue
    mids.append(new[len(new) // 2])

print("Answer 2: ", sum(mids))
