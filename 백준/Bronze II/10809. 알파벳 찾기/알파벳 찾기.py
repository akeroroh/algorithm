S = input()

alpha_lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

result = []
for i in range(len(alpha_lst)):
    if alpha_lst[i] in S:
        result.append(S.index(alpha_lst[i]))
    else:
        result.append(-1)

print(*result)