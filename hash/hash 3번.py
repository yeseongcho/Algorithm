import collections
N = int(input())
clothes = []
for i in range(N) :
    cloth = [str(x) for x in input().split()]
    clothes.append(cloth)


dic = {}
cloths = []

for clo in clothes : cloths.append(clo[1])

dic = collections.Counter(cloths)

answer = 1

for i in dic : answer = answer*(dic[i]+1)

answer -= 1

return answer
