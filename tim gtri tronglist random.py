from random import sample, randint
A=sample(range(100), 100)
a=randint(0,100)
A.sort()
if a in A:
    print(a,' có trong mảng')
    print('Vị trí của ',a,'là: ',A.index(a))
