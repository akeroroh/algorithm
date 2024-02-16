num_lst = list(map(int, input().split()))

result1 = 0
for i in range(5):
    result1 += num_lst[i]**2

print(result1%10)