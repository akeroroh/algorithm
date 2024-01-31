T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    print(f'#{test_case}')
    ans = [[] for _ in range(N)]
    for i in range(N):
        for j in range(i+1):
            if i == 0 or j == 0 or j == i:
                ans[i].append(1)
            else:
                ans[i].append(ans[i-1][j-1] + ans[i-1][j])
    for z in range(len(ans)):
        for q in ans[z]:
            print(q, end=' ')
        print()