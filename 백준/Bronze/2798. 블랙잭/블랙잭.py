N, M = list(map(int, input().split()))
arr = list(map(int, input().split()))

max_result = 0
result = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for p in range(j+1, N):
            if arr[i]+arr[j]+arr[p] >= max_result and arr[i]+arr[j]+arr[p] <= M:
                max_result = arr[i]+arr[j]+arr[p]

print(max_result)