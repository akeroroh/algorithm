N = int(input())

sub_result = 2
for i in range(N):
    sub_result += 2**i

print(sub_result**2)