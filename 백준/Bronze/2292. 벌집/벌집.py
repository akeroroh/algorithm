N = int(input())

result = 1
cnt = 1
cnt2 = 1
while N - cnt > 0:
    cnt += 6*cnt2
    cnt2 += 1
    result += 1

print(result)