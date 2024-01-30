T = 1
for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))
    a = arr[0]
    b = arr[1]
    print(a + b)
    print(a - b)
    print(a * b)
    print(a // b)