T = 1
for test_case in range(1, T + 1):
    num = int(input())
    for i in range(1, num+1):
        nums = str(i)
        counts = nums.count('3') + nums.count('6') + nums.count('9')
        if counts >= 1:
            print('-'*counts, end=' ')
        else:
            print(i, end=' ')