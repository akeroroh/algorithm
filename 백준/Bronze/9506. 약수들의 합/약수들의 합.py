while True:
    n = int(input())
    if n == -1:
        break
    sum_num = []
    for i in range(1, n):
        if n%i == 0:
            sum_num.append(i)
    if sum(sum_num) == n:
        print(f'{n} = ', end='')
        for j in sum_num:
            print(f'{j}', end='')
            if j != sum_num[-1]:
                print(' + ', end='')
        print()
    else:
        print(f'{n} is NOT perfect.')