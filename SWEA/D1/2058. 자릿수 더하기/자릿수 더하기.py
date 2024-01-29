T = 1
for test_case in range(1, T + 1):
    arr = str(input())
    sum = 0
    for i in range(len(arr)):
        sum += int(arr[i])
    print(sum)