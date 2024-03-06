import sys

N, K = list(map(int, sys.stdin.readline().split()))

result_lst = []
for i in range(1, N+1):
    if N % i == 0:
        result_lst.append(i)
    if len(result_lst) == K:
        break

if len(result_lst) < K:
    print(0)
else:
    print(result_lst[K-1])