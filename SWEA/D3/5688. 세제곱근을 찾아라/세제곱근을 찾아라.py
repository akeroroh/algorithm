def three(n):
    low = 0
    high = n

    while low <= high:
        mid = (low+high)//2
        number = mid**3

        if number == n:
            return mid
            break
        elif number < n:
            low = mid + 1
        else:
            high = mid -1

    return -1

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    print(f'#{test_case} {three(N)}')