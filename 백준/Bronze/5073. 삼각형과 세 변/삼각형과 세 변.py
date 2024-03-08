while True:
    N1, N2, N3 = list(map(int, input().split()))
    if N1 == 0 and N2 == 0 and N3 == 0:
        break

    N_lst = [N1, N2, N3]
    N_lst.sort()

    if N_lst[2] >= (N_lst[0] + N_lst[1]):
        print('Invalid')
    elif N1 == N2 == N3:
        print('Equilateral')
    elif N1 == N2 or N1 == N3 or N2 == N3:
        print('Isosceles')
    else:
        print('Scalene')