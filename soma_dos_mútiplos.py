n = int(input(' '))

tres = [x for x in range(3,n,3)]
cinco = [x for x in range(5,n,5)]
quinze = [x for x in range(15,n,15)]

print(sum(tres)+sum(cinco)-sum(quinze))