T = 1
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr_sort = sorted(arr)
    print(arr_sort[int((N-1)/2)])
