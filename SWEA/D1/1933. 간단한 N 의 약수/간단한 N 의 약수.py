T = 1
for test_case in range(1, T + 1):
    num = int(input())
    num_list = []
    for i in range(1, num+1):
        if (num % i == 0):
            num_list.append(i)
    for z in num_list:
        print(z, end=' ')