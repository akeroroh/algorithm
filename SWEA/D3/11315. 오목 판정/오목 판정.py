T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    omok = [list(input()) for _ in range(N)]

    result = ['NO']

    for i in range(N):
        for j in range(N-4):
            if ''.join(omok[i][j:j+5]) == 'ooooo':
                result[0] = 'YES'

    if result[0] != 'YES':
        for i in range(N):
            for j in range(N-4):
                if ''.join([omok[_][i] for _ in range(j, j+5)]) == 'ooooo':
                    result[0] = 'YES'

    if result[0] != 'YES':
        for i in range(N-4):
            for j in range(N-4):
                if ''.join([omok[i+_][j+_] for _ in range(5)]) == 'ooooo':
                    result[0] = 'YES'

    if result[0] != 'YES':
        for i in range(N-4):
            for j in range(4, N):
                if ''.join([omok[i+_][j-_] for _ in range(5)]) == 'ooooo':
                    result[0] = 'YES'

    print(f'#{test_case} {result[0]}')
