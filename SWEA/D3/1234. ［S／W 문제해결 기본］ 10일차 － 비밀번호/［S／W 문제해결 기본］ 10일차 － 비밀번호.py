T = 10
for test_case in range(1, T + 1):
    N, password = input().split()

    stack = []
    for i in password:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)

    result = ''.join(stack)

    print(f'#{test_case} {result}')