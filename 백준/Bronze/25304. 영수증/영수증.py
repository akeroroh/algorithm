X = int(input())
N = int(input())
price = [list(map(int, input().split())) for _ in range(N)]

sum_price = 0
for i in range(N):
    sum_price += price[i][0] * price[i][1]

if sum_price == X:
    print("Yes")
else:
    print("No")