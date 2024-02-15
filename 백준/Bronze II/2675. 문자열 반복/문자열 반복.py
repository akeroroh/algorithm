T = int(input())
for test_case in range(1, T+1):
    R, S = list(input().split())

    num = int(R)
    str_lst = list(S)
    result = []
    for i in range(len(str_lst)):
        result.append(str_lst[i]*num)

    print(''.join(result))