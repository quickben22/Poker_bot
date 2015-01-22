

def koja(jacina,znak,broj):
    pomoc=[]
    stol=[]
    stol2=[]
    pomoc4=[]
    for i in range(13):
        if jacina.count(i+1)>1: # 2 ili vise od 1 vrste
            pomoc.append(jacina.count(i+1))
            pomoc4.append(i+1) # koja karta se uparila ,utrisila i sl. 1=dvojka, 13=as
        stol=jacina[2:]
        if stol.count(i+1)>1:
            stol2.append(stol.count(i+1))

    pomoc3=[]
    pomoc3=jacina[:]
    pomoc3.sort()
    b=0
    
    for i in range(4):
        if znak.count(i+1)>4:
            if len(pomoc)>=1: # ima parova ili trisova na stolu
                for i in range(len(pomoc4)): #tko se tocno upario, 2,3...as
                    while(1): #sad ce otkrit skalu i ako je tris dole ili u mene
                        pomoc3.remove(pomoc4[i])
                        if pomoc3.count(pomoc4[i])==1:
                            break
                        
            for i in range(len(pomoc3)-1):
                if b==4:
                    return 8 #skala u boji
                elif jacina.count(13)>0 and jacina.count(1)>0 and jacina.count(2)>0 and jacina.count(3)>0 and jacina.count(4)>0:
                    return 8 #skala u boji
                elif (pomoc3[len(pomoc3)-1-i] - pomoc3[len(pomoc3)-2-i])==1 and pomoc3[len(pomoc3)-2-i]>0:
                   b+=1
                else:
                   b=0
    

    for i in range(len(pomoc)):
        if pomoc[i]==4:
            #print('poker')
            return 7

    for i in range(4):
        if znak.count(i+1)>4:
            return 5 #boja

    pomoc2=[]
    pomoc2=jacina[:]
    pomoc2.sort()
    a=0
    if len(pomoc)>=1: # ima parova ili trisova na stolu
        for i in range(len(pomoc4)): #tko se tocno upario, 2,3...as
            while(1):
                pomoc2.remove(pomoc4[i]) #ako je tris dole, nece skalu otkrit, ali tako je i bolje,jer je lako moguc full
                
                if pomoc2.count(pomoc4[i])==1:
                    break
                
    #print(pomoc2) #za otkrivanje karte, pomocna lista
    #print(pomoc4) #koja se karta uparila
    mjesto=-1
    for i in range(len(pomoc2)-1): #skala
        
        if (pomoc2[len(pomoc2)-1-i] - pomoc2[len(pomoc2)-2-i])==1 and pomoc2[len(pomoc2)-2-i]>0:
           a+=1
        else:
           a=0

        if a==3:
            mjesto=len(pomoc2)-2-i
        if a==4:
            return 4

    #print (mjesto)
    if jacina.count(13)>0 and jacina.count(1)>0 and jacina.count(2)>0 and jacina.count(3)>0 and jacina.count(4)>0:
        return 4 #skala
    
    if len(pomoc)==2:
        if sum(pomoc)==4:
            if len(stol2)==2:
                return 0 #2 para na stolu, dakle nemam nista
            else:
                return 2 #2 para
        else:
            return 6 #full

    if len(pomoc)>2:
        if sum(pomoc)==6:
            return 1 #3 para, ko da imam 1 par
        else:
            return 6 #full

   
        
    if len(pomoc)==1:
        if pomoc[0]==2:
            if len(stol2)==1:
                if mjesto==-1:
                    return 0 #par na stolu
            else:
                return 1 #par
            
        elif pomoc[0]==3:
            if len(stol2)==1:
                if stol2[0]==3:
                    return 0 #tris na stolu
                else:
                    return 3
            else:
                return 3 #tris
    #print(pomoc)
    #print(stol2)
    if mjesto>-1 and pomoc2[mjesto:(mjesto+4)].count(jacina[0])>0 and pomoc2[mjesto:(mjesto+4)].count(jacina[1])>0 and pomoc2[mjesto:(mjesto+4)].count(13)==0 and jacina[0]<13 and jacina[1]<13:
        return -1 # 4 od skale imam
    return 0
    
  
    
