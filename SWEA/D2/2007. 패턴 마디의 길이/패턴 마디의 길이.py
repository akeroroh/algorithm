T = int(input())
for test_case in range(1, T + 1):
    arr = input()

    pattern = ''
    for i in range(1,30):
        pattern = arr[:i]
        if arr[i:i+len(list(pattern))] == pattern:
            print(f'#{test_case} {len(pattern)}')
            break