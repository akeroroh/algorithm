import sys

N = int(sys.stdin.readline())
result = N
for i in range(N):
    str_lst = sys.stdin.readline()
    for j in range(len(str_lst)-1):
        if str_lst[j] == str_lst[j+1]:
            continue
        elif str_lst[j] in str_lst[j+1:]:
            result -= 1
            break
print(result)