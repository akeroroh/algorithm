T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    string_lst = list(input().split())

    result = []
    if N % 2 == 0:
        suffel1 = string_lst[:N//2]
        suffel2 = string_lst[N//2:]
        for i in range(N):
            if suffel2:
                result.append(suffel2.pop())
            if suffel1:
                result.append(suffel1.pop())
    else:
        suffel1 = string_lst[:N//2+1]
        suffel2 = string_lst[N//2+1:]
        for i in range(N):
            if suffel1:
                result.append(suffel1.pop())
            if suffel2:
                result.append(suffel2.pop())

    print(f'#{test_case}', end=' ')
    print(*list(reversed(result)))
