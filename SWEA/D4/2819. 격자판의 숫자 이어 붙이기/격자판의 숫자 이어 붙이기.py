def dfs(row, col, cnt, sub_result):
    global result, result_lst

    if cnt == 7:
        if sub_result not in result_lst:
            result_lst.append(sub_result)
            result += 1
        return

    for di in direct:
        nrow = row + di[0]
        ncol = col + di[1]
        if 0 <= nrow < 4 and 0 <= ncol < 4:
            dfs(nrow, ncol, cnt+1, sub_result+10**cnt*table[nrow][ncol])

T = int(input())
for test_case in range(1, T+1):
    table = [list(map(int, input().split())) for _ in range(4)]

    direct = (0, 1), (1, 0), (-1, 0), (0, -1)
    result_lst = []
    result = 0

    for i in range(4):
        for j in range(4):
            dfs(i, j, 0, 0)

    print(f'#{test_case} {result}')