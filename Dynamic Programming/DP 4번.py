m = int(input())
n = int(input())
puddles = [int(x) for x in input().split()]
routes = [[1,1]]
route_list = []
distance = 0
def route_search(now,route, route_list, distance,dist1=10000,dist2=10000) :
    # 목적지 도착
    if now == [m, n] :
        return distance, route
    if now[0] + 1 <= m :
        if [now[0]+1,now[1]] != puddles :
            distance += 1
            dist1, route = route_search([now[0]+1,now[1]],route,route_list,distance)
    if now[1] +1 <= n :
        if [now[0],now[1]+1] != puddles :
            distance += 1
            dist2, route = route_search([now[0],now[1]+1],route,route_list,distance)
    distance = min(dist1, dist2)
    if distance == dist1 :
        route.append([now[0]+1,now[1]])
    elif distance == dist2 :
        route.append([now[0], now[1]+1])
    return distance, route

count, route = route_search([1,1],routes, route_list, distance)

# 최단 경로 길이
print(count-1)
results = 0
for i in route :
    if i == [m,n] : results += 1
# 최단 경로 갯수
print(results)

