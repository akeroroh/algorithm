A, B = list(map(int, input().split()))
C = int(input())

cook_hour = C // 60
cook_minute = C % 60
oven_minute = B + cook_minute
oven_hour = A + cook_hour
if oven_minute >= 60:
    oven_hour += 1
    oven_minute -= 60
if oven_hour >= 24:
    oven_hour -= 24

print(f'{oven_hour} {oven_minute}')