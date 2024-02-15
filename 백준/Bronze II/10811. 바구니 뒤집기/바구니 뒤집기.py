N, M = list(map(int, input().split()))
num_lst = [list(map(int, input().split())) for _ in range(M)]

basket = [0] * N
for i in range(1, N+1):
    basket[i-1] = i

for i in range(M):
    reversing = basket[num_lst[i][0]-1:num_lst[i][1]]
    reversing.reverse()
    basket[num_lst[i][0]-1:num_lst[i][1]] = reversing

print(*basket)