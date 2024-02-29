def get_number(cnt, sum):
    global result
    if sum == K:
        result += 1
        return
    if cnt == N:
        return
    get_number(cnt+1, sum+arr[cnt])
    get_number(cnt+1, sum)

T = int(input())
for test_case in range(1, T+1):
    N, K = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    result = 0
    get_number(0, 0)

    print(f'#{test_case} {result}')