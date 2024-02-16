S = input().upper()
S_lst = list(set(S))

S_count = []
for i in S_lst:
    counts = S.count(i)
    S_count.append(counts)

if S_count.count(max(S_count)) >= 2:
    print("?")
else:
    print(S_lst[S_count.index(max(S_count))])