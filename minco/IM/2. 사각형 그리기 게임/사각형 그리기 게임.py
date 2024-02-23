T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    maps = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    max_squ = 0

    for i in range(N):
        for j in range(N):
            current = maps[i][j]
            for p in range(i, N):
                for q in range(j, N):
                    if maps[p][q] == current:
                        area = (p-i+1)*(q-j+1)
                        if area > max_squ:
                            max_squ = area
                            result = 1
                        elif area == max_squ:
                            result += 1

    print(f'#{test_case} {result}')