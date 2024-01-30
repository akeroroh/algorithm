T = 1
for test_case in range(1, T + 1):
    rsp = list(map(int, input().split()))
    A = rsp[0]
    B = rsp[1]
    if (A == 1 and B == 3) or (A == 2 and B == 1) or (A == 3 and B == 2):
        print("A")
    else:
        print("B")