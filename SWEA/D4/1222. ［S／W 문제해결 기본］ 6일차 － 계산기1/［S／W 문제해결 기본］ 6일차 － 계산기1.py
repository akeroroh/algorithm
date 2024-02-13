def postfix(lst):
    result =[]
    stack = []
    for str in lst:
        if str.isdigit():
            result.append(str)
        else:
            if stack:
                result.append(str)
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
            stack.append(n1 + n2)
    return stack


T = 10
for test_case in range(1, T+1):
    N = int(input())
    arr = input()

    print(f'#{test_case} {calculator((postfix(arr)))[0]}')