student = [int(input()) for _ in range(28)]

box = [0] * 30
for i in student:
    box[i-1] = 1

num_lst = []
for j in range(30):
    if box[j] == 0:
        num_lst.append(j+1)

print(num_lst[0])
print(num_lst[1])