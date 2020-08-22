import collections
participants = [str(x) for x in input().split()]

completion = [str(x) for x in input().split()]

arr = participants + completion

dic = collections.Counter(arr)

for part in dic :
    if dic[part]%2 != 0 :
        answer = part
        return answer
