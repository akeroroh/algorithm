T = int(input())
for test_case in range(1, T + 1):
    N, K = list(map(int, input().split()))
    score_list = [list(map(int, input().split())) for _ in range(N)]

    all_score_list = []
    for i in range(N):
        score = 0
        score += 0.35 * score_list[i][0]
        score += 0.45 * score_list[i][1]
        score += 0.2 * score_list[i][2]
        all_score_list.append(score)

    score_dict = {0: "D0", 1: "C-", 2: "C0", 3: "C+", 4: "B-", 5: "B0", 6: "B+", 7: "A-", 8: "A0", 9: "A+", 10: "A+"}

    sor_all_score_list = sorted(all_score_list)

    key_score = sor_all_score_list.index(all_score_list[K-1])
    final_key = key_score//(N/10)


    print(f'#{test_case} {score_dict[final_key]}')