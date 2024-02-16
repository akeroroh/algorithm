S = input()

result = 0

if S.count('dz=') >= 1:
    result += S.count('dz=')
    S = S.replace('dz=', '000')

cloatia_str = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
for i in cloatia_str:
    if S.count(i) >= 1:
        result += S.count(i)
        S = S.replace(i, '00')

result += len(S) - S.count('0')

print(result)