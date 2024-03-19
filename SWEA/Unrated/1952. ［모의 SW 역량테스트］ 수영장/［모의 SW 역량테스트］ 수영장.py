def dfs(d, sum):
    global result

    if sum >= result:
        return
    if d >= 12:
        result = min(sum, result)
        return

    dfs(d+1, sum+plan[d]*price_lst[0])
    dfs(d+1, sum+price_lst[1])
    dfs(d+3, sum+price_lst[2])

T = int(input())
for test_case in range(1, T+1):
    price_lst = list(map(int, input().split()))
    plan = list(map(int, input().split()))

    result = price_lst[3]
    dfs(0, 0)

    print(f'#{test_case} {result}')