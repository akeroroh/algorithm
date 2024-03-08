gak1 = int(input())
gak2 = int(input())
gak3 = int(input())

if gak1 == gak2 == gak3 == 60:
    print('Equilateral')
elif gak1+gak2+gak3==180 and (gak1==gak2 or gak1==gak3 or gak2==gak3):
    print('Isosceles')
elif gak1+gak2+gak3==180 and gak1!=gak2!=gak3:
    print('Scalene')
else:
    print("Error")