T = int(input())
for test_case in range(1, T + 1):
    palindrome = str(input())
    result = 0
    reverse_palindrome = palindrome[::-1]
    if reverse_palindrome == palindrome:
        result = 1
    print(f'#{test_case} {result}')