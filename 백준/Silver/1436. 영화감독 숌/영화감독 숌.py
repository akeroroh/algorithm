N = int(input())

result = []
start_num = '666'
while len(result) < N :
    for i in range(0, len(start_num)-2):
        if start_num[i] == start_num[i+1] == start_num[i+2] == '6':
            result.append(start_num)
            break
    start_num = str(int(start_num) + 1)

print(result[-1])