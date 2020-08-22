begin = str(input())
target = str(input())
words = [str(x) for x in input().split()]

def check(begin, target) :
    check_count = 0
    for i in range(len(target)) :
        if begin[i] != target[i] :
            check_count += 1
    if check_count == 1 :
        return True
    return False

def solution(now, targt, words, final_result=1000000, result=0) :
    if now == targt :
        return result
    for i in words :
        if i != now :
            if check(now, i) :
                index = words.index(i)
                del words[index]
                result = solution(i, targt, words) + 1
                final_result = min(result, final_result)
                words.insert(index,i) 
    return final_result

result = 0
final_result = 10000000
if target not in words :
    print(result)
else :
    result = solution(begin, target, words)
    print(result)
