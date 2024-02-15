A, B = list(input().split())
sang_A = int(A[::-1])
sang_B = int(B[::-1])
if sang_A > sang_B:
    print(sang_A)
else:
    print(sang_B)