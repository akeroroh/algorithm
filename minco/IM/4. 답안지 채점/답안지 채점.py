T = int(input())
for test_case in range(1, T+1):
    N, M = list(map(int, input().split()))
    answer = list(map(int, input().split()))
    result_paper = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if answer[j] == result_paper[i][j]:
                result_paper[i][j] = 1
            else:
                result_paper[i][j] = 0

    student_score = []
    for i in range(N):
        score = result_paper[i][0]
        current_score = 1
        for j in range(1, M):
            if result_paper[i][j-1] == 1 and result_paper[i][j] == 1:
                current_score += 1
                score += current_score
            elif result_paper[i][j-1] == 0 and result_paper[i][j] == 1:
                score += 1
            elif result_paper[i][j-1] == 1 and result_paper[i][j] == 0:
                current_score = 1
        student_score.append(score)

    print(f'#{test_case} {max(student_score) - min(student_score)}')