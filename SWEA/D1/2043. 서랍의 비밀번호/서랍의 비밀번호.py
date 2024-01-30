T = 1
for test_case in range(1, T + 1):
    num = list(map(int, input().split()))
    print(num[0] - num[1] + 1)