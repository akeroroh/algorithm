T = int(input())
for test_case in range(1, T + 1):
    arr = list(input())

    mirror_dic = {'q': 'p', 'p': 'q', 'b': 'd', 'd': 'b'}

    reversed_arr = arr[::-1]
    result = ''
    for i in reversed_arr:
        result += mirror_dic[i]

    print(f'#{test_case} {result}')