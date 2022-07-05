A = []
n = int(input())
for i in range(n):
    s = float(input())
    A.append(s)
print(' '.join('{:.3f}'.format(f) for f in A))