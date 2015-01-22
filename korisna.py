                #preflop pozicije, preflop sve, sve check,call,raise,fold
def statistika(popis_igraca,popis_igraca0,popis_igraca1,popis_igraca3,popis_igraca4,popis_igraca5,CB_igraca,imena_igraca,a):

    b=a-1
    
    if a>0 and a<6:                 #broj raiseova + broj call  / kroz broj (raise+call+check+fold prijeflopa sve)
        if float(popis_igraca1[imena_igraca[b]][1]+popis_igraca1[imena_igraca[b]][2])>0 and (sum(popis_igraca1[imena_igraca[b]]))>0:
            VPIP=float(popis_igraca1[imena_igraca[b]][1]+popis_igraca1[imena_igraca[b]][2])/(sum(popis_igraca1[imena_igraca[b]]))
        else:
            VPIP=0
        if float(popis_igraca1[imena_igraca[b]][2])>0 and (sum(popis_igraca1[imena_igraca[b]]))>0:            #broj raiseova prijeflopa/ (check+call+raise+fold)
            PFR=float(popis_igraca1[imena_igraca[b]][2])/(sum(popis_igraca1[imena_igraca[b]]))
        else:
            PFR=0
        if float(popis_igraca3[imena_igraca[b]][2]+popis_igraca4[imena_igraca[b]][2]+popis_igraca5[imena_igraca[b]][2])>0 and (popis_igraca3[imena_igraca[b]][1]+popis_igraca4[imena_igraca[b]][1]+popis_igraca5[imena_igraca[b]][1])>0:
                        #Raise nakon flopa, agresija nakon flopa=> raise/call
            AF=float(popis_igraca3[imena_igraca[b]][2]+popis_igraca4[imena_igraca[b]][2]+popis_igraca5[imena_igraca[b]][2])/(popis_igraca3[imena_igraca[b]][1]+popis_igraca4[imena_igraca[b]][1]+popis_igraca5[imena_igraca[b]][1]) #raise/call
        else:                #vidio 5 kartu/vidio 3 kartu
            AF=0
        if float(popis_igraca[imena_igraca[b]][8])>0 and (sum(popis_igraca[imena_igraca[b]][0:6]))>0:
            WTSD=float(popis_igraca[imena_igraca[b]][8])/(sum(popis_igraca[imena_igraca[b]][0:6]))
        else:       #vidio 5 kartu/vidio flop
            WTSD=0
        if float(CB_igraca[imena_igraca[b]][1])>0 and (CB_igraca[imena_igraca[b]][0]+CB_igraca[imena_igraca[b]][1])>0:     
            CB=float(CB_igraca[imena_igraca[b]][1])/(CB_igraca[imena_igraca[b]][0]+CB_igraca[imena_igraca[b]][1])
        else: #postotak,broj puta igrac nastavi raise na flopu, nakon sto je raise preflop
            CB=0
        if float(CB_igraca[imena_igraca[b]][3])>0 and (CB_igraca[imena_igraca[b]][2]+CB_igraca[imena_igraca[b]][3])>0:
            CB2=float(CB_igraca[imena_igraca[b]][3])/(CB_igraca[imena_igraca[b]][2]+CB_igraca[imena_igraca[b]][3])
        else: #postoak koliko puta ce nastavit raiseat na cetvrtoj, ako je raise preflop i flop
            CB2=0


#------____________________________________________________________________________


        pozicija_blefa=popis_igraca0[imena_igraca[b]].index(max(popis_igraca0[imena_igraca[b]]))          #pozicija gdje je najvise raiseo pajdo
        srednja_vrijednost=0
        moja=0
        if sum(popis_igraca0[imena_igraca[b]])>0: #pozicija na kojoj najvise dize
            srednja_vrijednost=float(sum(popis_igraca0[imena_igraca[b]]))/6
        if srednja_vrijednost>0:
            if max(popis_igraca0[imena_igraca[b]])>0 and popis_igraca0[imena_igraca[b]][pozicija_blefa]>float(srednja_vrijednost)*1.7: 
                moja=pozicija_blefa+1                   
            else:
                moja=7  #karte mu podjednako jake svugdje, losiji igrac
        else:
            moja=0

        prijeflopa1=0
        
        if VPIP<0.10: #ultra tight preflop
            #print('ultra tight preflop')
            prijeflopa1=1
        elif VPIP<0.18: #tight preflop
           # print('tight preflop')
            prijeflopa1=2
        elif VPIP>0.40: #loose preflop
           # print('loose preflop')
            prijeflopa1=3
        elif VPIP>0.60: #ultraloose preflop
            #print('ultraloose preflop')
            prijeflopa1=4
        else:       #standard
           # print('standard preflop')
            prijeflopa1=5

        prijeflopa2=0
        if VPIP!=0 and PFR!=0:
            if float(VPIP)/PFR>2.5: # fish, puno cold-call, malo raise
               # print('passive,vjerojatno fish,puno call malo raise prije flopa') 
                prijeflopa2=1
            elif float(VPIP)/PFR>3.5: #sigurno fish
              #  print('passive, sigurno fish, jako puno call, jako malo raise prije flopa')
                prijeflopa2=2
            elif float(VPIP)/PFR<=1.45:
               # print('agresivan prije flopa, jako malo call, samo raise')
                prijeflopa2=3
            elif float(VPIP)/PFR<=1.17:
              #  print('ultra agresivan prije flopa, jako malo call, samo raise')
                prijeflopa2=4
            else: #standard
              #  print('standard, dize prije flopa dosta, ali ne pretjerano, nije fish')
                prijeflopa2=5
            
        postflop1=0
        
        if AF<1: #passive postflop
          #  print('passive postflop')
            postflop1=1    
        elif AF>2:  #aggresive postflop
          #  print('aggresive postflop')
            postflop1=2
        elif AF<0.5: #ultra passive postflop
         #   print('ultra passive postflop')
            postflop1=3
        elif AF>4: #ultra aggrasive postflop
         #   print('ultra aggresive postflop')
            postflop1=4
        else:   #standard
          #  print('standard postflop')
            postflop1=5
            
        postflop2=0
        
        if WTSD>0.33: #calling station , u kombinaciji sa AF,
            if AF>2: #ako je agresivan i ima velik WTSD, previse call-a
           #     print('puno call-a,ceka,value bet')
                postflop2=1
            elif AF<1: #ako je pasivan i ima visok WTSD, pusta ljude da vide flop vise nego treba 
           #     print('pusta ljude da vide flop,value bet')
                postflop2=2
            else:
                #standard, ali isto calling station
          #      print('standard, ali isto calling station')
                postflop2=3
            
        elif WTSD<0.15: #fit or fold, blefirat, foldaju puno nakon flopa,
            if AF>2: ## ako je velik AF tjera ljude da foldaju prije SD,
            #    print('tjera ljude da foldaju na flopu')
                postflop2=4
            elif AF<1: #nizak WTSD i pasivan nakon flopa, onda je weak tight
           #     print('weak tight na flopu')
                postflop2=5
            else: #blefirat,foldaju puno
          #      print('blefirat, puno foldaju prije kraja, nije sigurno zasto') #ne mora znacit
                postflop2=6
        else:
         #   print('standardno vidi 5. kartu, nije calling station niti puno folda na flopu')
            postflop2=7

        postflop3=0

        
        if CB>=0.75 and PFR>0.15: #puno raise-a prije flopa, pa ponovo na flopu, to znaci da cesto na flopu nema karte, ali ipak raise-a
        #    print('puno raise na flopu i prije flopa, znaci da cesto raise na nista')
            postflop3=1
        elif CB<=0.4:
        #    print('nece raise na flopu ako ne dobije nista')
            postflop3=2
        else:
         #   print('nikakve informacije, vezane uz raise na flopu')
            postflop3=5
            
        if CB>=0.75 and CB2<=0.4: # raise na flopu, ali nece na turnu (red fish?), treba ih callat
        #    print('raise-a na flopu, ali ne na turnu, isplati ga se pratit')
            postflop3=3
        elif CB>=0.75 and CB2>0.55:
           # print('nastavlja raise na turnu')
            postflop3=4
        else:
        #    print('CB2 mi nista ne govori, vjerojatno nije read fish')
            postflop3=5

        if popis_igraca[imena_igraca[b]][9]<30:
            prijeflopa1=0
            prijeflopa2=0
            moja=0
            postflop1=0
            postflop2=0
        if popis_igraca[imena_igraca[b]][9]<60:
            postflop3=0
            
        return [prijeflopa1,prijeflopa2,moja,postflop1,postflop2,postflop3]
    #if a==2:        
