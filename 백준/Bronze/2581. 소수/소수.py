M = int(input())
N = int(input())

result_list = []
for i in range(M, N+1):
    cnt = 0
    for j in range(1, i+1):
        if i%j == 0:
            cnt += 1
    if cnt == 2:
        result_list.append(i)
if result_list:
    print(sum(result_list))
    print(result_list[0])
else:
    print(-1)