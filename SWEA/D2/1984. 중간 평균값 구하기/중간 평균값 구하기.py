T = int(input())
for test_case in range(1, T + 1):
    num_list = list(map(int, input().split()))

    num_list.remove(max(num_list))
    num_list.remove(min(num_list))

    print(f'#{test_case} {round(sum(num_list)/len(num_list))}')