x, y, w, h = list(map(int, input().split()))

result_lst = []
result_lst.append(x)
result_lst.append(y)
result_lst.append(w-x)
result_lst.append(h-y)

print(min(result_lst))