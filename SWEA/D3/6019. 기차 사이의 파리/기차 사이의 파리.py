T = int(input())
for test_case in range(1, T + 1):
    D, A, B, F = list(map(int, input().split()))

    result = D/(A+B)

    print(f'#{test_case} {F*result}')