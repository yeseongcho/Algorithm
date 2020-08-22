priorities = [int(x) for x in input().split()]

location = int(input())

documents = [int(i) for i in range(len(priorities))]

i = 0

lists = []
while True :
    if priorities[i] == max(priorities) :
        doc = documents.pop(0)
        pri = priorities.pop(0)
        lists.append(doc)
        if priorities == [] : break
    else :
        doc = documents.pop(0)
        documents.append(doc)
        pri = priorities.pop(0)
        priorities.append(pri)

results = lists.index(location) + 1
print(results)


