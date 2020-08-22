N = int(input())
triangle = []

for i in range(N) :
    flo = [int(x) for x in input().split()]
    triangle.append(flo)

def depth_search(now, i, nxt,sum, memo={}) :
    if (now, i) in memo :
        return memo[(now, i)]
    if nxt == len(triangle) :
        return sum
    sum1 = sum + triangle[nxt][i]
    sum2 = sum + triangle[nxt][i+1]
    sum1 = depth_search(nxt, i, nxt+1,sum1)
    sum2 = depth_search(nxt, i+1, nxt+1,sum2)
    result = max(sum1, sum2)
    if result == sum1 :
        memo[(now, i)] = result
    else :
        memo[(now, i+1)] = result
    return result
   
sum = triangle[0][0]
results = depth_search(0,0,1,sum)
print(results)

