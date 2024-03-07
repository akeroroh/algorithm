N = int(input())

if N == 1:
    print()
else:
    result = []
    cnt = 2
    while N > 1:
        if N % cnt == 0:
            result.append(cnt)
            N /= cnt
        else:
            cnt += 1
    for i in result:
        print(i)