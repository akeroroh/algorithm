num_lst = [int(input()) for _ in range(10)]

na_lst = []
for i in num_lst:
    na_lst.append(i%42)

print(len(set(na_lst)))