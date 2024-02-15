N, M = list(map(int, input().split()))
ball = [list(map(int, input().split())) for _ in range(M)]

basket = [0]*N
for i in range(N):
    basket[i] = i+1

for j in range(M):
    basket[ball[j][0]-1], basket[ball[j][1]-1] = basket[ball[j][1]-1], basket[ball[j][0]-1]

print(*basket)