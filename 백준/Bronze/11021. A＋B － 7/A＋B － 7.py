T = int(input())
for test_case in range(1, T+1):
    A, B = list(map(int, input().split()))
    print(f'Case #{test_case}: {A+B}')