def num_sort(arr, cnt):
    global result

    if cnt == circle_num:
        bigyo_num = int(''.join(map(str, arr)))
        result = max(result, bigyo_num)
        return

    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
                arr[i], arr[j] = arr[j], arr[i]

                check_num = int(''.join(map(str, arr)))
                if (cnt, check_num) not in visited:
                    num_sort(arr, cnt+1)
                    visited.append((cnt, check_num))
                
                arr[i], arr[j] = arr[j], arr[i]


T = int(input())
for test_case in range(1, T+1):
    nums, circle_num = list(map(int, input().split()))
    numbers = list(map(int, str(nums)))

    result = 0
    visited = []
    num_sort(numbers, 0)

    print(f'#{test_case} {result}')