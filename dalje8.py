import mis2
import karte
import slike5
import red
#import ruka
import random
import umjetna4
import umjetna4_1
import scr33n
import pomak
import pomak2
import pot
import dizanje
import uigri
import igraci
import button
import imena
import analiza_igraca
import time
import vrsta
import fajlovi
import fajlovi2
import korisna
#import dbhash


situacija=0
pom=0
pom2=0
zastavica=0
vrijeme=4
diz=0
prvi=-3
drugi=-3
treci=-3
cetvrti=-3
peti=-3
pamti_kartu4=55

pamti_kartu=55
pamti_kartu2=55
pamti_kartu3=55
button_gdje=1
broj_flopova=0
broj_krugova=0
statistika=0
cb1=0
cb2=0
cb3=0
cb4=0
cb5=0

pare_uigraca=[]
bet_raise=[0,0,0,0,0]
check_call=[0,0,0,0,0]
foldic=[0,0,0,0,0]
vide_flop3=[0,0,0,0,0]
imena_igraca=['a','b','c','d','e']
ko_raisea='a'
CB_igraca={'a':[0,0,0,0],'b':[0,0,0,0],'c':[0,0,0,0],'d':[0,0,0,0],'e':[0,0,0,0]} #1. nije nastavio raiseat na flopu, 2.nastavio raiseat na flopu, 3. nije nastavio raiseat na turnu, 4. nastavio raiseat i na turnu
popis_igraca={'a':[0,0,0,0,0,0,0,0,0,0],'b':[0,0,0,0,0,0,0,0,0,0],'c':[0,0,0,0,0,0,0,0,0,0],'d':[0,0,0,0,0,0,0,0,0,0],'e':[0,0,0,0,0,0,0,0,0,0]} # button, small blind, bigblind, 3,4,5
popis_igraca1={'a':[0,0,0,0],'b':[0,0,0,0],'c':[0,0,0,0],'d':[0,0,0,0],'e':[0,0,0,0]} #check,call,raise,fold, prije flopa
popis_igraca0={'a':[0,0,0,0,0,0],'b':[0,0,0,0,0,0],'c':[0,0,0,0,0,0],'d':[0,0,0,0,0,0],'e':[0,0,0,0,0,0]} #raise, pozicija
popis_igraca2={'a':[0,0,0,0],'b':[0,0,0,0],'c':[0,0,0,0],'d':[0,0,0,0],'e':[0,0,0,0]} #check,call,raise,fold
popis_igraca3={'a':[0,0,0,0],'b':[0,0,0,0],'c':[0,0,0,0],'d':[0,0,0,0],'e':[0,0,0,0]} #check,call,raise,fold nakon flopa
popis_igraca4={'a':[0,0,0,0],'b':[0,0,0,0],'c':[0,0,0,0],'d':[0,0,0,0],'e':[0,0,0,0]} #na 4
popis_igraca5={'a':[0,0,0,0],'b':[0,0,0,0],'c':[0,0,0,0],'d':[0,0,0,0],'e':[0,0,0,0]} #na 5 karti
while(vrijeme):     #BU,SB,BB,UTG,MP,CO,sve skupa, vidio 4 karte, vidio 5 karata
    time.sleep(0.65)
 
    slike5.grabi(pom,pom2)
    a=0
    
    bre=scr33n.prekid()
    if bre==0:
        break
    if zastavica==0:
        pom=pomak.kamo()
        pom2=pomak2.kamo()
        
        zastavica=1
        continue
    card=[]
    jacina=[]
    znak=[]
    
	
    for i in range(7):
        card.append(karte.koja(i))
        jacina.append(int((card[i]+3)/4)) #pretvorba u kartu
        if card[i]>0:
            znak.append(card[i]%4+1) # pretvorba u znak
        else:
            znak.append(0)

    vrijeme-=1
    a=red.tko(8)
    z1=1

    
            
       
        
    if card[2]>0 and card[2]!=pamti_kartu: #tko je vidio flop
        #statistika+=1
        button_gdje=button.gdje(pom,pom2)
        igraci_uigri=[]
        igraci_uigri=uigri.tko(pom,pom2)
           #broj_flopova+=1
        usporedba1=set(imena_igraca) #za usporedbu 2 liste,nova imena imena koja sam zabiljezio da li su se promjenila
        usporedba2=set(popis_igraca.keys()) #za usporedbu 2 liste, stara imena , u dictionary imena
        usporedba3=usporedba1-usporedba2 # imena u novim imenima koja nisu u starim
        usporedba4=usporedba2-usporedba1 # imena u starim imenima(dictionary) koja nisu u novim

        while (len(usporedba4)):
            sacuvaj=usporedba4.pop()#da ne nestae
            fajlovi2.spremi(sacuvaj,popis_igraca[sacuvaj],8)
            del popis_igraca[sacuvaj] # staro ime se brise
            fajlovi2.spremi(sacuvaj,popis_igraca2[sacuvaj],8)
            del popis_igraca2[sacuvaj]
            fajlovi2.spremi(sacuvaj,popis_igraca3[sacuvaj],8)
            del popis_igraca3[sacuvaj]
            fajlovi2.spremi(sacuvaj,popis_igraca4[sacuvaj],8)
            del popis_igraca4[sacuvaj]
            fajlovi2.spremi(sacuvaj,popis_igraca5[sacuvaj],8)
            del popis_igraca5[sacuvaj]
            fajlovi2.spremi(sacuvaj,popis_igraca1[sacuvaj],8)
            del popis_igraca1[sacuvaj]
            fajlovi2.spremi(sacuvaj,popis_igraca0[sacuvaj],8)
            del popis_igraca0[sacuvaj]
            fajlovi2.spremi(sacuvaj,CB_igraca[sacuvaj],8) #sprema pobrisanog igraca, koji vise ne igra
            del CB_igraca[sacuvaj]
        while (len(usporedba3)):
            sacuvaj=usporedba3.pop()#da ne nestae
            popis_igraca[sacuvaj]=fajlovi.spremi(sacuvaj,1) #novo ime se dodaje
            popis_igraca2[sacuvaj]=fajlovi.spremi(sacuvaj,2)
            popis_igraca3[sacuvaj]=fajlovi.spremi(sacuvaj,3)
            popis_igraca4[sacuvaj]=fajlovi.spremi(sacuvaj,4)
            popis_igraca5[sacuvaj]=fajlovi.spremi(sacuvaj,5)
            popis_igraca1[sacuvaj]=fajlovi.spremi(sacuvaj,6)
            popis_igraca0[sacuvaj]=fajlovi.spremi(sacuvaj,7)
            CB_igraca[sacuvaj]=fajlovi.spremi(sacuvaj,8) #stavlja vec spremljene podatke o novom igracu , ili ako ih nema sve nule [0,0,0,0]


        
                
            
        for i in range(len(igraci_uigri)): #tko je vidio flop , koliko igraca toliko puta se vrti
            if (button_gdje)==(igraci_uigri[i]): # BU na buttonu
                popis_igraca[imena_igraca[(igraci_uigri[i])-1]][0]+=1 #   ime koje ima igrac koji je doso vidit flop,ime igraca 5 npr., njemu dodati 1

            elif (button_gdje)%6==(igraci_uigri[i]+5)%6:#small blind SB
                popis_igraca[imena_igraca[(igraci_uigri[i])-1]][1]+=1
            elif (button_gdje)%6==(igraci_uigri[i]+4)%6:#big blind BB
                popis_igraca[imena_igraca[(igraci_uigri[i])-1]][2]+=1
            elif (button_gdje)%6==(igraci_uigri[i]+3)%6:#big blind+1 UTG
                popis_igraca[imena_igraca[(igraci_uigri[i])-1]][3]+=1
            elif (button_gdje)%6==(igraci_uigri[i]+2)%6:#big blind+2  MP
                popis_igraca[imena_igraca[(igraci_uigri[i])-1]][4]+=1
            elif (button_gdje)%6==(igraci_uigri[i]+1)%6:# CO
                popis_igraca[imena_igraca[(igraci_uigri[i])-1]][5]+=1
            
        for i in range(5):
            popis_igraca[imena_igraca[i]][6]+=1 # svim igracima dodat koliko je flopova doslo
        #print('dosao flop => za pamcenje,ko je vidio flop')
        #print(popis_igraca)
        pamti_kartu=card[2]
        #print(imena_igraca[0],popis_igraca[imena_igraca[0]])
        
    elif card[5]>0 and card[5]!=pamti_kartu2: #ko je vidio 4. kartu
        pamti_kartu2=card[5]
        
        igraci_uigri=[]
        igraci_uigri=uigri.tko(pom,pom2)
         
        usporedba1=set(imena_igraca) #za usporedbu 2 liste,nova imena imena koja sam zabiljezio da li su se promjenila
        usporedba2=set(popis_igraca.keys()) #za usporedbu 2 liste, stara imena , u dictionary imena
        usporedba3=usporedba1-usporedba2 # imena u novim imenima koja nisu u starim
        usporedba4=usporedba2-usporedba1 # imena u starim imenima(dictionary) koja nisu u novim

        while (len(usporedba4)):
            sacuvaj=usporedba4.pop()#da ne nestae
            fajlovi2.spremi(sacuvaj,popis_igraca[sacuvaj],8)
            del popis_igraca[sacuvaj] # staro ime se brise
            fajlovi2.spremi(sacuvaj,popis_igraca2[sacuvaj],8)
            del popis_igraca2[sacuvaj]
            fajlovi2.spremi(sacuvaj,popis_igraca3[sacuvaj],8)
            del popis_igraca3[sacuvaj]
            fajlovi2.spremi(sacuvaj,popis_igraca4[sacuvaj],8)
            del popis_igraca4[sacuvaj]
            fajlovi2.spremi(sacuvaj,popis_igraca5[sacuvaj],8)
            del popis_igraca5[sacuvaj]
            fajlovi2.spremi(sacuvaj,popis_igraca1[sacuvaj],8)
            del popis_igraca1[sacuvaj]
            fajlovi2.spremi(sacuvaj,popis_igraca0[sacuvaj],8)
            del popis_igraca0[sacuvaj]
            fajlovi2.spremi(sacuvaj,CB_igraca[sacuvaj],8) #sprema pobrisanog igraca, koji vise ne igra
            del CB_igraca[sacuvaj]
        while (len(usporedba3)):
            sacuvaj=usporedba3.pop()#da ne nestae
            popis_igraca[sacuvaj]=fajlovi.spremi(sacuvaj,1) #novo ime se dodaje
            popis_igraca2[sacuvaj]=fajlovi.spremi(sacuvaj,2)
            popis_igraca3[sacuvaj]=fajlovi.spremi(sacuvaj,3)
            popis_igraca4[sacuvaj]=fajlovi.spremi(sacuvaj,4)
            popis_igraca5[sacuvaj]=fajlovi.spremi(sacuvaj,5)
            popis_igraca1[sacuvaj]=fajlovi.spremi(sacuvaj,6)
            popis_igraca0[sacuvaj]=fajlovi.spremi(sacuvaj,7)
            CB_igraca[sacuvaj]=fajlovi.spremi(sacuvaj,8) #stavlja vec spremljene podatke o novom igracu , ili ako ih nema sve nule [0,0,0,0]


        
        for i in range(len(igraci_uigri)):
            popis_igraca[imena_igraca[(igraci_uigri[i])-1]][7]+=1
        #print(imena_igraca[0],popis_igraca[imena_igraca[0]])  

    elif card[6]>0 and card[6]!=pamti_kartu3: #ko je vidio 5. kartu
        pamti_kartu3=card[6]

        igraci_uigri=[]
        igraci_uigri=uigri.tko(pom,pom2)
           #broj_flopova+=1
        usporedba1=set(imena_igraca) #za usporedbu 2 liste,nova imena imena koja sam zabiljezio da li su se promjenila
        usporedba2=set(popis_igraca.keys()) #za usporedbu 2 liste, stara imena , u dictionary imena
        usporedba3=usporedba1-usporedba2 # imena u novim imenima koja nisu u starim
        usporedba4=usporedba2-usporedba1 # imena u starim imenima(dictionary) koja nisu u novim

        while (len(usporedba4)):
            sacuvaj=usporedba4.pop()#da ne nestae
            fajlovi2.spremi(sacuvaj,popis_igraca[sacuvaj],8)
            del popis_igraca[sacuvaj] # staro ime se brise
            fajlovi2.spremi(sacuvaj,popis_igraca2[sacuvaj],8)
            del popis_igraca2[sacuvaj]
            fajlovi2.spremi(sacuvaj,popis_igraca3[sacuvaj],8)
            del popis_igraca3[sacuvaj]
            fajlovi2.spremi(sacuvaj,popis_igraca4[sacuvaj],8)
            del popis_igraca4[sacuvaj]
            fajlovi2.spremi(sacuvaj,popis_igraca5[sacuvaj],8)
            del popis_igraca5[sacuvaj]
            fajlovi2.spremi(sacuvaj,popis_igraca1[sacuvaj],8)
            del popis_igraca1[sacuvaj]
            fajlovi2.spremi(sacuvaj,popis_igraca0[sacuvaj],8)
            del popis_igraca0[sacuvaj]
            fajlovi2.spremi(sacuvaj,CB_igraca[sacuvaj],8) #sprema pobrisanog igraca, koji vise ne igra
            del CB_igraca[sacuvaj]
        while (len(usporedba3)):
            sacuvaj=usporedba3.pop()#da ne nestae
            popis_igraca[sacuvaj]=fajlovi.spremi(sacuvaj,1) #novo ime se dodaje
            popis_igraca2[sacuvaj]=fajlovi.spremi(sacuvaj,2)
            popis_igraca3[sacuvaj]=fajlovi.spremi(sacuvaj,3)
            popis_igraca4[sacuvaj]=fajlovi.spremi(sacuvaj,4)
            popis_igraca5[sacuvaj]=fajlovi.spremi(sacuvaj,5)
            popis_igraca1[sacuvaj]=fajlovi.spremi(sacuvaj,6)
            popis_igraca0[sacuvaj]=fajlovi.spremi(sacuvaj,7)
            CB_igraca[sacuvaj]=fajlovi.spremi(sacuvaj,8) #stavlja vec spremljene podatke o novom igracu , ili ako ih nema sve nule [0,0,0,0]

        
        for i in range(len(igraci_uigri)):
            popis_igraca[imena_igraca[(igraci_uigri[i])-1]][8]+=1

        #print(imena_igraca[0],popis_igraca[imena_igraca[0]])    
    prvi-=1
    drugi-=1
    treci-=1
    cetvrti-=1
    peti-=1
    if prvi<-2 or drugi<-2 or treci<-2 or cetvrti<-2 or peti<-2:
        usporedba1=set(imena_igraca) #za usporedbu 2 liste,nova imena imena koja sam zabiljezio da li su se promjenila
        usporedba2=set(popis_igraca.keys()) #za usporedbu 2 liste, stara imena , u dictionary imena
        usporedba3=usporedba1-usporedba2 # imena u novim imenima koja nisu u starim
        usporedba4=usporedba2-usporedba1 # imena u starim imenima(dictionary) koja nisu u novim

        while (len(usporedba4)):
            sacuvaj=usporedba4.pop()#da ne nestae
            fajlovi2.spremi(sacuvaj,popis_igraca[sacuvaj],8)
            del popis_igraca[sacuvaj] # staro ime se brise
            fajlovi2.spremi(sacuvaj,popis_igraca2[sacuvaj],8)
            del popis_igraca2[sacuvaj]
            fajlovi2.spremi(sacuvaj,popis_igraca3[sacuvaj],8)
            del popis_igraca3[sacuvaj]
            fajlovi2.spremi(sacuvaj,popis_igraca4[sacuvaj],8)
            del popis_igraca4[sacuvaj]
            fajlovi2.spremi(sacuvaj,popis_igraca5[sacuvaj],8)
            del popis_igraca5[sacuvaj]
            fajlovi2.spremi(sacuvaj,popis_igraca1[sacuvaj],8)
            del popis_igraca1[sacuvaj]
            fajlovi2.spremi(sacuvaj,popis_igraca0[sacuvaj],8)
            del popis_igraca0[sacuvaj]
            fajlovi2.spremi(sacuvaj,CB_igraca[sacuvaj],8) #sprema pobrisanog igraca, koji vise ne igra
            del CB_igraca[sacuvaj]
        while (len(usporedba3)):
            sacuvaj=usporedba3.pop()#da ne nestae
            popis_igraca[sacuvaj]=fajlovi.spremi(sacuvaj,1) #novo ime se dodaje
            popis_igraca2[sacuvaj]=fajlovi.spremi(sacuvaj,2)
            popis_igraca3[sacuvaj]=fajlovi.spremi(sacuvaj,3)
            popis_igraca4[sacuvaj]=fajlovi.spremi(sacuvaj,4)
            popis_igraca5[sacuvaj]=fajlovi.spremi(sacuvaj,5)
            popis_igraca1[sacuvaj]=fajlovi.spremi(sacuvaj,6)
            popis_igraca0[sacuvaj]=fajlovi.spremi(sacuvaj,7)
            CB_igraca[sacuvaj]=fajlovi.spremi(sacuvaj,8) #stavlja vec spremljene podatke o novom igracu , ili ako ih nema sve nule [0,0,0,0]

            
        krugic1=analiza_igraca.kakav(1,pom,pom2)
        krugic2=analiza_igraca.kakav(2,pom,pom2)
        krugic3=analiza_igraca.kakav(3,pom,pom2)
        krugic4=analiza_igraca.kakav(4,pom,pom2)
        krugic5=analiza_igraca.kakav(5,pom,pom2)
        button_gdje=button.gdje(pom,pom2)
        
    if prvi<-2:
        #print('igrac1',analiza_igraca.kakav(1,pom,pom2))

        
        if card[2]==0:
            pomocni_niz=[0,1,2,3,4,5]

            
                
            
            if krugic1==1:   #prvi igrac, flop
                popis_igraca1[imena_igraca[0]][0]+=1#igracu dodati check,call,raise,fold statistiku    
                prvi=0
                cb1=0
            elif krugic1==2:
                popis_igraca1[imena_igraca[0]][1]+=1
                prvi=0
                cb1=0
            elif krugic1==3: #raise
                cb1=0
                popis_igraca1[imena_igraca[0]][2]+=1
                prvi=0
                popis_igraca0[imena_igraca[0]][pomocni_niz[1-button_gdje]]+=1
                cb1+=1
                ko_raisea=imena_igraca[0]
            elif krugic1==4:
                popis_igraca1[imena_igraca[0]][3]+=1
                prvi=0
                cb1=0
            #print(imena_igraca[0],popis_igraca0[imena_igraca[0]])
           

        elif card[2]>0 and card[5]==0:   
            if krugic1==1:  #prvi igrac, flop
                popis_igraca3[imena_igraca[0]][0]+=1#igracu dodati check,call,raise,fold statistiku    
                prvi=0
                if cb1==1: #nema continuation bet
                    print('igrac1 raise prije flopa,ali ne na flopu')
                    cb1=0
                    CB_igraca[imena_igraca[0]][0]+=1 #raise prije flopa,ali nije na flopu
            elif krugic1==2:
                popis_igraca3[imena_igraca[0]][1]+=1
                prvi=0
                if cb1==1: #nema continuation bet
                    print('igrac1 raise prije flopa,ali ne na flopu')
                    cb1=0
                    CB_igraca[imena_igraca[0]][0]+=1 #raise prije flopa,ali nije na flopu
            elif krugic1==3:
                popis_igraca3[imena_igraca[0]][2]+=1
                prvi=0
                cb1+=2
                if cb1==3: #continuatuion bet na flopu
                    CB_igraca[imena_igraca[0]][1]+=1 #raise prije flopa i na flopu
                    print('igrac1 raise prije flopa,i na flopu')
                ko_raisea=imena_igraca[0]
            elif krugic1==4:
                popis_igraca3[imena_igraca[0]][3]+=1
                prvi=0
                if cb1==1: #nema continuation bet
                    print('igrac1 raise prije flopa,ali ne na flopu')
                    cb1=0
                    CB_igraca[imena_igraca[0]][0]+=1 #raise prije flopa,ali nije na flopu

            
            
                 
        elif card[2]>0 and card[5]>0 and card[6]==0:
            if krugic1==1:   #prvi igrac, 4 karte dole
                popis_igraca4[imena_igraca[0]][0]+=1 #igracu dodati check,call,raise,fold statistiku    
                prvi=0
            elif krugic1==2 :
                popis_igraca4[imena_igraca[0]][1]+=1
                prvi=0
            elif krugic1==3 :
                popis_igraca4[imena_igraca[0]][2]+=1
                prvi=0
                cb1+=4
                ko_raisea=imena_igraca[0]
            elif krugic1==4 :
                popis_igraca4[imena_igraca[0]][3]+=1
                prvi=0

            if cb1==3 and krugic1!=0:
                cb1=0
                CB_igraca[imena_igraca[0]][2]+=1 #raise prijeflopa,na flopu, ali ne na turnu
                print('igrac1 raise prije flopa,i na flopu,ali ne na turnu')
            elif cb1==7 and krugic1!=0: #continuation bet na četvrtoj
                CB_igraca[imena_igraca[0]][3]+=1 #raise prijeflopa,na flopu, i na turnu
                print('igrac1 raise prije flopa,i na flopu i na turnu')

                
        elif card[2]>0 and card[5]>0 and card[6]>0:
            if krugic1==1 :   #prvi igrac, 5 karata dole
                popis_igraca5[imena_igraca[0]][0]+=1#igracu dodati check,call,raise,fold statistiku    
                prvi=0
            elif krugic1==2:
                popis_igraca5[imena_igraca[0]][1]+=1
                prvi=0
            elif krugic1==3:
                popis_igraca5[imena_igraca[0]][2]+=1
                prvi=0
                cb1+=8
                ko_raisea=imena_igraca[0]
            elif krugic1==4:
                popis_igraca5[imena_igraca[0]][3]+=1
                prvi=0
            if cb1==7:
                cb1=0
            elif cb1==15: #cb i na petoj

                cb1=0
        
        if krugic1==1:   #prvi igrac
            popis_igraca2[imena_igraca[0]][0]+=1#igracu dodati check,call,raise,fold statistiku    
            prvi=0
        elif krugic1==2:
            popis_igraca2[imena_igraca[0]][1]+=1
            prvi=0
        elif krugic1==3:
            popis_igraca2[imena_igraca[0]][2]+=1
            prvi=0
            ko_raisea=imena_igraca[0]
        elif krugic1==4:
            popis_igraca2[imena_igraca[0]][3]+=1
            prvi=0
        #print(imena_igraca[0],popis_igraca2[imena_igraca[0]],analiza_igraca.kakav(1,pom,pom2))
    if drugi<-2:
        #print('igrac2',analiza_igraca.kakav(2,pom,pom2))

        if card[2]==0:
            pomocni_niz=[0,1,2,3,4,5]

            
            
            if krugic2==1 : #drugi igrac,flop
                popis_igraca1[imena_igraca[1]][0]+=1 #igracu dodati check,call,raise,fold statistiku    
                drugi=0
                cb2=0
            elif krugic2==2 :
                popis_igraca1[imena_igraca[1]][1]+=1
                drugi=0
                cb2=0
            elif krugic2==3 : #raise
                cb2=0
                popis_igraca1[imena_igraca[1]][2]+=1
                drugi=0
                popis_igraca0[imena_igraca[1]][pomocni_niz[2-button_gdje]]+=1 #dodati, poziciju ukojoj je raiseo prije flopa
                cb2+=1
                ko_raisea=imena_igraca[1]
            elif krugic2==4:
                popis_igraca1[imena_igraca[1]][3]+=1
                drugi=0
                cb2=0
            #print(imena_igraca[1],popis_igraca0[imena_igraca[1]])

            

            
        elif card[2]>0 and card[5]==0:  
            if krugic2==1: #drugi igrac,flop
                popis_igraca3[imena_igraca[1]][0]+=1 #igracu dodati check,call,raise,fold statistiku    
                drugi=0
            elif krugic2==2 :
                popis_igraca3[imena_igraca[1]][1]+=1
                drugi=0
            elif krugic2==3 :
                popis_igraca3[imena_igraca[1]][2]+=1
                drugi=0
                cb2+=2
                ko_raisea=imena_igraca[1]
            elif krugic2==4:
                popis_igraca3[imena_igraca[1]][3]+=1
                drugi=0

            if cb2==1 and krugic2!=0:
                cb2=0
                CB_igraca[imena_igraca[1]][0]+=1
            elif cb2==3 and krugic2!=0: #continutatino bet na flopu
                CB_igraca[imena_igraca[1]][1]+=1
            
        elif card[2]>0 and card[5]>0 and card[6]==0:
            if krugic2==1: #drugi igrac, 4 karte
                popis_igraca4[imena_igraca[1]][0]+=1 #igracu dodati check,call,raise,fold statistiku    
                drugi=0
            elif krugic2==2:
                popis_igraca4[imena_igraca[1]][1]+=1
                drugi=0
            elif krugic2==3 :
                popis_igraca4[imena_igraca[1]][2]+=1
                drugi=0
                cb2+=4
                ko_raisea=imena_igraca[1]
            elif krugic2==4:
                popis_igraca4[imena_igraca[1]][3]+=1
                drugi=0

            if cb2==3 and krugic2!=0: #nema cb-a
                cb2=0
                CB_igraca[imena_igraca[1]][2]+=1
            elif cb2==7 and krugic2!=0: #cb se nastavlja na 4
                CB_igraca[imena_igraca[1]][3]+=1
                
        elif card[2]>0 and card[5]>0 and card[6]>0:
            if krugic2==1: #drugi igrac, 5 karata
                popis_igraca5[imena_igraca[1]][0]+=1 #igracu dodati check,call,raise,fold statistiku    
                drugi=0
            elif krugic2==2:
                popis_igraca5[imena_igraca[1]][1]+=1
                drugi=0
            elif krugic2==3:
                popis_igraca5[imena_igraca[1]][2]+=1
                drugi=0
                cb2+=8
                ko_raisea=imena_igraca[1]
            elif krugic2==4:
                popis_igraca5[imena_igraca[1]][3]+=1
                drugi=0

            if cb2==7:
                cb2==0
            elif cb2==15: #cb se nastavlja

                cb2=0
        
        if krugic2==1: #drugi igrac
            popis_igraca2[imena_igraca[1]][0]+=1 #igracu dodati check,call,raise,fold statistiku    
            drugi=0
        elif krugic2==2:
            popis_igraca2[imena_igraca[1]][1]+=1
            drugi=0
        elif krugic2==3:
            popis_igraca2[imena_igraca[1]][2]+=1
            drugi=0
            ko_raisea=imena_igraca[1]
        elif krugic2==4:
            popis_igraca2[imena_igraca[1]][3]+=1
            drugi=0

            
    if treci<-2:
        #print('igrac3',analiza_igraca.kakav(3,pom,pom2))

        if card[2]==0:
            pomocni_niz=[0,1,2,3,4,5] #koristi za određivanje pozicije igraca koji raise-a
            
            if krugic3==1 : #treci igrac
                popis_igraca1[imena_igraca[2]][0]+=1#igracu dodati check,call,raise,fold statistiku    
                treci=0
                cb3=0
            elif krugic3==2:
                treci=0
                popis_igraca1[imena_igraca[2]][1]+=1
                cb3=0
            elif krugic3==3:
                cb3=0
                popis_igraca1[imena_igraca[2]][2]+=1
                treci=0
                cb3+=1
                popis_igraca0[imena_igraca[2]][pomocni_niz[3-button_gdje]]
                ko_raisea=imena_igraca[2]
            elif krugic3==4:
                treci=0
                cb3=0
                popis_igraca1[imena_igraca[2]][3]+=1

            
            #print(imena_igraca[2],popis_igraca0[imena_igraca[2]])
        elif card[2]>0 and card[5]==0:     
            if krugic3==1: #treci igrac
                popis_igraca3[imena_igraca[2]][0]+=1#igracu dodati check,call,raise,fold statistiku    
                treci=0
            elif krugic3==2:
                treci=0
                popis_igraca3[imena_igraca[2]][1]+=1
            elif krugic3==3:
                popis_igraca3[imena_igraca[2]][2]+=1
                treci=0
                cb3+=2
                ko_raisea=imena_igraca[2]
            elif krugic3==4:
                treci=0
                popis_igraca3[imena_igraca[2]][3]+=1

            if cb3==1 and krugic3!=0:
                cb3=0
                CB_igraca[imena_igraca[2]][0]+=1
            elif cb3==3 and krugic3!=0:
                CB_igraca[imena_igraca[2]][1]+=1
                
        elif card[2]>0 and card[5]>0 and card[6]==0:
            if krugic3==1 : #treci igrac
                popis_igraca4[imena_igraca[2]][0]+=1#igracu dodati check,call,raise,fold statistiku    
                treci=0
            elif krugic3==2:
                treci=0
                popis_igraca4[imena_igraca[2]][1]+=1
            elif krugic3==3 :
                popis_igraca4[imena_igraca[2]][2]+=1
                treci=0
                cb3+=4
                ko_raisea=imena_igraca[2]
            elif krugic3==4:
                treci=0
                popis_igraca4[imena_igraca[2]][3]+=1

            if cb3==3 and krugic3!=0:
                CB_igraca[imena_igraca[2]][2]+=1
                cb3=0
            elif cb3==7 and krugic3!=0:
                CB_igraca[imena_igraca[2]][3]+=1
                
        elif card[2]>0 and card[5]>0 and card[6]>0:
            if krugic3==1 : #treci igrac
                popis_igraca5[imena_igraca[2]][0]+=1#igracu dodati check,call,raise,fold statistiku    
                treci=0
            elif krugic3==2:
                treci=0
                popis_igraca5[imena_igraca[2]][1]+=1
            elif krugic3==3:
                popis_igraca5[imena_igraca[2]][2]+=1
                treci=0
                cb3+=8
                ko_raisea=imena_igraca[2]
            elif krugic3==4:
                treci=0
                popis_igraca5[imena_igraca[2]][3]+=1


            if cb3==7:
                cb3=0
            elif cb3==15: #nastavak cb

                cb3=0
    
        if krugic3==1: #treci igrac
            popis_igraca2[imena_igraca[2]][0]+=1#igracu dodati check,call,raise,fold statistiku    
            treci=0
        elif krugic3==2:
            treci=0
            popis_igraca2[imena_igraca[2]][1]+=1
        elif krugic3==3:
            popis_igraca2[imena_igraca[2]][2]+=1
            treci=0
            ko_raisea=imena_igraca[2]
        elif krugic3==4:
            treci=0
            popis_igraca2[imena_igraca[2]][3]+=1

    if cetvrti<-2:
        #print('igrac4',analiza_igraca.kakav(4,pom,pom2))
        if card[2]==0:

            pomocni_niz=[0,1,2,3,4,5]
            if krugic4==1: #cetvrti igrac
                popis_igraca1[imena_igraca[3]][0]+=1 #igracu dodati check,call,raise,fold statistiku    
                cetvrti=0
                cb4=0
            elif krugic4==2:
                popis_igraca1[imena_igraca[3]][1]+=1
                cetvrti=0
                cb4=0
            elif krugic4==3:
                cb4=1
                popis_igraca1[imena_igraca[3]][2]+=1
                cetvrti=0
                popis_igraca0[imena_igraca[3]][pomocni_niz[4-button_gdje]]+=1
                ko_raisea=imena_igraca[3]
            elif krugic4==4:
                popis_igraca1[imena_igraca[3]][3]+=1
                cetvrti=0


            #print(imena_igraca[3],popis_igraca0[imena_igraca[3]])
        elif card[2]>0 and card[5]==0:
            if krugic4==1: #cetvrti igrac
                popis_igraca3[imena_igraca[3]][0]+=1 #igracu dodati check,call,raise,fold statistiku    
                cetvrti=0
            elif krugic4==2 :
                popis_igraca3[imena_igraca[3]][1]+=1
                cetvrti=0
            elif krugic4==3:
                popis_igraca3[imena_igraca[3]][2]+=1
                cetvrti=0
                cb4+=2
                ko_raisea=imena_igraca[3]
            elif krugic4==4:
                popis_igraca3[imena_igraca[3]][3]+=1
                cetvrti=0

            if cb4==1 and krugic4!=0:
                cb4=0
                CB_igraca[imena_igraca[3]][0]+=1
            elif cb4==3 and krugic4!=0:
                CB_igraca[imena_igraca[3]][1]+=1
                
        elif card[2]>0 and card[5]>0 and card[6]==0:
            if krugic4==1: #cetvrti igrac
                popis_igraca4[imena_igraca[3]][0]+=1 #igracu dodati check,call,raise,fold statistiku    
                cetvrti=0
            elif krugic4==2:
                popis_igraca4[imena_igraca[3]][1]+=1
                cetvrti=0
            elif krugic4==3:
                popis_igraca4[imena_igraca[3]][2]+=1
                cetvrti=0
                cb4+=4
                ko_raisea=imena_igraca[3]
            elif krugic4==4:
                popis_igraca4[imena_igraca[3]][3]+=1
                cetvrti=0

            if cb4==3 and krugic4!=0:
                cb4=0
                CB_igraca[imena_igraca[3]][2]+=1
            elif cb4==7 and krugic4!=0:
                CB_igraca[imena_igraca[3]][3]+=1
                
        elif card[2]>0 and card[5]>0 and card[6]>0:
            if krugic4==1: #cetvrti igrac
                popis_igraca5[imena_igraca[3]][0]+=1 #igracu dodati check,call,raise,fold statistiku    
                cetvrti=0
            elif krugic4==2:
                popis_igraca5[imena_igraca[3]][1]+=1
                cetvrti=0
            elif krugic4==3:
                popis_igraca5[imena_igraca[3]][2]+=1
                cetvrti=0
                cb4+=8
                ko_raisea=imena_igraca[3]
            elif krugic4==4:
                popis_igraca5[imena_igraca[3]][3]+=1
                cetvrti=0

            if cb4==7:
                cb4=0
            #elif cb4==15:
        
        if krugic4==1: #cetvrti igrac
            popis_igraca2[imena_igraca[3]][0]+=1 #igracu dodati check,call,raise,fold statistiku    
            cetvrti=0
        elif krugic4==2:
            popis_igraca2[imena_igraca[3]][1]+=1
            cetvrti=0
        elif krugic4==3:
            popis_igraca2[imena_igraca[3]][2]+=1
            cetvrti=0
            ko_raisea=imena_igraca[3]
        elif krugic4==4:
            popis_igraca2[imena_igraca[3]][3]+=1
            cetvrti=0
    if peti<-2:
        #print('igrac5',analiza_igraca.kakav(5,pom,pom2))


        if card[2]==0:

            pomocni_niz=[0,1,2,3,4,5]
            if krugic5==1 : #peti igrac
                popis_igraca1[imena_igraca[4]][0]+=1 #igracu dodati check,call,raise,fold statistiku    
                peti=0
            elif krugic5==2:
                popis_igraca1[imena_igraca[4]][1]+=1
                peti=0
            elif krugic5==3 :
                cb5=1
                popis_igraca1[imena_igraca[4]][2]+=1
                peti=0
                popis_igraca0[imena_igraca[4]][pomocni_niz[5-button_gdje]]+=1
                ko_raisea=imena_igraca[4]
            elif krugic5==4 :
                popis_igraca1[imena_igraca[4]][3]+=1
                peti=0
            #print(imena_igraca[4],popis_igraca0[imena_igraca[4]])
            
        elif card[2]>0 and card[5]==0:
            if krugic5==1: #peti igrac
                popis_igraca3[imena_igraca[4]][0]+=1 #igracu dodati check,call,raise,fold statistiku    
                peti=0
            elif krugic5==2:
                popis_igraca3[imena_igraca[4]][1]+=1
                peti=0
            elif krugic5==3:
                popis_igraca3[imena_igraca[4]][2]+=1
                peti=0
                cb5+=2
                ko_raisea=imena_igraca[4]
            elif krugic5==4:
                popis_igraca3[imena_igraca[4]][3]+=1
                peti=0

            if cb5==1  and krugic5!=0:
                cb5=0
                CB_igraca[imena_igraca[4]][0]+=1
            elif cb5==3 and krugic5!=0:
                CB_igraca[imena_igraca[4]][1]+=1
                
        elif card[2]>0 and card[5]>0 and card[6]==0:
            if krugic5==1: #peti igrac
                popis_igraca4[imena_igraca[4]][0]+=1 #igracu dodati check,call,raise,fold statistiku    
                peti=0
            elif krugic5==2:
                popis_igraca4[imena_igraca[4]][1]+=1
                peti=0
            elif krugic5==3:
                popis_igraca4[imena_igraca[4]][2]+=1
                peti=0
                cb5+=4
                ko_raisea=imena_igraca[4]
            elif krugic5==4:
                popis_igraca4[imena_igraca[4]][3]+=1
                peti=0

            if cb5==3 and krugic5!=0:
                cb5=0
                CB_igraca[imena_igraca[4]][2]+=1
            elif cb5==7 and krugic5!=0:
                CB_igraca[imena_igraca[4]][3]+=1
                
                
        elif card[2]>0 and card[5]>0 and card[6]>0:
            if krugic5==1: #peti igrac
                popis_igraca5[imena_igraca[4]][0]+=1 #igracu dodati check,call,raise,fold statistiku    
                peti=0
            elif krugic5==2:
                popis_igraca5[imena_igraca[4]][1]+=1
                peti=0
            elif krugic5==3:
                popis_igraca5[imena_igraca[4]][2]+=1
                peti=0
                cb5+=8
                ko_raisea=imena_igraca[4]
            elif krugic5==4:
                popis_igraca5[imena_igraca[4]][3]+=1
                peti=0

            if cb5==7:
                cb5=0
            #elif cb5==15:
        
        if krugic5==1: #peti igrac
            popis_igraca2[imena_igraca[4]][0]+=1 #igracu dodati check,call,raise,fold statistiku    
            peti=0
        elif krugic5==2:
            popis_igraca2[imena_igraca[4]][1]+=1
            peti=0
        elif krugic5==3:
            popis_igraca2[imena_igraca[4]][2]+=1
            peti=0
            ko_raisea=imena_igraca[4]
        elif krugic5==4:
            popis_igraca2[imena_igraca[4]][3]+=1
            peti=0

   
    if statistika>4: #broj flopova, nebitno jer u modulu vrsta se pazi da li igrac ima dovoljno krugova za racunanje statistike

        vide_flop3=vrsta.igraca(popis_igraca,popis_igraca2,imena_igraca,1)
        bet_raise=vrsta.igraca(popis_igraca,popis_igraca2,imena_igraca,2) #postotak raisea za sve igrace
        check_call=vrsta.igraca(popis_igraca,popis_igraca2,imena_igraca,3) #postotak check call-a
        foldic=vrsta.igraca(popis_igraca,popis_igraca2,imena_igraca,4) # postotak folda, za sve igrace
    if a:
        
        

        
            
        card=[]
        jacina=[]
        znak=[]
        for i in range(7):
            card.append(karte.koja(i))
            jacina.append(int((card[i]+3)/4))
            if card[i]>0:
                znak.append(card[i]%4+1)
            else:
                znak.append(0)
        if card[2]>0: #ako je flop doso
            print('doso flop')
            #situacija=2
            
        else:
            situacija=0

        if card[0]>0 and card[0]!=pamti_kartu4:
            statistika+=1

            imena_igraca=[]
            for i in range(5):
                imena_igraca.append(imena.pamti((i+1),pom,pom2))
            
            usporedba1=set(imena_igraca) #za usporedbu 2 liste,nova imena imena koja sam zabiljezio da li su se promjenila
            usporedba2=set(popis_igraca.keys()) #za usporedbu 2 liste, stara imena , u dictionary imena
            usporedba3=usporedba1-usporedba2 # imena u novim imenima koja nisu u starim
            usporedba4=usporedba2-usporedba1 # imena u starim imenima(dictionary) koja nisu u novim

            while (len(usporedba4)):
                sacuvaj=usporedba4.pop()#da ne nestae
                fajlovi2.spremi(sacuvaj,popis_igraca[sacuvaj],8)
                del popis_igraca[sacuvaj] # staro ime se brise
                fajlovi2.spremi(sacuvaj,popis_igraca2[sacuvaj],8)
                del popis_igraca2[sacuvaj]
                fajlovi2.spremi(sacuvaj,popis_igraca3[sacuvaj],8)
                del popis_igraca3[sacuvaj]
                fajlovi2.spremi(sacuvaj,popis_igraca4[sacuvaj],8)
                del popis_igraca4[sacuvaj]
                fajlovi2.spremi(sacuvaj,popis_igraca5[sacuvaj],8)
                del popis_igraca5[sacuvaj]
                fajlovi2.spremi(sacuvaj,popis_igraca1[sacuvaj],8)
                del popis_igraca1[sacuvaj]
                fajlovi2.spremi(sacuvaj,popis_igraca0[sacuvaj],8)
                del popis_igraca0[sacuvaj]
                fajlovi2.spremi(sacuvaj,CB_igraca[sacuvaj],8) #sprema pobrisanog igraca, koji vise ne igra
                del CB_igraca[sacuvaj]
            while (len(usporedba3)):
                sacuvaj=usporedba3.pop()#da ne nestae
                popis_igraca[sacuvaj]=fajlovi.spremi(sacuvaj,1) #novo ime se dodaje
                popis_igraca2[sacuvaj]=fajlovi.spremi(sacuvaj,2)
                popis_igraca3[sacuvaj]=fajlovi.spremi(sacuvaj,3)
                popis_igraca4[sacuvaj]=fajlovi.spremi(sacuvaj,4)
                popis_igraca5[sacuvaj]=fajlovi.spremi(sacuvaj,5)
                popis_igraca1[sacuvaj]=fajlovi.spremi(sacuvaj,6)
                popis_igraca0[sacuvaj]=fajlovi.spremi(sacuvaj,7)
                CB_igraca[sacuvaj]=fajlovi.spremi(sacuvaj,8) #stavlja vec spremljene podatke o novom igracu , ili ako ih nema sve nule [0,0,0,0]


            if (statistika%10)==0: #svakih 10 krugova
                for i in imena_igraca:
                    fajlovi2.spremi(i,popis_igraca[i],1)
                    fajlovi2.spremi(i,popis_igraca2[i],2)
                    fajlovi2.spremi(i,popis_igraca3[i],3)
                    fajlovi2.spremi(i,popis_igraca4[i],4)
                    fajlovi2.spremi(i,popis_igraca5[i],5)
                    fajlovi2.spremi(i,popis_igraca1[i],6)
                    fajlovi2.spremi(i,popis_igraca0[i],7)
                    fajlovi2.spremi(i,CB_igraca[i],8)

                print('statistika',statistika)
                
            pamti_kartu4=card[0]
            broj_krugova+=1
            for i in range (len(imena_igraca)):
                if len(pare_uigraca)>4:
                    if pare_uigraca[i]!=0:#ako je nula onda ili nije igrac, ili je sitting out
                        popis_igraca[imena_igraca[i]][9]+=1
                else:    
                    popis_igraca[imena_igraca[i]][9]+=1 #broj krugova vidio
                
            #print(popis_igraca[imena_igraca[1]])

        blinds=pot.koji(pom,pom2)
        if a==2:
            diz=dizanje.koliki(a)
        elif a==3:
            diz=dizanje.koliki(a)

        
        
        #for i in range(len(igraci_uigri)):
            #igraci.podaci(igraci_uigri[i],pom,pom2)

        button_gdje=button.gdje(pom,pom2)
        vide_flop=[]
        igraci_uigri=[]
        igraci_uigri=uigri.tko(pom,pom2)
        bet_raise2=[]
        check_call2=[]
        foldic2=[]
        #if statistika>=10:
             #tko ima karte na stolu u trenutku kad sam ja na redu,broj, lista
            
            #for i in igraci_uigri: #postotak,koliko su puta vidili flop
                 #bio na stolu vise od 15 krugova, dovoljna statistika
                 #   if float(sum(popis_igraca[imena_igraca[i-1]][:6]))!=0 and popis_igraca[imena_igraca[i-1]][6]!=0:
                   #     vide_flop.append(float(sum(popis_igraca[imena_igraca[i-1]][:6]))/popis_igraca[imena_igraca[i-1]][6])
                 #       bet_raise2.append(bet_raise[i-1]) #statistike od igraca u igri
               #         check_call2.append(check_call[i-1]) #statistike od igraca u igri
               #         foldic2.append(foldic[i-1])
               #     else:
              #          vide_flop.append(0)
              #          bet_raise2.append(0)
             ##           check_call2.append(0)
            #            foldic2.append(0)
            #    else:
           #         vide_flop.append(0)
             #       bet_raise2.append(0)
             #       check_call2.append(0)
            #        foldic2.append(0)
        
            #for i in range(len(igraci_uigri)):
        pare_uigraca=[]
        for i in range(6):
            pare_uigraca.append(igraci.podaci(i+1,pom,pom2))    
        time.sleep(0.7) # izgleda ljudskije
        #print(popis_igraca0)

        igraci_statistika={} 
        for i in igraci_uigri:
            if popis_igraca[imena_igraca[i-1]][9]>30:
                igraci_statistika[imena_igraca[i-1]]=(korisna.statistika(popis_igraca,popis_igraca0,popis_igraca1,popis_igraca3,popis_igraca4,popis_igraca5,CB_igraca,imena_igraca,i))    
            else:
                igraci_statistika[imena_igraca[i-1]]=[0,0,0,0,0,0]
        if random.randint(1,2)<2:   #sigurni nacin igranja     
            situacija=umjetna4.inteligencija(card,jacina,znak,a,situacija,blinds,diz,button_gdje,vide_flop,pare_uigraca,bet_raise,check_call,foldic,vide_flop3,igraci_uigri,igraci_statistika,imena_igraca,ko_raisea)
        else: #slobodniji nacin igranja
            situacija=umjetna4_1.inteligencija(card,jacina,znak,a,situacija,blinds,diz,button_gdje,vide_flop,pare_uigraca,bet_raise,check_call,foldic,vide_flop3,igraci_uigri,igraci_statistika,imena_igraca)
        print('ovo je situacija',situacija)
        diz=0
            #print('nema flopa')
        
    
        #print('nisam na redu')
