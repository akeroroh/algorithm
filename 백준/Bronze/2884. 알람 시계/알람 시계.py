H, M = list(map(int, input().split()))

alarm_M = M - 45
if alarm_M < 0:
    alarm_M = 60 - abs(alarm_M)
    H -= 1
if H < 0:
    H = 24 - abs(H)
    
print(f'{H} {alarm_M}')