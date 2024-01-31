T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    maps = [[0]*10 for d in range(10)]
    for i in range(N):
        a, b, c, d, color = list(map(int, input().split()))
        for z in range(a, c+1):
            for q in range(b, d+1):
                maps[z][q] += color
    count_pup = 0
    for p in range(10):
        for w in range(10):
            if maps[p][w] == 3:
                count_pup += 1
    print(f'#{test_case} {count_pup}')