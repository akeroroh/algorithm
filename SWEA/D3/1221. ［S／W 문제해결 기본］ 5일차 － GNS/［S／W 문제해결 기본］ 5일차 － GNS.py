T = int(input())
for test_case in range(1, T + 1):
    test_N_arr = list(map(str, input().split()))
    N = test_N_arr[1]
    test_arr = list(map(str, input().split()))

    planet_num_dic = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}
    planet_reverse_num_dic = {v:k for k,v in planet_num_dic.items()}

    num_unsort_list = []
    for i in test_arr:
        num_unsort_list.append(planet_num_dic[i])

    num_sort_list = sorted(num_unsort_list)
    final_list = []
    for i in num_sort_list:
        final_list.append(planet_reverse_num_dic[i])

    print(f'#{test_case}')
    print(*final_list)