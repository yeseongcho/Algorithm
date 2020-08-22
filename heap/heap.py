scovile = [int(x) for x in input().split()]

K = int(input())

count = 0
while(min(scovile) < K ) :
    mins = min(scovile)
    scovile.pop(scovile.index(mins))
    sub_mins = min(scovile)
    scovile.pop(scovile.index(sub_mins))
    new = mins+sub_mins*2
    scovile.append(new)
    if len(scovile) == 1 :
        break
    count += 1

if max(scovile) < K :
    count = -1

print(count)
