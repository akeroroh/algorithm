def postfix(lst):
    result = []
    stack = []

    isp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}
    icp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 3}

    for str in lst:
        if str.isdigit():
            result.append(str)
        elif str == '(':
            stack.append(str)
        elif str == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
        else:
            if stack:
                if isp[stack[-1]] < icp[str]:
                    stack.append(str)
                else:
                    while stack and isp[stack[-1]] >= icp[str]:
                        result.append(stack.pop())
                    stack.append(str)
            else:
                stack.append(str)
    while stack:
        result += stack.pop()
    return result


def calculator(arr):
    stack = []
    for str in arr:
        if str.isdigit():
            stack.append(int(str))
        else:
            n2 = stack.pop()
            n1 = stack.pop()
            if str == '+':
                stack.append(n1 + n2)
            elif str == '*':
                stack.append(n1 * n2)
            elif str == '-':
                stack.append(n1 - n2)
            else:
                stack.append(n1 / n2)
    return stack


T = 10
for test_case in range(1, T + 1):
    N = int(input())
    arr = input()
    print(f'#{test_case} {calculator((postfix(arr)))[0]}')