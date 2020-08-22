import heapq as hp
import math 
jobs = []

N = int(input())

for i in range(N) :
    job = [int(x) for x in input().split()]
    jobs.append(job)


jobs = sorted(jobs, key=lambda x : x[1])

print(jobs)

answer = jobs[0][1] - jobs[0][0]
accum = jobs[0][1]

for i in range(1, len(jobs)) :
    answer = answer + (accum - jobs[i][0]) + jobs[i][1]
    accum = accum + jobs[i][1]

answer = math.floor(answer/N)

print(answer)
