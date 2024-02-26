def change(x):
    global switch
    switch[x] = abs(switch[x] - 1)


n = int(input())
switch = [0] + list(map(int, input().split()))

for _ in range(int(input())):
    gender, no = map(int, input().split())
    i = 1
    if gender == 1:
        while no * i <= n:
            change(no * i)
            i += 1
    elif gender == 2:
        change(no)
        while 1 <= no - i and no + i <= n and switch[no - i] == switch[no + i]:
            change(no - i)
            change(no + i)
            i += 1

for i in range(1, len(switch), 10):
    print(*switch[i:i + 10])