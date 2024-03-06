N = int(input())
arr = list(map(int, input().split()))

result = N
for i in arr:
    if i == 1:
        result -= 1
    for j in range(2, i):
        if i%j == 0:
            result -= 1
            break

print(result)