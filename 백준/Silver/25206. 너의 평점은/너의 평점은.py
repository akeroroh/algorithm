import sys

score_dic = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}

score_lst = [list(sys.stdin.readline().split()) for _ in range(20)]

result = 0
hak_lst = []
for i in range(20):
    if score_lst[i][2] == 'P':
        continue
    hak_lst.append(float(score_lst[i][1]))
    result += float(score_lst[i][1]) * float(score_dic[score_lst[i][2]])

hak_sum = sum(hak_lst)

print(result/hak_sum)