T = int(input())
for test_case in range(1, T + 1):
    price = int(input())

    price_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

    change_list = []
    for i in price_list:
        change = 0
        while price // i > 0:
            change += price//i
            price -= (price//i)*i
            break
        change_list.append(change)

    print(f'#{test_case}')
    for i in change_list:
        print(i, end=' ')
    print()