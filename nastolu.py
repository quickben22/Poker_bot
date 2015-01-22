
def sto(jacina,znak):
    stolic=jacina[2:]
    pomocni=[]
    pomocni=stolic[:]
    pomocni.sort()
    pomocni2=znak[2:]
    mjesto=-1
    a=0
    #print(pomocni)
    z=0
    if pomocni2.count(1)==5 or pomocni2.count(2)==5 or pomocni2.count(3)==5 or pomocni2.count(4)==5:
        print('5 od boje na stolu')
        z+=8
    elif pomocni2.count(1)==4 or pomocni2.count(2)==4 or pomocni2.count(3)==4 or pomocni2.count(4)==4:
        print('4 od boje na stolu')
        z+=4
    mjesto=0
    for i in range(len(pomocni)-1): #skala
        
        if (pomocni[len(pomocni)-1-i] - pomocni[len(pomocni)-2-i])==1 and pomocni[len(pomocni)-2-i]>0:
           a+=1
        else:
           a=0

        if a==3:
            mjesto=1
        if a==4:
            #print('skala dole')
            z+=2


    if pomocni.count(13)>0 and z!=2 and (z-4)!=2 and (z-8)!=2 and pomocni.count(1)>0 and pomocni.count(2)>0 and pomocni.count(3)>0 and pomocni.count(4)>0:
        print('skala na stolu dole')
        z+=2

    if mjesto:
        print ('4 od skale na stolu')
        z+=1
    
    
    return z
