T = int(input())
for test_case in range(1, T+1):
    x1_1, y1_1, x2_1, y2_1 = list(map(int, input().split()))
    x1_2, y1_2, x2_2, y2_2 = list(map(int, input().split()))

    squ1_lst = [[x1_1, y1_1], [x2_1, y1_1], [x1_1, y2_1], [x2_1, y2_1]]
    squ2_lst = [[x1_2, y1_2], [x2_2, y1_2], [x1_2, y2_2], [x2_2, y2_2]]

    result = 4
    for i in squ2_lst:
        if x1_1 < i[0] < x2_1 and y1_1 < i[1] < y2_1:
            result = 1
        elif x1_1 < i[0] < x2_1 and (y1_1 == i[1] or y2_1 == i[1]):
            result = 2
        elif (x1_1 == i[0] or x2_1 == i[0]) and y1_1 < i[1] < y2_1:
            result = 2
        elif i in squ1_lst:
            result = 3

    print(f'#{test_case} {result}')