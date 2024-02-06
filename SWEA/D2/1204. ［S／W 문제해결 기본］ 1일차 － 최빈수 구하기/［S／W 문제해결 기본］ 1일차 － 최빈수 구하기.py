T = int(input())
for test_case in range(1, T + 1):
    tc = int(input())
    score_list = list(map(int, input().split()))

    counts = [0] * 101

    for i in score_list:
        counts[i] += 1

    max_score = max(counts)
    max_list = [i for i, v in enumerate(counts) if v == max_score]
    result = max(max_list)

    print(f'#{test_case} {result}')