T = int(input())
for test_case in range(1, T+1):
    N, K = list(map(int, input().split()))
    maps1 = [list(map(int, input().split()))+[0] for _ in range(N)]
    maps1.append([0]*(N+1))

    result = 0
    for i in range(N):
        score = 1
        for j in range(1, N+1):
            if maps1[i][j-1] >= 1 and maps1[i][j] == 1:
                score += 1
            elif maps1[i][j-1] >= 1 and maps1[i][j] == 0:
                if score == K:
                    result += 1
                score = 1

    for i in range(N+1):
        score = 1
        for j in range(1, N+1):
            if maps1[j-1][i] >= 1 and maps1[j][i] == 1:
                score += 1
            elif maps1[j-1][i] >= 1 and maps1[j][i] == 0:
                if score == K:
                    result += 1
                score = 1

    print(f'#{test_case} {result}')