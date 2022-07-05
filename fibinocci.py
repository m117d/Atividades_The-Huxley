while True:
    A = int(input('\n'))

    if A ==0:
        break
    a1=0
    a2=1

    if A ==1:
        print(' {}'.format(a1), end='')
    else:
        contador = 3
        print('{} {}'.format(a1, a2), end='')


        while contador <= A:
           a3 = a1+a2
           print(' {}'.format(a3), end='')
           a1 = a2
           a2 = a3
           contador += 1