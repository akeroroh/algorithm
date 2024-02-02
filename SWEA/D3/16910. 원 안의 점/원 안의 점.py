T = int(input())
for test_case in range(1, T + 1):
    num = int(input())

    num_count = 0
    for i in range(-num, num+1):
        for j in range(-num, num+1):
            if i**2 + j**2 <= num**2:
                num_count += 1

    print(f'#{test_case} {num_count}')