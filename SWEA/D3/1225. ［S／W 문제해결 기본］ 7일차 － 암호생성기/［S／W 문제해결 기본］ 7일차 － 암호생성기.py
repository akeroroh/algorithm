from collections import deque

T = 10
for test_case in range(1, T+1):
    tc = int(input())
    q = deque(map(int, input().split()))

    minus_num = 1
    while q[-1] != 0:
        a = q.popleft()
        b = a - minus_num
        minus_num += 1
        if minus_num == 6:
            minus_num = 1
        if b <= 0:
            b = 0
            q.append(b)
            break
        q.append(b)

    print(f'#{test_case}', end=' ')
    print(*q)