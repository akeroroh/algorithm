T = int(input())
for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))
    result = ''
    if arr[0] < arr[1]:
        result = '<'
    elif arr[0] == arr[1]:
        result = '='
    else:
        result = '>'
    print(f'#{test_case} {result}')