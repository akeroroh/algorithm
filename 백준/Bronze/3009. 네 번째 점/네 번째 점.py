x1, y1 = list(map(int, input().split()))
x2, y2 = list(map(int, input().split()))
x3, y3 = list(map(int, input().split()))

x_lst = x1, x2, x3
y_lst = y1, y2, y3

result_x = []
result_y = []
for i in x_lst:
    if x_lst.count(i) == 1:
        result_x.append(i)
for i in y_lst:
    if y_lst.count(i) == 1:
        result_y.append(i)

print(f'{result_x[0]} {result_y[0]}')