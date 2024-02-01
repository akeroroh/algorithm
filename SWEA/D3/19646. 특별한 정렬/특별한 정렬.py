T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    num_list = list(map(int, input().split()))

    sort_lst = sorted(num_list)

    print(f'#{test_case} {sort_lst[-1]} {sort_lst[0]} {sort_lst[-2]} {sort_lst[1]} {sort_lst[-3]} {sort_lst[2]} {sort_lst[-4]} {sort_lst[3]} {sort_lst[-5]} {sort_lst[4]}')