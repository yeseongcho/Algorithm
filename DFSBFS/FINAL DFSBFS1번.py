# 코딩 테스트 연습 DFS/BFS 타겟 넘버문제
arr = [ int(i) for i in input().split() ]
target = int(input())
def solution(arr, target, answer, i, sums = 0) :
    # base case
    if i == len(arr) :
        sums = sum(arr)
        if (sums == target) :
            answer += 1
        return answer
    i += 1
    answer = solution(arr, target, answer, i)
    i -= 1
    arr[i] = -arr[i]
    print(arr)
    i += 1
    answer = solution(arr, target, answer, i)
    return answer
    
answer = 0; i = 0;
arr_all = []
answer = solution(arr, target, answer, i)
print(answer)

# input
# [1, 1, 1, 1, 1]
# output
# 5

