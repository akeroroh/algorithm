T = 10
for test_case in range(1, T + 1):
    tc = int(input())
    maps = [list(map(str, input())) for _ in range(100)]

    palindrome = 0
    for i in range(100):
        for j in range(100):
            for p in range(100):
                palindrome_check = []
                if j+p <= 100:
                    for q in range(p):
                        palindrome_check.append(maps[i][j+q])
                if palindrome_check == palindrome_check[::-1]:
                    if palindrome < len(palindrome_check):
                        palindrome = len(palindrome_check)

    for i in range(100):
        for j in range(100):
            for p in range(100):
                palindrome_check = []
                if j+p <= 100:
                    for q in range(p):
                        palindrome_check.append(maps[j+q][i])
                if palindrome_check == palindrome_check[::-1]:
                    if palindrome < len(palindrome_check):
                        palindrome = len(palindrome_check)

    print(f'#{test_case} {palindrome}')