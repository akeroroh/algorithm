from collections import deque

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs():
    global q

    while q:
        temp = []
        while q:
            x, y = q.pop()
            for i, j in move:
                dx = x+i
                dy = y+j
                if 0 <= dx < 100 and 0 <= dy < 100:
                    if not maps[dx][dy]:
                        maps[dx][dy] = 1
                        temp.append((dx, dy))
                    if maps[dx][dy] == 3:
                        return 1
        q = temp
    return 0

T = 10
for test_case in range(1, T + 1):
    tc = int(input())
    maps = [list(map(int, input().strip())) for _ in range(100)]

    q = deque()
    q.extend([(1, 1)])

    print(f'#{test_case} {bfs()}')