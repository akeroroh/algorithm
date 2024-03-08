a, b, c = list(map(int, input().split()))

byeon_lst = [a, b, c]
byeon_lst.sort()

while byeon_lst[2] >= (byeon_lst[0] + byeon_lst[1]):
    byeon_lst[2] -= 1

print(sum(byeon_lst))