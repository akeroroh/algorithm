T = int(input())
for test_case in range(1, T+1):
    C = int(input())

    result = []

    result.append(C//25)
    C -= C//25*25
    result.append(C//10)
    C -= C//10*10
    result.append(C//5)
    C -= C//5*5
    result.append(C//1)

    print(*result)