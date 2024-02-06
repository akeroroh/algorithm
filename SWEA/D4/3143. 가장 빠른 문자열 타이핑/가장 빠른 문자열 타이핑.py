T = int(input())
for test_case in range(1, T + 1):
    A, B = list(map(str, input().split()))

    C = A.count(B)
    result = len(A)-C*len(B)+C

    print(f'#{test_case} {result}')