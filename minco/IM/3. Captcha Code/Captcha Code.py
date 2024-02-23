T = int(input())
for test_case in range(1, T+1):
    N, K = list(map(int, input().split()))
    sample = list(map(int, input().split()))
    passcode = list(map(int, input().split()))

    passcode_index = 0

    for i in range(N):
        if sample[i] == passcode[passcode_index]:
            passcode_index += 1
            if passcode_index == K:
                break

    if passcode_index < K:
        print(f'#{test_case} 0')
    else:
        print(f'#{test_case} 1')
