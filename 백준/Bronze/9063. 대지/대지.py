N = int(input())
x_lst = []
y_lst = []
for i in range(N):
    x, y = list(map(int, input().split()))
    x_lst.append(x)
    y_lst.append(y)

garo = max(x_lst)-min(x_lst)
sero = max(y_lst)-min(y_lst)

print(garo*sero)