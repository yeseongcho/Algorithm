import heapq as hp

scovile = [int(x) for x in input().split()]

K = int(input())

count = 0
hp.heapify(scovile)

while(scovile[0] < K and len(scovile)>=2) :
    mins = hp.heappop(scovile) # 가장 작은 항목
    sub_mins = hp.heappop(scovile) # 두번째 작은 항목
    new = mins+sub_mins*2
    hp.heappush(scovile, new) # 새로운 스코빌 지수 추가
    answer += 1
## K 이상을 만들 수 없는 경우
if scovile[len(scovile)-1] < K :
    count = -1

print(count)

