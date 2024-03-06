import sys
A, B, V = list(map(int, sys.stdin.readline().split()))

result = 0
if A >= V:
    result = 1
elif (V-A)%(A-B)==0:
    result = (V-A)//(A-B) + 1
else:
    result = (V-A)//(A-B) + 2

print(result)