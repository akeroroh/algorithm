T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input()))
    max_p = 0
    for number in arr:  # 49679
        if max_p < arr.count(number):
            number_lst = []
            max_p = arr.count(number)
            number_lst.append(number)
        elif max_p == arr.count(number):
            max_p = arr.count(number)
            number_lst.append(number)
    print(f'#{test_case} {max(number_lst)} {max_p}')
