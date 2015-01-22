

def igraca(popis_igraca,popis_igraca2,imena_igraca,broj):
    
            #check,call,raise,fold
    vide_flop=[]
    for i in range(5):#vide flop igraci     #broj puta vidio flop   /   broj flopova
        if float(sum(popis_igraca[imena_igraca[i]][:6]))!=0 and popis_igraca[imena_igraca[i]][6]!=0 and popis_igraca[imena_igraca[i]][9]>10:
            vide_flop.append(float(sum(popis_igraca[imena_igraca[i]][:6]))/popis_igraca[imena_igraca[i]][6])
        else:
            vide_flop.append(0)
    bet_raise=[]
    check_call=[]
    fold=[]
    for i in range(5):                         #raise,bet     podijeljeno sa    (broj_krugova+doso na flop+ doso na 4 + doso na 5)                 
        broj_krugova=popis_igraca[imena_igraca[i]][9]
        if float(popis_igraca2[imena_igraca[i]][2])!=0 and (sum(popis_igraca2[imena_igraca[i]]))!=0 and popis_igraca[imena_igraca[i]][9]>10:          
            bet_raise.append(float(popis_igraca2[imena_igraca[i]][2])/(sum(popis_igraca2[imena_igraca[i]])))    
        else:
            bet_raise.append(0)
        if float(sum(popis_igraca2[imena_igraca[i]][:2])-popis_igraca2[imena_igraca[i]][0]/2)!=0 and (sum(popis_igraca2[imena_igraca[i]]))!=0 and popis_igraca[imena_igraca[i]][9]>10:
            check_call.append(float(sum(popis_igraca2[imena_igraca[i]][:2])-popis_igraca2[imena_igraca[i]][0]/2)/(sum(popis_igraca2[imena_igraca[i]])))    
        else: #check+call stavio sam da chekove uzima kao pola, umjest ocijelu vrijednost, dakle check_call== call+check/2
            check_call.append(0)
            #fold:
        if float(popis_igraca2[imena_igraca[i]][3])!=0 and (sum(popis_igraca2[imena_igraca[i]]))!=0 and popis_igraca[imena_igraca[i]][9]>10:  # mora biti prisutan vise od 15 krugova da bi se neka statistika racunala za njega         
            fold.append(float(popis_igraca2[imena_igraca[i]][3])/(sum(popis_igraca2[imena_igraca[i]])))    
        else:
            fold.append(0)

    #if vide_flop>0.4    #loose
    #if vide_flop>0.55 very_lose
    if broj==1:
        return vide_flop
    elif broj==2:
        return bet_raise
    elif broj==3:
        return check_call
    elif broj==4:
        return fold
    
    #print(vide_flop)
    #print(bet_raise)
    #print(check_call)
    #print(fold)
