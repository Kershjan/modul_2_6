from random import randint

comb = list()
v1 = randint(3,20)
v2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for i in v2:
    for j in range(i+1, v1):
        n1 = i + j
        if v1 % n1 == 0:
            comb.append(i)
            comb.append(j)

print(v1)
print(*comb)
