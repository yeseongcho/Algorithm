progresses = [int(x) for x in input().split()]

speeds = [int(x) for x in input().split()]

answer = []

result = []

accum = 1

for i in range(len(progresses)) :
    lim = 100 - progresses[i]
    get = 0
    while True :
        get += 1
        if get*speeds[i] >= lim :
            break
    result.append(get)

Max = result[0]

for i in range(1, len(result)) :
    if Max < result[i] :
        answer.append(accum)
        accum = 1
        if i != len(result)-1 :
            Max = result[i]
    else :
        accum += 1
        if i == len(result)-1 :
            answer.append(accum)

if Max < result[len(result)-1] :
    answer.append(1)

print(answer)
    
