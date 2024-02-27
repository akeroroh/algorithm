T = int(input())
for test_case in range(1, T+1):
    N, T = list(map(int, input().split()))
    card_lst = [1+i for i in range(N)]

    for _ in range(T):
        # if N % 3 == 0:
        #     pick_card = card_lst[:N//3*2]
        #     for i in range(len(pick_card)):
        #         card_lst.pop(0)
        #         card_lst.append(pick_card[i])
        # elif N % 3 == 2:
        #     pick_card = card_lst[-(N // 3):]
        #     for i in range(len(pick_card)):
        #         card_lst.pop(-1)
        #         card_lst.insert(0, pick_card[i])
        # else:
        #     pick_card = card_lst[-(N // 3)-1:]
        #     for i in range(len(pick_card)):
        #         card_lst.pop(-1)
        #         card_lst.insert(0, pick_card[i])

        bottom_cards = card_lst[-(N // 3):]  # 하위 37%의 카드 선택
        card_lst = bottom_cards + card_lst[:-(N // 3)]

        result = [''] * len(card_lst)
        # 홀수 장
        if N % 2:
            for i in range(N // 2 + 1):
                result[2 * i] = card_lst[i]
            for i in range(N // 2):
                result[2 * i + 1] = card_lst[i + N // 2 + 1]
        # 짝수 장
        else:
            for i in range(N // 2):
                result[2 * i] = card_lst[i]
                result[2 * i + 1] = card_lst[i + N // 2]
        card_lst = result

    print(f'#{test_case}', end=' ')
    print(*card_lst)