T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    arr.sort(key=lambda x:x[1])

    cnt = 0
    end_point = 0
    for i in range(N):
        s, e = arr[i]
        if end_point <= s:
            end_point = e
            cnt += 1
    print(f'#{test_case} {cnt}')