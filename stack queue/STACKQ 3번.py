brige_l = int(input())
weight = int(input())

truck_weights = [int(x) for x in input().split()]

can_together = []
together_list = []

sum = 0
i = 0

while i<len(truck_weights):
    if sum+truck_weights[i] <= weight :
        can_together.append(truck_weights[i])
        sum += truck_weights[i]
        i += 1
    else :
        together_list.append(can_together)
        can_together=[]
        sum = 0

together_list.append(can_together)
print(together_list)

minus = len(together_list)-1

chain = 0

for i in range(len(together_list)-1) :
    if together_list[i][len(together_list[i])-1] + together_list[i+1][0] <= weight:
        chain += 1
    
result = 0
for i in together_list :
    result += len(i) + brige_l

result = result - minus - chain

print(result)
