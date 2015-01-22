
def liste(a,b):
    c=[]
    c=a[:]
    d=[]
    d=b[:]
    e=[]
    for i in range(len(c)):
        e.append(abs(c[i]-d[i]))

    return e
