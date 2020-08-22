N = int(input())
arr = []
for i in range(N) :
    ticket = [str(x) for x in input().split()]
    arr.append(ticket)


start = "ICN"
answer = ["ICN"]

def find_route(arr,now,answer) :
    if len(arr) == 1 :
        answer.append(arr[0][1])
        return answer, arr
    start_point = []
    for i in range(len(arr)) : start_point.append(arr[i][0])
    if now not in start_point : return answer, arr
    next = []
    for i in range(len(arr)) :
        if arr[i][0] == now :
            next.append([arr[i][1], i])
    next = sorted(next)
    for i in next :
        now = i[0]
        pops = arr.pop(i[1])
        answer.append(now)
        answer, arr = find_route(arr, now, answer)
        if len(arr) == 1 :
            return answer, arr
        arr.insert(i[1], pops)
        answer.pop()
    return answer, arr
        
answer, arr = find_route(arr, start, answer)
print(answer)
        
    
    
