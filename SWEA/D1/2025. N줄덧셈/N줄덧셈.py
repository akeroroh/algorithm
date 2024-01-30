T = 1
for test_case in range(1, T + 1):
    num = int(input())
    result = 0
    for i in range(num+1):
        result += i
    print(result)