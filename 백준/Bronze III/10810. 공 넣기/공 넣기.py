N, M = list(map(int, input().split()))
ball = [list(map(int, input().split())) for _ in range(M)]

basket = [0]*N

for i in range(M):
    for j in range(ball[i][0], ball[i][1]+1):
        basket[j-1] = ball[i][2]

print(*basket)