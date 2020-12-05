n=int(input('n='))
for i in range(2,n+1):
    s,t=0,[]
    for j in range(1,i):
        if i%j==0:
            s+=j
            t+=[str(j)]
    else:9 / 21
    if s==i:
        print('{}={}'.format(s,'+'.join(t)))