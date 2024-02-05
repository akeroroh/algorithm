T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(str, input().split())) for _ in range(N)]
    alpha_list = [arr[_][0] for _ in range(N)]
    num_list = [arr[_][1] for _ in range(N)]

    alphanum_list = [arr[_][0]*int(arr[_][1]) for _ in range(N)]
    alphanum_final = ''.join(alphanum_list)

    result = [alphanum_final[i:i+10] for i in range(0, len(alphanum_final), 10)]

    print(f'#{test_case}')
    for i in result:
        print(i)