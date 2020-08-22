import heapq as hp

operation = []
N = int(input())
for i in range(N) :
    x = str(input())
    operation.append(x)
heap = []
for op in operation :
    if op[0] == "I" : hp.heappush(heap, int(op[2:])) 
    elif op == "D 1" :
        if answer == [] : continue
        hp._heapify_max(heap) 
        hp.heappop(heap)
    elif op == "D -1" :
        if answer == [] : continue
        hp.heapify(heap)
        hp.heappop(heap)
if heap == [] :
    heap = [0, 0]
    print(heap)
    print("Done")
elif len(heap) == 1 :
    min = heap[0] ; max = heap[0]
    heap = [max, min]
    print(heap)
else :
    hp.heapify(heap)
    min = hp.heappop(heap)
    hp._heapify_max(heap)
    max = hp.heappop(heap)
    heap = [max, min]
    print(heap)
