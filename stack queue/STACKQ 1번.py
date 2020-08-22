prices = [int(x) for x in input().split()]

answer = []

accum = 0

for i in range(len(prices)-1) :
    for j in range(i+1, len(prices)) :
        accum += 1
        if prices[i] > prices[j] :
            break
    answer.append(accum)
    accum = 0

answer.append(0)

print(answer)
