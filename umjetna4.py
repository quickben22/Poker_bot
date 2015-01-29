import mis2
import ruka
import nastolu
import igraci
import vrsta2
import nastolu2

def inteligencija(card,jacina,znak,call,situacija2,blinds,diz,button_gdje,vide_flop,pare_uigraca,bet_raise2,check_call2,foldic2,vide_flop3,igraci_uigri,igraci_statistika,imena_igraca,ko_raisea):
    print('umjetna4')
    bjezi=0
    if card[2]>0:
        broj_prijemene=5-(button_gdje%6)
        if broj_prijemene==0:
            broj_prijemene=-5
    else:
        broj_prijemene=5-((button_gdje+2)%6)
        if broj_prijemene==0:
            broj_prijemene=-5
    zapomoc=[1,2,3,4,5]
    igraci_prijemene=zapomoc[-broj_prijemene:]
    uigri_prijemene=[]
    uigri_poslijemene=[]
    #print('igraci u igri',igraci_uigri)
    #print('igraci prije mene',igraci_prijemene)
    setic1=set(igraci_prijemene)
    setic2=set(igraci_uigri)
    setic3=setic1.intersection(setic2)
    setic4=setic2.difference(setic1)
    for i in range(len(setic3)): #igraci u igri prije mene
        uigri_prijemene.append(setic3.pop())
    for i in range(len(setic4)): #igraci u igri poslije mene
        uigri_poslijemene.append(setic4.pop())

   
    #print('uigri prije mene',uigri_prijemene)
    #print('uigri poslije mene',uigri_poslijemene)
    bet_raise3=[]
    check_call3=[]
    foldic3=[]
    vide_flop4=[]
    vrste_igraca=[] #vrste igraca prije mene
    pare_uigraca2=[] #pare u ugraca prije mena

    imena_prije=[]
    imena_poslije=[]
    
    for i in uigri_prijemene:
        #opasni_igrac_prije[imena_igraca[i-1]]=igraci_statistika[imena_igraca[i-1]]
        imena_prije.append(imena_igraca[i-1])
        bet_raise3.append(bet_raise2[i-1])
        check_call3.append(check_call2[i-1])
        foldic3.append(foldic2[i-1])
        vide_flop4.append(vide_flop3[i-1])
        vrste_igraca.append(vrsta2.igraca(bet_raise2[i-1],check_call2[i-1],foldic2[i-1],vide_flop3[i-1]))
        pare_uigraca2.append(pare_uigraca[i-1])
    bet_raise4=[]
    check_call4=[]
    foldic4=[]
    vide_flop5=[]
    vrste_igraca2=[] #vrste igraca poslije mene
    pare_uigraca3=[] #pare u ugraca prije mena
    for i in uigri_poslijemene:
        imena_poslije.append(imena_igraca[i-1]) #imena, koja sluze kao key, igraca prije, odnosno poslije mene
        #opasni_igrac_poslije[imena_igraca[i-1]]=igraci_statistika[imena_igraca[i-1]]
        bet_raise4.append(bet_raise2[i-1])
        check_call4.append(check_call2[i-1])
        foldic4.append(foldic2[i-1])
        vide_flop5.append(vide_flop3[i-1])
        vrste_igraca2.append(vrsta2.igraca(bet_raise2[i-1],check_call2[i-1],foldic2[i-1],vide_flop3[i-1]))
        pare_uigraca3.append(pare_uigraca[i-1])

    opasni_igrac=0
    opasni_igrac2=0
    opasni_igrac3=0
    opasni_pare=0
    opasni_pare2=0
    opasni_ime1='a'
    opasni_ime2='b'
    #print('igraci prije mene,vrsta',vrste_igraca)
    #print('igraci poslije mene,vrsta', vrste_igraca2)

    opasni_lista=[0,0,0,0,0,0]
    
    if len(vrste_igraca)>0:
        opasni_igrac=vrste_igraca[-1] #zadnji igrac prije mene, meni najblizi
        opasni_pare=pare_uigraca2[-1]
        opasni_ime1=imena_prije[-1]
    elif len(vrste_igraca2)>0: 
        opasni_igrac2=vrste_igraca2[-1] #zadnji igrac poslije mene, ako nema nikog prije mene, taj je najopasniji
        opasni_pare2=pare_uigraca3[-1]
        opasni_ime2=imena_poslije[-1]
    if opasni_igrac==0 and opasni_igrac2!=0:
        opasni_igrac=opasni_igrac2 # zadnji od onih poslije mene, postaje prvi prije mene(otprilike)
    if opasni_ime1=='a' and opasni_ime2!='b':
        opasni_ime1=opasni_ime2
    if opasni_pare==0 and opasni_pare2!=0:
        opasni_pare=opasni_pare2

    if len(igraci_statistika)>0 and opasni_ime1!='a':
        opasni_lista=igraci_statistika[opasni_ime1]
    #print('statisticka ',opasni_pare)
        print('opasni lista',opasni_lista)
        if (opasni_lista[0]==1 or opasni_lista[0]==2): #tight
            if opasni_lista[1]==1 or opasni_lista[1]==2: #passive
                opasni_igrac=2    
            elif opasni_lista[1]==3 or opasni_lista[1]==4: #aggresive
                opasni_igrac=3
            else:
                opasni_igrac=0
        elif (opasni_lista[0]==3 or opasni_lista[0]==4): #loose
            if opasni_lista[1]==1 or opasni_lista[1]==2: #passive
                opasni_igrac=4    
            elif opasni_lista[1]==3 or opasni_lista[1]==4: #aggresive
                opasni_igrac=1
            else:
                opasni_igrac=0
        else:
                opasni_igrac=0

    #print('opasni igrac== %d'%opasni_igrac )
    
    #velicina_pota=blinds
    #velicina_raisea=diz
    velicina_pota=blinds/5
    velicina_raisea=diz/5
    pare_uigraca2=pare_uigraca[:]
    blinds=int((blinds-diz)/2-1)#za 2/1 blindse
    if blinds%2==1:
	    blinds-=1
	
    #blinds=int((blinds-diz)/10-1)#za 10/5 blindse
    #button_gdje==6 BU, 5 SB, 4 BB, 3 UTG, 2 MP, 1 CO
    if velicina_raisea>0 and velicina_pota>0:
        postotak=float(velicina_raisea)/velicina_pota
        #print('postotak je %.2f'%postotak)
    else:
        postotak=0
    if len(vide_flop4)>0: # igraci prije mene
        vide_flop2=vide_flop4[:]
        opasnost=vide_flop2.pop()
        if opasnost==0:
            postotak+=0
        elif opasnost<0.2: #bjezi kud te noge nose
           bjezi=1 #skoro uopce ne igra, dakle bjezi
        elif opasnost<=0.3:
            postotak+=0.3 #ako na malo ruku dolazi, smanjit raise koji sam spreman pratit
        elif opasnost<=0.4:
            postotak+=0.2

    tri_od_boje=0
    jedan_za_skalu=0
    skala_dvije_strane=0
    stol2=[]
    stol2=nastolu2.sto(jacina,znak)[:]
    if stol2[1]==2:
        postotak+=0.3
        tri_od_boje=1
    if stol2[0]==20:
        postotak+=0.2
        jedan_za_skalu=1
    if stol2[0]==40:
        skala_dvije_strane=1
        postotak+=0.3

    
    
    isplati1=0 #rucni par,set ceka
    isplati2=0 #boju cekam
    isplati3=0 #skalu cekam
    isplati4=0 #2 overcard
    pare_umene=pare_uigraca[5]/5
    max_dobitak=opasni_pare/5
    #pare_umene=pare_uigraca[5]
    #max_dobitak=opasni_pare
    if pare_umene<max_dobitak:
        max_dobitak=pare_umene
        
    if (0.045*(max_dobitak+velicina_pota))>=(0.955*velicina_raisea):           #koliko se isplati pratit, za rucni par
        isplati1=1 #isplati se set cekat
    
    if (0.2*(max_dobitak+velicina_pota))>=(0.8*velicina_raisea):
        isplati2=1 #isplati se boju cekat
    if (0.175*(max_dobitak+velicina_pota))>=(0.825*velicina_raisea):
        isplati3=1 #isplati se skalu cekat
    if (0.13*(max_dobitak+velicina_pota))>=(0.87*velicina_raisea):
        isplati4=1 #isplati se sa 2 overcard cekat

    SPR=float(max_dobitak)/velicina_pota #  __________________SPR
    
    #print('glupost',((0.175*(max_dobitak+velicina_pota))-(0.825*velicina_raisea)))
    #print('postotak',postotak)
    
    situacija=0
    jacina2=[]
    jacina2=jacina[:]
    boja=0
    hand=ruka.koja(jacina2,znak,call)
    netreba_dizat=0
    tri_od_boje=0
    for i in vrste_igraca2:
        if i==1: # ako je igrac poslije mena LAG
            netreba_dizat=1

    blefirat=0
    zastavica_1=0
    if len(igraci_uigri)==2 and max(jacina[2:])<11: #nema visokih karata
        for i in vrste_igraca2:
            if i==2 or i==3:
                zastavica_1+=1
        for i in vrste_igraca:
            if i==2 or i==3:
                zastavica_1+=1
        if zastavica_1==2:
            blefirat=1 # ako su 2 igraca Tight,isplati se blefirat
    
    
    elif len(igraci_uigri)==1 and max(jacina[2:])<11:
        zastavica_1=0
        for i in vrste_igraca2:
            if i==2 or i==3 or i==4:
                zastavica_1+=1
        for i in vrste_igraca:
            if i==2 or i==3 or i==4:
                zastavica_1+=1
        if zastavica_1==1:
            blefirat=1 #igrac nije calling station

    if situacija2==1007:
        if len(igraci_uigri)==1:
            blefirat=1 #blefirat, da ili ne

    blefirat2=0 #drugi uvijet blefiranja, prije flopa
    brojilo=0
    if card[2]==0:
        
        if len(imena_prije)==0 and (call==1 or velicina_raisea<3):
            for i in imena_poslije:
                print('statistika_igraca1',igraci_statistika[i])
                if igraci_statistika[i][0]==1 or igraci_statistika[i][0]==2 or igraci_statistika[i][0]==5:
                    brojilo+=1
            
        if (len(imena_prije)+len(imena_poslije))==brojilo and (call==1 or velicina_raisea<3):
            blefirat2=1 #mozes blefirat
        else:
            blefirat2=0 #nemoj blefirat

    blefirat3=0
    brojilo=0
    if card[2]>0 and card[5]==0:
        for i in imena_prije:
            print('statistika_igraca2',igraci_statistika[i])
            if (igraci_statistika[i][4]!=1 and igraci_statistika[i][4]!=2 and igraci_statistika[i][4]!=3 and igraci_statistika[i][4]!=0):
                brojilo+=1

        for i in imena_poslije:
            print('statistika_igraca3',igraci_statistika[i])
            if (igraci_statistika[i][4]!=1 and igraci_statistika[i][4]!=2 and igraci_statistika[i][4]!=3 and igraci_statistika[i][4]!=0): 
                brojilo+=1


        if brojilo==(len(imena_prije)+len(imena_poslije)): #sve igraci koji ne dolaze previse od zadnje karte, mozes probat blef
            blefirat3=1
        else:
            blefirat3=0

    
    print('postotak: %.2f'%postotak)
    print('raise,pot,blefirat2,blefirat3',velicina_raisea, velicina_pota,blefirat2,blefirat3)

    visoke_karte=0
    for i in jacina[2:]:
        if i>9:
            visoke_karte+=1
    
    if max(card)==53:
        print('kriva detekcija karte,2 iste')
        if call==1:
            mis2.click(750,670) #call
            mis2.click(750,370) #makni ga sa gumb
            return 0
        elif call>1:
            mis2.click(630,670) #fold
            
            return 0

    
        
        
    elif jacina[2]==0: # prije flopa
        
        if (jacina[0]>10 and jacina[0]==jacina[1]) : #rucni par QQ ili vise+
            if netreba_dizat==1 and (velicina_raisea==2 or velicina_raisea==1) and call!=3: #ima LAG-a nakon mene
                mis2.click(750,670) #call
                mis2.click(750,370) #makni ga sa gumba
                print('call')
                situacija=1 #prva situacija
            else:
                for i in range(3):  #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                print('veliki raise')
                situacija=1 #prva situacija
        elif (jacina[0]+jacina[1])>24: # ak 
            if situacija2==2 and SPR>3 and call==2: #reraise i ima puno para covjek
                mis2.click(750,670) #call
                mis2.click(750,370) #makni ga sa gumba
                print('call')
                situacija=2002 #situacija u kojoj je covjek jako reraise i ima puno para


            else:
                for i in range(3):  #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                print('veliki raise')
                situacija=2 # druga situacija
        elif jacina[0]<11 and jacina[0]==jacina[1]: #mali rucni par, i srednji ako neko raise,samo call inace raise
            if call==2 and (velicina_raisea==2 or velicina_raisea==1):
                if jacina[0]>7:
                    for i in range(3):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                        
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    print('raise')
                    situacija=3 # treca situacija
                else:
                    for i in range(2):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                        
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    print('raise')
                    situacija=3 # treca situacija
            elif call==2 and (velicina_raisea<13 or postotak<0.40):
                mis2.click(750,670) #call
                mis2.click(750,370) #makni ga sa gumba
                print('call')
                situacija=103
            elif call==3 and (velicina_raisea<13 or postotak<0.60):
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                print('all in')
            elif call>1:
                mis2.click(630,670) #fold
                print('fold')
                
            elif call==1:
                if jacina[0]>7:
                    for i in range(3):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    print('raise')
                    situacija=3# treca situacija
                else:
                    for i in range(2):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    print('raise')
                    situacija=3# treca situacija
            elif call==3:
                if (velicina_raisea<13 or postotak<0.40):
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    print('all in')
                else:    
                    mis2.click(630,670) #fold
                    print('fold')

        elif bjezi==1 and velicina_raisea>6: #sigurusa maximalna
            if call==1:
                mis2.click(750,670) #call
                mis2.click(750,370) #makni ga sa gumba
                print('call')
                situacija=107
            else:
                mis2.click(630,670) #fold
                print('fold')
            
        elif len(igraci_uigri)<3 and (velicina_raisea==2 and velicina_raisea!=1 ) and button_gdje!=4 and button_gdje!=5 and blefirat2==1: # 2 ili manje ljudi u igri ostalo, ako je prazan stol, ovaj uvijet 
            for i in range(2):  #koliko puta raiseat
                mis2.click(1000,625) #raise jos
                    
            mis2.click(930,670) #raise velik gumb
            mis2.click(750,370) #makni ga sa gumba
            print('raise')
            situacija=1007# treca situacija    
            
        elif velicina_raisea==1 and len(igraci_uigri)==1 and blefirat2==1:
            for i in range(2):  #koliko puta raiseat
                mis2.click(1000,625) #raise jos
                    
            mis2.click(930,670) #raise velik gumb
            mis2.click(750,370) #makni ga sa gumba
            print('raise')
            situacija=1007# treca situacija
            
        elif button_gdje==3: #UTG
            
            if jacina[0]+jacina[1]>21 or (jacina[0]+jacina[1]>19 and jacina[0]==jacina[1]) :   #AJ do KJ  
                if velicina_raisea==2 or velicina_raisea==1 or call==1:          #u boji QT,K9,A8
                    for i in range(2):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    print('veliki raise')
                    situacija=1007
                elif velicina_raisea<13 or postotak<0.4:
                    if call==2:
                        mis2.click(750,670) #call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=107
                    elif call==3:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('all in')
                        
                elif call==1:
                    mis2.click(750,670) #call
                    mis2.click(750,370) #makni ga sa gumba
                    print('call')
                    situacija=107
                else:
                    mis2.click(630,670) #fold
                    print('fold')

            elif call==1:
                    mis2.click(750,670) #call
                    mis2.click(750,370) #makni ga sa gumba
                    print('call')
                    situacija=107
            
            else:
                
                mis2.click(630,670) #fold
                print('fold')

        elif button_gdje==2: #MP
           
            if (jacina[0]+jacina[1])>21:
                if velicina_raisea==2 or velicina_raisea==1 or call==1:                 #  A & J, A & T, K & Q KJ ne treba u boji
                    for i in range(2):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    print('veliki raise')
                    situacija=1007
                elif bjezi==1:
                    if call>1:
                        mis2.click(630,670) #fold
                        print('fold')
                    elif call==1:
                        mis2.click(750,670) #call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=107
                elif velicina_raisea<13 or postotak<0.4:
                    if call==2:
                        mis2.click(750,670) #call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=107
                    elif call==3:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('all in')
                    elif call==1:
                        mis2.click(750,670) #call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=107
                elif call==1:
                    mis2.click(750,670) #call
                    mis2.click(750,370) #makni ga sa gumba
                    print('call')
                    situacija=107
                else:
                    mis2.click(630,670) #fold
                    print('fold')       #A & 8, A & 9 i svasta drugo u boji do JT

            elif call==1:
                    mis2.click(750,670) #call
                    mis2.click(750,370) #makni ga sa gumba
                    print('call')
                    situacija=107
            elif call>1:
                    mis2.click(630,670) #fold
                    print('fold')       #A & 8, A & 9 i svasta drugo u boji do JT
        
                    
            elif znak[0]==znak[1] and (jacina[0]+jacina[1])>18:
                if velicina_raisea==2 or velicina_raisea==1  or call==1:                   
                    for i in range(2):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    print('veliki raise')
                    situacija=1007
                elif bjezi==1: # katastrofalno malo dolazi
                    if call>1:
                        mis2.click(630,670) #fold
                        print('fold')
                    elif call==1:
                        mis2.click(750,670) #call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=107    
                elif velicina_raisea<13 or postotak<0.4:
                    if call==2:
                        mis2.click(750,670) #call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=107
                    elif call==3:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('all in')
                    elif call==1:
                        mis2.click(750,670) #call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=107
                elif call==1:
                        mis2.click(750,670) #call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=107
                else:
                    mis2.click(630,670) #fold
                    print('fold')
            elif call==1:
                    mis2.click(750,670) #call
                    mis2.click(750,370) #makni ga sa gumba
                    print('call')
                    situacija=107
            else:
                mis2.click(630,670) #fold
                print('fold') 

        
        elif button_gdje==5: #SB
            if call==2 and velicina_raisea==1 and len(vrste_igraca)<1 and blefirat2==1: # nema nikog  prije mene
                for i in range(2):  #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                print('veliki raise')
                situacija=1007
            
            elif call==2 and velicina_raisea==1 and len(vrste_igraca)>=1:
                if (jacina[0]+jacina[1])>21  or (jacina[0]==9 and jacina[1]==12) or (jacina[0]==12 and jacina[1]==9) or (jacina[0]==10 and jacina[1]==11) or (jacina[0]==11 and jacina[1]==10) or (jacina[1]==9 and jacina[0]==10) or (jacina[1]==10 and jacina[0]==9) or (jacina[0]==11 and jacina[1]==9) or (jacina[0]==9 and jacina[1]==11) : #slike, nis posebno
                    for i in range(2):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    print('veliki raise')
                    situacija=1007
                elif ((jacina[0]+jacina[1])>17 or (jacina[0]==9 and jacina[1]==8) or (jacina[0]==8 and jacina[1]==9) or (jacina[0]==7 and jacina[1]==8) or (jacina[0]==8 and jacina[1]==7)) and znak[0]==znak[1] : #karte,u boji, a nis posebeno
                    for i in range(2):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    print('veliki raise')
                    situacija=1007
                else:
                    mis2.click(630,670) #fold
                    print('fold')
                    
            elif call==2 and len(vrste_igraca)>=1:
                if (jacina[0]+jacina[1])>21  or (jacina[0]==9 and jacina[1]==12) or (jacina[0]==12 and jacina[1]==9) or (jacina[0]==10 and jacina[1]==11) or (jacina[0]==11 and jacina[1]==10) or (jacina[1]==9 and jacina[0]==10) or (jacina[1]==10 and jacina[0]==9) or (jacina[0]==11 and jacina[1]==9) or (jacina[0]==9 and jacina[1]==11) : #slike, nis posebno
                    if bjezi==1: # katastrofalno malo dolazi
                        if call>1:
                            mis2.click(630,670) #fold
                            print('fold')
                        elif call==1:
                            mis2.click(750,670) #call
                            mis2.click(750,370) #makni ga sa gumba
                            print('call')
                            situacija=107  

                    elif (velicina_raisea<13 or postotak<0.40):
                        mis2.click(750,670) #call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=107 # karte slike, 4 situacija, isto kao sa kartama u boji igram, 4 zamjenio sa 107
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif ((jacina[0]+jacina[1])>17 or (jacina[0]==9 and jacina[1]==8) or (jacina[0]==8 and jacina[1]==9) or (jacina[0]==7 and jacina[1]==8) or (jacina[0]==8 and jacina[1]==7)) and znak[0]==znak[1] : #karte,u boji, a nis posebeno
                    if bjezi==1: # katastrofalno malo dolazi
                        if call>1:
                            mis2.click(630,670) #fold
                            print('fold')
                        elif call==1:
                            mis2.click(750,670) #call
                            mis2.click(750,370) #makni ga sa gumba
                            print('call')
                            situacija=107  


                    elif (velicina_raisea<13 or postotak<0.40):
                        mis2.click(750,670) #call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=107 # karte slike, 4 situacija, isto kao sa kartama u boji igram, 4 zamjenio sa 107
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                else:
                    mis2.click(630,670) #fold
                    print('fold')
            elif call==1:
                mis2.click(750,670) #call
                mis2.click(750,370) #makni ga sa gumba
                print('call')
                situacija=107
            elif call==3:
                if (velicina_raisea<5 or postotak<0.30):
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    print('all in')
                else:    
                    mis2.click(630,670) #fold
                    print('fold')
            else:
                mis2.click(630,670) #fold
                print('fold')
                                                                            
        elif (jacina[0]+jacina[1])>21  or (jacina[0]==9 and jacina[1]==12) or (jacina[0]==12 and jacina[1]==9) or (jacina[0]==10 and jacina[1]==11) or (jacina[0]==11 and jacina[1]==10) or (jacina[1]==9 and jacina[0]==10) or (jacina[1]==10 and jacina[0]==9) or (jacina[0]==11 and jacina[1]==9) or (jacina[0]==9 and jacina[1]==11) : #slike, nis posebno
            if call==3:                                                     #T & K                                                         # J i Q                                                                       J & T                                                                    Q & T                                                                                   
                if (velicina_raisea<20 or postotak<0.40):
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    print('all in')
                else:    
                    mis2.click(630,670) #fold
                    print('fold')
            elif call==2 and (velicina_raisea==2 or velicina_raisea==1): #fale uvijeti
                for i in range(2):  #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                print('veliki raise')
                situacija=1007

            elif bjezi==1: # katastrofalno malo dolazi
                if call>1:
                    mis2.click(630,670) #fold
                    print('fold')
                elif call==1:
                    mis2.click(750,670) #call
                    mis2.click(750,370) #makni ga sa gumba
                    print('call')
                    situacija=107  

            elif call==2 and (velicina_raisea<20 or postotak<0.40):
                mis2.click(750,670) #call
                mis2.click(750,370) #makni ga sa gumba
                print('call')
                situacija=107 # karte slike, 4 situacija, isto kao sa kartama u boji igram, 4 zamjenio sa 107
            elif call==2:
                mis2.click(630,670) #fold
                print('fold')
            elif call==1:
                for i in range(2):  #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                print('veliki raise')
                situacija=1007     
            elif call==1:
                mis2.click(750,670) #call
                mis2.click(750,370) #makni ga sa gumba
                print('call')
                situacija=107
                
        elif ((jacina[0]+jacina[1])>17 or (jacina[0]==9 and jacina[1]==8) or (jacina[0]==8 and jacina[1]==9) or (jacina[0]==7 and jacina[1]==8) or (jacina[0]==8 and jacina[1]==7)) and znak[0]==znak[1] : #karte,u boji, a nis posebeno
            if call==3: #all in foldam  #                               T & 9                                                               8 & 9
                if (velicina_raisea<13 or postotak<0.40):
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    print('all in')
                else:    
                    mis2.click(630,670) #fold
                    print('fold')
            elif bjezi==1: # katastrofalno malo dolazi
                if call>1:
                    mis2.click(630,670) #fold
                    print('fold')
                elif call==1:
                    mis2.click(750,670) #call
                    mis2.click(750,370) #makni ga sa gumba
                    print('call')
                    situacija=107  


            elif call==2 and (velicina_raisea==2 or velicina_raisea==1): #fale uvijeti
                for i in range(2):  #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                print('veliki raise')
                situacija=1007
            elif call==2 and (velicina_raisea<13 or postotak<0.40):
                mis2.click(750,670) #call
                mis2.click(750,370) #makni ga sa gumba
                print('call')
                situacija=107 # karte slike, 4 situacija, isto kao sa kartama u boji igram, 4 zamjenio sa 107
            elif call==2:
                mis2.click(630,670) #fold
                print('fold')
            elif call==1:
                for i in range(2):  #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                print('veliki raise')
                situacija=1007    
            elif call==1:
                mis2.click(750,670) #call
                mis2.click(750,370) #makni ga sa gumba
                print('call')
                situacija=107
                
        elif button_gdje==6 and call==2 and velicina_raisea==2 and len(vrste_igraca)==0 and blefirat2==1: #Button
            if situacija==1007 :
                if call<3 and velicina_raisea<3:
                    mis2.click(750,670) #call
                    mis2.click(750,370) #makni ga sa gumba
                    print('call')
                    situacija=107 # situacija 107 isto bolja za situaciju 5
                else:
                   
                    mis2.click(630,670) #fold
                    print('fold')
                    
            else:
                for i in range(2):  #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                print('veliki raise')
                situacija=1007
        elif call==2 and velicina_raisea==1:
            mis2.click(750,670) #call
            mis2.click(750,370) #makni ga sa gumba
            print('call')
            situacija=107 # situacija 107 isto bolja za situaciju 5
            
        elif call==1: #nemam nis, ali mogu cekirat
            mis2.click(750,670) #call
            mis2.click(750,370) #makni ga sa gumba
            print('call')
            situacija=107 # situacija 107 isto bolja za situaciju 5
        else:
            mis2.click(630,670) #fold
            print('fold')
        
            

    elif jacina[2]>0 and jacina[5]==0: # na flopu
        if situacija2==1 or situacija2==6 or situacija2==7 or situacija2==8: #prva situacija (veliki rucni par)
            hand=ruka.koja(jacina2,znak,call)# trenutno imam
            if hand>=3 and opasni_igrac!=1 and opasni_igrac!=3: #dobio set ili ful, slow-play za sve osim LAG-a i TAG-a
                for i in range(blinds/2):  #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                    
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                print('veliki raise')
                situacija=6
            elif hand>=3: #LAG igrac, pretvorit se u calling station
                if call==2:
                    mis2.click(750,670) #call
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=6
                    print('call')    
                elif call==3:
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    print('all in')
                    situacija=6
                elif call==1:
                    mis2.click(750,670) #call
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=6
                    print('check') 
                
            elif jacina[1]>=max(jacina[2:]): #nema karte jace od mojeg rucnog para,dizi ko lud
                for i in range(blinds):  #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                    
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                print('veliki raise')
                situacija=7
            elif call==1 and jacina[1]<=max(jacina[2:]): #ima jacih karata na flopu,niko nije raise,lagani raise
                for i in range(blinds/2):  #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                    
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                print('lagani raise')
                situacija=8
            elif call==2 and jacina[1]<=max(jacina[2:]) and (isplati1==1 or opasni_igrac==1):
                mis2.click(750,670) #call
                mis2.click(750,370) #makni ga sa gumba
                situacija=8
                print('call')
            elif call==3 and jacina[1]<=max(jacina[2:]) and isplati1==1:
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                print('allin')
                situacija=8
            elif call>1 and jacina[1]<=max(jacina[2:]): #neko je raisea-o,begaj
                mis2.click(630,670) #fold
                print('fold')
                
        elif situacija2==2 or situacija2==9 or situacija2==10: #druga situacija, aq,ak
            hand=ruka.koja(jacina2,znak,call)
            if hand>=2 and opasni_igrac!=1 and opasni_igrac!=3: #slow play na aggresive players
                for i in range(blinds/2):  #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                situacija=9
                print('veliki raise')
            elif hand>=2:
                if call==2:
                    mis2.click(750,670) #call
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=9
                    print('call')    
                elif call==3:
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    print('all in')
                    situacija=9
                elif call==1:
                    mis2.click(750,670) #call
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=9
                    print('check')     
            elif hand==1 and (jacina[0]+jacina[1])==24 and call>1: #aq imam,pajdo na moj raise raisea ili allina, provjerit dali je najjaci par
                if jacina.count(11)==2 and 11<max(jacina[2:]): #dama se uparila, ali na flopu je kralj
                    if postotak>0.5:
                        mis2.click(630,670) #fold
                        print('fold')
                    elif postotak<=0.5 and (opasni_igrac!=3 or opasni_igrac!=2): # 2 tight
                        mis2.click(750,670) #call
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=10
                        print('call')
                else: #na flopu nema kralja, ili se as upario, dakle najjaci par na flopu sa aq, do kraja
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba    
                    situacija=9
            elif hand==1: #sigurno najjaci par
                for i in range(blinds):  #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                situacija=9
                print('veliki raise')

            elif znak[0]==znak[1] and znak[2:].count(znak[0])>=2: #cekam boju, ali nemam nista, raise do kraja
                for i in range(blinds/2):  #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                situacija=109 # situacija od obicnih karata sa bojom
                print('veliki raise')
            elif call==1 and opasni_igrac!=4 and situacija2!=2002: #calling donkey
                for i in range(blinds/2):  #koliko puta raiseat #ako je pajdo reraise i ima puno para=2002
                    mis2.click(1000,625) #raise jos
                    
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                situacija=10
                print('raise')
            elif call==1:
                mis2.click(750,670) #call
                mis2.click(750,370) #makni ga sa gumba
                situacija=10
                print('call')
            elif call==2 and isplati4==1: #isplati se 6 karata cekat, 2 overcard
                mis2.click(750,670) #call
                mis2.click(750,370) #makni ga sa gumba
                situacija=10
                print('call')
            elif call==3 and isplati4==1:
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                situacija=10
                print('allin')
            elif call==2:
                mis2.click(630,670) #fold
                print('fold')
                
            elif call==3:
                mis2.click(630,670) #fold
                print('fold')
                
                
        elif situacija2==3 or situacija2==103 or situacija2==11 or situacija2==12: #treca situacija, mali rucni par
            hand=ruka.koja(jacina2,znak,call)


            if hand>2 and opasni_igrac!=1 and opasni_igrac!=3 and situacija2!=103: #slow playat ovo dvoje
                for i in range(blinds/2):  #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                print('veliki raise')
                situacija=11
            elif hand>2:
                if call==2:
                    mis2.click(750,670) #call
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=11
                    print('call')    
                elif call==3:
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    print('all in')
                    situacija=11
                elif call==1:
                    mis2.click(750,670) #call
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=11
                    print('check')
                    
            elif jacina[0]>=max(jacina):
                for i in range(blinds):  #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                print('veliki raise')
                situacija=1200
            elif call==1 and len(vrste_igraca2)==0 and opasni_igrac!=4 and visoke_karte<2 : #nemam par,ali svi chekirali, i ne smije biti calling station
                for i in range(blinds/2):  #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                            
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                situacija=1200
                print('raise')
            elif call==1:
                mis2.click(750,670) #call
                mis2.click(750,370) #makni ga sa gumba
                situacija=12
                print('call')
            elif call==1 and situacija2==3: #raiseo sam prije flopa
                for i in range(blinds/2):  #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                            
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                situacija=1200
                print('raise')
            elif call>1 and isplati1==0:
                mis2.click(630,670) #fold
                print('fold')
            elif call==2:
                mis2.click(750,670) #call
                mis2.click(750,370) #makni ga sa gumba
                situacija=12
                print('call')
            elif call==3:
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                situacija=12
                print('allin')
                
        elif situacija2==4 or situacija2==13 or situacija2==14 or situacija2==15 or situacija2==104: # cetvrta situacija, glupe slike
            hand=ruka.koja(jacina2,znak,call)
            if hand>1: # 2 para i vise
                for i in range(blinds):  #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                    
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                situacija=13
                print('veliki raise')
            elif hand==1 and call>1: #neko raisea, ja samo par
                if call==3: # fold na all in
                    if jacina[0]>=max(jacina[2:]) or jacina[1]>=max(jacina[2:]): # najjaci par imam(ne mora biti u slucaju At ili Aj ili Kj), call
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=0
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                else:
                    mis2.click(750,670) #call
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=14
                    print('call')
            elif hand==1 and call==1: #niko ne raise, ja imam par, raise
                for i in range(blinds):  #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                    
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                situacija=104
                print('raise')
            elif znak[0]==znak[1] and znak[2:].count(znak[0])>=2: #cekam boju, ali nemam nista, raise do kraja
                for i in range(blinds):  #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                situacija=109 # situacija od obicnih karata sa bojom
                print('veliki raise')
            
            
            elif call==1: #niko ne raise,ja nemam nis, check
                mis2.click(750,670) #call
                mis2.click(750,370) #makni ga sa gumba
                situacija=15
                print('call')
            elif call>1: #raise, a ja nista nemam
                mis2.click(630,670) #fold
                print('fold')

        elif situacija2==107 or situacija2==1007 or situacija2==108 or situacija2==109 or situacija2==110 or situacija2==111: #karte u boji
            hand=ruka.koja(jacina2,znak,call)
            boja=0
           
            
            if znak[0]==znak[1]: # dodatak jer sam situaciju slika izjednacio sa kartama u boji
                
                for i in range(4):
                    if znak.count(i+1)>3:
                        boja=1 # 4 od boje su na stolu
                        break
                    else:
                        boja=0
            #print(boja,znak)
            if hand<3 and bjezi==1: #mega opasnost
                if call==1: #niko ne raise,ja nemam nis, check
                    mis2.click(750,670) #call
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=113
                    print('call')
                elif call>1: #raise, a ja nista nemam
                    mis2.click(630,670) #fold
                    print('fold')

            elif hand>=2 and (situacija2==107 or situacija2==1007) and len(vrste_igraca2)!=0 and call==1: #neko je drugi raise prije flopa
                 #niko ne raise,ja nemam nis, check
                    mis2.click(750,670) #call
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=108
                    print('call')
                
            elif hand>2 and opasni_igrac!=3 and opasni_igrac!=1: # 2 para i vise, nek se dize, svima osim aggresive players
                for i in range(blinds/2):  #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                    
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                situacija=108
                print('veliki raise')
            elif hand>2:
                if call==2:
                    mis2.click(750,670) #call
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=108
                    print('call')    
                elif call==3:
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    print('all in')
                    situacija=108
                elif call==1:
                    mis2.click(750,670) #call
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=108
                    print('check')    
            elif hand==2 and jacina[2:].count(jacina[2])==1 and jacina[2:].count(jacina[3])==1 :
                #2 prava para
                for i in range(blinds):  #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                    
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                situacija=108
                print('veliki raise')
                
            elif boja==1: # 4 od boje na stolu
                if (situacija2==107 or situacija2==1007 or SPR<3):
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=109
                    print('veliki raise')
                elif call==1:
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=109
                    print('veliki raise')
                elif call==2 and situacija2==109: #bio reraise
                    mis2.click(750,670) #call
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=109
                    print('call')
                elif call==3:
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=109
                    print('all in')
                else:
                    mis2.click(630,670) #fold
                    print('fold')
            elif hand==-1: #skala sa 2 strane
                if (situacija2==107 or situacija2==1007 or SPR<3):
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=109
                    print('veliki raise')
                elif call==1:
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=109
                    print('veliki raise')
                elif call==2 and situacija2==109: #bio reraise
                    mis2.click(750,670) #call
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=109
                    print('call')
                elif call==3:
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=109
                    print('all in')
                else:
                    mis2.click(630,670) #fold
                    print('fold')
                    
            elif (hand==1 or hand==2) and call==1: #imam najjaci par, niko raise
                if jacina.count(jacina[0])>1: #prva karta se uparila


                   

                    if jacina[0]>=max(jacina[2:]): #najjaci par na stolu imam,niko nije raise  raise
                        for i in range(blinds):  #koliko puta raiseat
                            mis2.click(1000,625) #raise jos
                            
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=110
                        print('raise')
                        
                    elif call==1 and len(vrste_igraca2)==0 and blefirat3==1: #nemam najjaci par,ali imam par, svi chekirali
                        for i in range(blinds/2):  #koliko puta raiseat
                            mis2.click(1000,625) #raise jos
                            
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=111
                        print('raise')
                    elif call==1 and blefirat==1 and blefirat3==1:
                        for i in range(blinds/2):  #koliko puta raiseat
                            mis2.click(1000,625) #raise jos
                            
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=111
                        print('raise')
                    elif call==1: #nemam najjaci par,ali imam par
                        mis2.click(750,670) #call
                        mis2.click(750,370) #makni ga sa gumba
                    #    print('1')
                        situacija=111
                        print('call')
                    elif call==2 and postotak<0.3: #mini raise call sa 1 parom
                        mis2.click(750,670) #call
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=111
                        print('call')
                    elif call>1:
                        mis2.click(630,670) #fold
                        mis2.click(750,370) #makni ga sa gumba
                        print('fold')
                    
                elif jacina.count(jacina[1])>1:#druga karta se uparila
                    if jacina[1]>=max(jacina[2:]): #najjaci par na stolu imam, niko nije raise , raise
                        for i in range(blinds):  #koliko puta raiseat
                            mis2.click(1000,625) #raise jos
                            
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('raise')
                        situacija=110 # dvije iste situacija
                    elif call==1 and len(vrste_igraca2)==0 and blefirat3==1: #nemam najjaci par,ali imam par, svi chekirali
                        for i in range(blinds/2):  #koliko puta raiseat
                            mis2.click(1000,625) #raise jos
                            
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=111
                        print('raise')
                    elif call==1 and blefirat==1 and blefirat3==1:
                        for i in range(blinds/2):  #koliko puta raiseat
                            mis2.click(1000,625) #raise jos
                            
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=111
                        print('raise')
                    elif call==1: #nemam najjaci par,ali imam par
                        mis2.click(750,670) #call
                        mis2.click(750,370) #makni ga sa gumba
                    #    print('1')
                        situacija=111
                        print('call')
                    elif call==2 and postotak<0.3: #mini raise call sa 1 parom
                        mis2.click(750,670) #call
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=111
                        print('call')
                    elif call>1:
                        mis2.click(630,670) #fold
                        mis2.click(750,370) #makni ga sa gumba
                        print('fold')
                        
                else:
                    mis2.click(750,670) #call
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=111
                   # print('3')
                    print('call')


            elif (hand==1 or hand==2) and call>1: #imam najjaci par, neko raise
                if jacina.count(jacina[0])>1: #prva karta se uparila
                    if jacina[0]>=max(jacina[2:]) and postotak<0.51 and (opasni_igrac!=2 and opasni_igrac!=3): #najjaci par na stolu imam, call na njegov raise
                                                                          #treba provjeravat sto je na flopu... mozda...                  
                         

                        if situacija2==111 or situacija2==110: #neko reraise, ne zanima me, fold

                            if call==3 and postotak<0.45:
                                mis2.click(930,670) #raise velik gumb
                                mis2.click(750,370) #makni ga sa gumba
                                situacija=111
                                print('allin')
                            elif call==2 and (postotak<0.35 or SPR<1.5): #mali reraise dolazimo
                                mis2.click(750,670) #call
                                mis2.click(750,370) #makni ga sa gumba
                                situacija=110
                                print('call')
                            elif call>1:
                                mis2.click(630,670) #fold
                                mis2.click(750,370) #makni ga sa gumba
                                print('fold')
                            
                        elif call==2 and situacija2==1007: #nije reraise
                            if postotak<0.3: #jako mali raise neko napravio
                                for i in range(blinds/2):  #koliko puta raiseat
                                    mis2.click(1000,625) #raise jos
                                    
                                mis2.click(930,670) #raise velik gumb
                                mis2.click(750,370) #makni ga sa gumba
                                situacija=111
                                print('raise')    
                           
                        
                            elif call==3 and situacija2==1007 and postotak<0.6:
                                mis2.click(930,670) #raise velik gumb
                                mis2.click(750,370) #makni ga sa gumba
                                print('all in')
                            else:    
                                mis2.click(750,670) #call
                                mis2.click(750,370) #makni ga sa gumba
                                situacija=110
                                print('call')
                                
                        elif call==2 and postotak<0.45:
                            mis2.click(750,670) #call
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=110
                            print('call')
                        elif call==2:
                            mis2.click(630,670) #fold
                            mis2.click(750,370) #makni ga sa gumba
                            print('fold')
                        elif call==3 and postotak<0.45:
                            mis2.click(930,670) #raise velik gumb
                            mis2.click(750,370) #makni ga sa gumba
                            print('all in')
                        else:
                            mis2.click(630,670) #fold
                            mis2.click(750,370) #makni ga sa gumba
                            print('fold')
                    elif call==1: #nemam najjaci par
                        mis2.click(750,670) #call
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=111
                    #    print('4')
                        print('call')
                    elif call>1 and (opasni_igrac==2 or opasni_igrac==3): #drugi par bacam na rajse, to bi mozda trebalo promjenit ovisno o igracima
                        mis2.click(630,670) #fold
                        mis2.click(750,370) #makni ga sa gumba
                        print('fold')
                    elif call==2 and (opasni_igrac==1) and postotak<0.51: #LAG player, taj dize na svasta
                        mis2.click(750,670) #call
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=111
                    #    print('4')
                        print('call')
                    elif call==2 and postotak<0.26:
                        mis2.click(750,670) #call
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=111
                    
                        print('call')
                    else:
                        mis2.click(630,670) #fold
                        mis2.click(750,370) #makni ga sa gumba
                        print('fold')
                    
                elif jacina.count(jacina[1])>1:#druga karta se uparila
                    if jacina[1]>=max(jacina[2:]) and postotak<0.51 and (opasni_igrac!=2 and opasni_igrac!=3): #najjaci par na stolu imam, neko je raise, call

                                                              #ne smije biti tight player

                        if situacija2==111 or situacija2==110: #neko reraise, ne zanima me, fold

                            if call==3 and postotak<0.35:
                                mis2.click(930,670) #raise velik gumb
                                mis2.click(750,370) #makni ga sa gumba
                                situacija=111
                                print('allin')
                            elif call==2 and (postotak<0.35 or SPR<1.5): #mali reraise dolazimo
                                mis2.click(750,670) #call
                                mis2.click(750,370) #makni ga sa gumba
                                situacija=110
                                print('call')
                            elif call>1:
                                mis2.click(630,670) #fold
                                mis2.click(750,370) #makni ga sa gumba
                                print('fold')
                    
                        elif call==2 and situacija2==1007: #nije reraise
                            if postotak<0.3: #jako mali raise neko napravio
                                for i in range(blinds/2):  #koliko puta raiseat
                                    mis2.click(1000,625) #raise jos
                                    
                                mis2.click(930,670) #raise velik gumb
                                mis2.click(750,370) #makni ga sa gumba
                                situacija=111
                                print('raise')    
                           
                            elif call==3 and situacija2==1007:
                                mis2.click(930,670) #raise velik gumb
                                mis2.click(750,370) #makni ga sa gumba
                                print('all in')

                            else:    
                                mis2.click(750,670) #call
                                mis2.click(750,370) #makni ga sa gumba
                                situacija=110
                                print('call')
                        elif call==2 and postotak<0.45:
                            mis2.click(750,670) #call
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=110
                            print('call')
                        elif call==3 and postotak<0.45:
                            mis2.click(930,670) #raise velik gumb
                            mis2.click(750,370) #makni ga sa gumba
                            print('all in')
                        elif call==2:
                            mis2.click(630,670) #fold
                            mis2.click(750,370) #makni ga sa gumba
                            print('fold')
                        else:
                            mis2.click(630,670) #fold
                            mis2.click(750,370) #makni ga sa gumba
                            print('fold')
                    elif call==1: #nemam najjaci par
                        mis2.click(750,670) #call
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=111
                      #  print('5')
                        print('call')
                    elif call==2 and (opasni_igrac==1) and postotak<0.41: #drugi par bacam na rajse, to bi mozda trebalo promjenit ovisno o igracima
                        mis2.click(750,670) #call
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=111
                    #    print('4')
                        print('call')
                    elif call==2 and postotak<0.26:
                        mis2.click(750,670) #call
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=111
                    
                        print('call')
                    else:
                        mis2.click(630,670) #fold
                        mis2.click(750,370) #makni ga sa gumba
                        print('fold')
                        
                else:
                    mis2.click(750,670) #call
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=111
                   # print('6')
                    print('call')
                    
            elif call==1 and len(vrste_igraca2)==0 and opasni_igrac!=4 and blefirat3==1: #nemam par,ali svi chekirali, i ne smije biti calling station
                for i in range(blinds/2):  #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                            
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                situacija=111
                print('raise')
            elif call==1 and blefirat==1 and blefirat3==1:
                for i in range(blinds/2):  #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                            
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                situacija=111
                print('raise')

            elif call==1: #nemam nis
                mis2.click(750,670) #call
                mis2.click(750,370) #makni ga sa gumba
                    #    print('1')
                situacija=111
                print('call')


            elif call==2 and situacija2==1007 and postotak<0.26: #nije reraise, a ja raise prije flopa
                 #jako mali raise neko napravio
                for i in range(blinds/2):  #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                                    
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                situacija=111
                print('raise')
            elif call>1:
                mis2.click(630,670) #fold
                mis2.click(750,370) #makni ga sa gumba
                print('fold')
                
           

                
                
        elif situacija2==5 or situacija2==16 or situacija2==17 or situacija2==105 or situacija2==106: #peta situacija, lose karte, besplatni flop
            hand=ruka.koja(jacina2,znak,call)
            if hand>1: # 2 para i vise
                for i in range(blinds):  #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                    
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                situacija=16
                print('veliki raise')
                #print(hand)
            elif hand==1: #imam par, neko raise
                if jacina.count(jacina[0])>1: #prva karta se uparila
                    if jacina[0]>=max(jacina[2:]): #najjaci par na stolu imam, niko nije raise prije flopa, raise
                        for i in range(blinds):  #koliko puta raiseat
                            mis2.click(1000,625) #raise jos
                            
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=105
                        print('raise')
                   
                    elif call==1: # nista ili par, niko ne raisea
                        mis2.click(750,670) #call
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=17
                        #print('prvi')
                        print('call')
                    elif call>1:
                        mis2.click(630,670) #fold
                        mis2.click(750,370) #makni ga sa gumba
                        print('fold')
                        
                elif jacina.count(jacina[1])>1:#druga karta se uparila
                    if jacina[1]>=max(jacina[2:]): #najjaci par na stolu imam, niko nije raise prije flopa, raise
                        for i in range(blinds):  #koliko puta raiseat
                            mis2.click(1000,625) #raise jos
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=106
                        print('veliki raise')
                    elif call==1: # nista ili par, niko ne raisea
                        mis2.click(750,670) #call
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=17
                        #print('drugi')
                        print('call')
                    elif call>1:
                        mis2.click(630,670) #fold
                        mis2.click(750,370) #makni ga sa gumba
                        print('fold')
                else:
                    if call==1:
                        mis2.click(750,670) #call
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=17
                        #print('treci')
                        print(jacina)
                        print('call')    
                    elif call>1:
                        mis2.click(630,670) #fold
                        mis2.click(750,370) #makni ga sa gumba
                        print('fold')
                
            elif call==1: # nista ili par, niko ne raisea
                mis2.click(750,670) #call
                mis2.click(750,370) #makni ga sa gumba
                situacija=17
                print('call')
            elif call>1:
                mis2.click(630,670) #fold
                mis2.click(750,370) #makni ga sa gumba
                print('fold')

                
#-----_________________________________________________________________________________________________



            
    elif jacina[5]>0 and jacina[6]==0: #            4 karte dole
        if situacija2==6 or situacija2==18 : # imam set ili ful, nastavi dizat, sa rucnim parom
            hand=ruka.koja(jacina2,znak,call)
            karte_stol=nastolu.sto(jacina,znak)
            if karte_stol==4 or karte_stol==5 or karte_stol==1:
                if hand<3:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=18
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand==3:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=18
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=18
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand==4 and karte_stol<4: #skala i nema 4 of boje
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=18
                    print('veliki raise') #  idemo do kraja
                elif hand==4 and karte_stol>3:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=18
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=18
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand>4:
                        for i in range(blinds):  #koliko puta raiseat
                            mis2.click(1000,625) #raise jos
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=18
                        print('veliki raise') #  idemo do kraja
                    
                        
                else:
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=18
                    print('veliki raise') #  idemo do kraja

            else:
                for i in range(blinds):  #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                    
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                situacija=18
                print('veliki raise')
            
        elif situacija2==7 or situacija2==19 or situacija2==20 or situacija2==21: #nije bilo karte jace od mojeg rucnog para,dizo ko lud
            hand=ruka.koja(jacina2,znak,call)
            karte_stol=nastolu.sto(jacina,znak)
            if karte_stol==4 or karte_stol==5 or karte_stol==1: #4 od skale ili 4 od boje
                if hand==2 and jacina[2:].count(jacina[2])==1 and jacina[2:].count(jacina[3])==1 and jacina[2:].count(jacina[4])==1 and jacina[2:].count(jacina[5])==1 and jacina[2:].count(jacina[6])==1: 
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=21
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=21
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand<3:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=21
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand==3:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=21
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=21
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand==4 and karte_stol<4: #skala i nema 4 of boje
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=21
                    print('veliki raise') #  idemo do kraja
                elif hand==4 and karte_stol>3:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=21
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=21
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand>4:
                        for i in range(blinds):  #koliko puta raiseat
                            mis2.click(1000,625) #raise jos
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=21
                        print('veliki raise') #  idemo do kraja
                    
                        
                else:
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=21
                    print('veliki raise') #  idemo do kraja



            elif hand>=3: #dobio set ili vise, raise ko lud
                for i in range(blinds):  #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                    
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                situacija=19
                print('veliki raise')
            elif jacina[1]>=max(jacina[2:]): #nije dosla karta veca od mog rucnog,nastavi raise
                for i in range(blinds):  #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                    
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                situacija=20
                print('veliki raise')
            elif jacina[1]<max(jacina[2:]) and call==1: #dosla je veca, ali niko ne raise
                for i in range(blinds):  #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                    
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                situacija=21
                print('raise')
            elif jacina[1]<max(jacina[2:]) and call==2 and postotak<0.31:
                mis2.click(750,670) # call
                mis2.click(750,370) #makni ga sa gumba
                print('call')
                situacija=21
            elif jacina[1]<max(jacina[2:]) and call==3 and postotak<0.31:
                mis2.click(930,670) #raise velik gum
                mis2.click(750,370) #makni ga sa gumba
                situacija=21
                print('all in')
            elif jacina[1]<max(jacina[2:]) and call>1: #dosla je veca i neko raise,begaj
                mis2.click(630,670) # fold
               
                print('fold')

        elif situacija2==8 or situacija2==22 or situacija2==23: ##, ja rucni par ,ima jacih karata na flopu,niko nije raise,lagani raise
            hand=ruka.koja(jacina2,znak,call)
            karte_stol=nastolu.sto(jacina,znak)
            if karte_stol==4 or karte_stol==5 or karte_stol==1:
                if hand==2 and jacina[2:].count(jacina[2])==1 and jacina[2:].count(jacina[3])==1 and jacina[2:].count(jacina[4])==1 and jacina[2:].count(jacina[5])==1 and jacina[2:].count(jacina[6])==1: 
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=22
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=22
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand<3:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=22
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand==3:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=22
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=22
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand==4 and karte_stol<4: #skala i nema 4 of boje
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=23
                    print('veliki raise') #  idemo do kraja
                elif hand==4 and karte_stol>3:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=22
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=22
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand>4:
                        for i in range(blinds):  #koliko puta raiseat
                            mis2.click(1000,625) #raise jos
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=23
                        print('veliki raise') #  idemo do kraja
                    
                        
                else:
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=23
                    print('veliki raise') #  idemo do kraja



            if hand>=3: #dobio set ili vise, raise ko lud
                for i in range(blinds):  #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                    
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                situacija=22
                print('veliki raise')
                
            elif call==1: #check
                mis2.click(750,670) # call
                mis2.click(750,370) #makni ga sa gumba
                print('call')
                situacija=23
            elif call==2 and postotak<0.32: #check
                mis2.click(750,670) # call
                mis2.click(750,370) #makni ga sa gumba
                print('call')
                situacija=23
            elif call==3 and postotak<0.32: #check
                mis2.click(750,670) # call
                mis2.click(750,370) #makni ga sa gumba
                print('call')
                situacija=23
            
            
            elif call>1:
                mis2.click(630,670) #fold
                print('fold')


        elif situacija2==9 or situacija2==24 : #aq,ak, dobio par, ide se do kraja, je nije
            karte_stol=nastolu.sto(jacina,znak)
            if karte_stol==4 or karte_stol==5 or karte_stol==1:
                if hand==2 and jacina[2:].count(jacina[2])==1 and jacina[2:].count(jacina[3])==1 and jacina[2:].count(jacina[4])==1 and jacina[2:].count(jacina[5])==1 and jacina[2:].count(jacina[6])==1: 
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=24
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=24
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
        
                elif hand<3:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=24
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand==3:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=24
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=24
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand==4 and karte_stol<4: #skala i nema 4 of boje
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=24
                    print('veliki raise') #  idemo do kraja
                elif hand==4 and karte_stol>3:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=24
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=24
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand>4:
                        for i in range(blinds):  #koliko puta raiseat
                            mis2.click(1000,625) #raise jos
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=24
                        print('veliki raise') #  idemo do kraja
                    
                        
                else:
                    
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=24
                    print('veliki raise') #  idemo do kraja

            else:
                for i in range(blinds):  #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                    
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                situacija=24
                print('veliki raise')

        elif situacija2==10 or situacija2==25 or situacija2==26: #nista na flopu, pratio moj raise, ak,aq imam
            hand=ruka.koja(jacina2,znak,call)
            karte_stol=nastolu.sto(jacina,znak)
            if znak[0]==znak[1]: # dodatak jer sam situaciju slika izjednacio sa kartama u boji
                

                if znak.count(znak[0])>3:
                    boja=1 # 4 od boje su na stolu
                else:
                    boja=0


            if karte_stol==4 or karte_stol==5 or karte_stol==1:
                if hand==2 and jacina[2:].count(jacina[2])==1 and jacina[2:].count(jacina[3])==1 and jacina[2:].count(jacina[4])==1 and jacina[2:].count(jacina[5])==1 and jacina[2:].count(jacina[6])==1: 
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=26
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=26
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')

                elif hand<3:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=26
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand==3:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=26
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=26
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand==4 and karte_stol<4: #skala i nema 4 of boje
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=25
                    print('veliki raise') #  idemo do kraja
                elif hand==4 and karte_stol>3:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=26
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=26
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand>4:
                        for i in range(blinds):  #koliko puta raiseat
                            mis2.click(1000,625) #raise jos
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=25
                        print('veliki raise') #  idemo do kraja
                    
                        
                else:
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=25
                    print('veliki raise') #  idemo do kraja
                    
            elif hand>=1: #ak dobim par,veliki raise do kraja
                for i in range(blinds):  #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                    
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                situacija=25
                print('veliki raise')
            elif call==1 and (len(vrste_igraca2)==0 or len(vrste_igraca)==1): # nemam nis, ali svi su chekirali ili je 1 u igri
                for i in range(blinds/2):  #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                    
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                situacija=26
                print('veliki raise')
    
            elif call==1:
                mis2.click(750,670) # call
                mis2.click(750,370) #makni ga sa gumba
                print('call')
                situacija=26
            elif call==2 and boja==1 and postotak<0.4:
                mis2.click(750,670) # call
                mis2.click(750,370) #makni ga sa gumba
                print('call')
                situacija=26
            elif call==2 and postotak<0.23:
                mis2.click(750,670) # call
                mis2.click(750,370) #makni ga sa gumba
                print('call')
                situacija=26
            elif call==3 and boja==1 and postotak<0.4:
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                situacija=26
                print('veliki raise')
            elif call==3 and postotak<0.23:
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                situacija=26
                print('veliki raise')
                
            elif call>1: #nis nemam, ak raise fold
                mis2.click(630,670) #fold
                print('fold')

        elif situacija2==11 or situacija2==27: #mali rucni par+set
            karte_stol=nastolu.sto(jacina,znak)
            if karte_stol==4 or karte_stol==5 or karte_stol==1:
                if hand==2 and jacina[2:].count(jacina[2])==1 and jacina[2:].count(jacina[3])==1 and jacina[2:].count(jacina[4])==1 and jacina[2:].count(jacina[5])==1 and jacina[2:].count(jacina[6])==1: 
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=27
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=27
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')

                elif hand<3:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=27
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand==3:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=27
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=27
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand==4 and karte_stol<4: #skala i nema 4 of boje
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=27
                    print('veliki raise') #  idemo do kraja
                elif hand==4 and karte_stol>3:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=27
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=27
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand>4:
                        for i in range(blinds):  #koliko puta raiseat
                            mis2.click(1000,625) #raise jos
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=27
                        print('veliki raise') #  idemo do kraja
                    
                        
                else:
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=27
                    print('veliki raise') #  idemo do kraja

            
            else:
                for i in range(blinds):  #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                situacija=27
                print('veliki raise')
            
        elif situacija2==12 or situacija2==1200 or situacija2==28 or situacija2==29: #mali rucni par, niko nije raise
            hand=ruka.koja(jacina2,znak,call)

            karte_stol=nastolu.sto(jacina,znak)
            if karte_stol==4 or karte_stol==5 or karte_stol==1:

                if hand==2 and jacina[2:].count(jacina[2])==1 and jacina[2:].count(jacina[3])==1 and jacina[2:].count(jacina[4])==1 and jacina[2:].count(jacina[5])==1 and jacina[2:].count(jacina[6])==1: 
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=28
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=28
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand<3:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=28
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand==3:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=28
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=28
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand==4 and karte_stol<4: #skala i nema 4 of boje
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=28
                    print('veliki raise') #  idemo do kraja
                elif hand==4 and karte_stol>3:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=28
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=28
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand>4:
                        for i in range(blinds):  #koliko puta raiseat
                            mis2.click(1000,625) #raise jos
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=28
                        print('veliki raise') #  idemo do kraja
                    
                        
                else:
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=28
                    print('veliki raise') #  idemo do kraja
            
            elif hand>=3: #dobio tris ili vise
                if len(vrste_igraca2)==0 or call==2 or call==3:
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                        
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=28
                    print('veliki raise')
                elif call==1:
                    mis2.click(750,670) # call
                    mis2.click(750,370) #makni ga sa gumba
                    print('call')
                    situacija=28
                else:
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                        
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=28
                    print('veliki raise')
                    
            elif jacina[0]>=max(jacina):
                for i in range(blinds):  #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                print('veliki raise')
                situacija=29

            elif call==1 and visoke_karte<2 and situacija2==1002:
                              #raiseo na trecoj, nije dosla visoka nastavi raise
                for i in range(blinds/2):  #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                print('veliki raise')
                situacija=29
            elif call==1: #niko raise,check
                mis2.click(750,670) # call
                mis2.click(750,370) #makni ga sa gumba
                print('call')
                situacija=29
            elif call==2 and (isplati1==1 or postotak<0.22) and velicina_raisea<30: #niko raise,check
                mis2.click(750,670) # call
                mis2.click(750,370) #makni ga sa gumba
                print('call')
                situacija=29
            elif call==3 and (isplati1==1 or postotak<0.32): #niko raise,check
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                situacija=28
                print('allin')
            elif call>1: 
                mis2.click(630,670) #fold
                print('fold')

        elif situacija2==13 or situacija2==30 : # 2 para i vise, s glupim slikama
            for i in range(blinds):  #koliko puta raiseat
                mis2.click(1000,625) #raise jos
                    
            mis2.click(930,670) #raise velik gumb
            mis2.click(750,370) #makni ga sa gumba
            situacija=30
            print('veliki raise') # kad je bal nek je maskembal, idemo do kraja
                
        elif situacija2==14 or situacija2==104 or situacija2==31 or situacija2==32: #neko raiseao, ja samo par, s glupim slikak
            hand=ruka.koja(jacina2,znak,call) # dodatak 104, ja raiseo sa parom(jer niko nije), neko me pratio
            if hand>=2: #dobio 2 para ili vise, ma nek se gubi, ovo preispitat
                for i in range(blinds):  #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                situacija=31
                print('veliki raise') #  idemo do kraja
            if call==1:
                mis2.click(750,670) # call
                mis2.click(750,370) #makni ga sa gumba
                print('call')
                situacija=32
            if call>1:
                mis2.click(630,670) #fold
                print('fold')
                
        
            

        elif situacija2==15 or situacija2==33 or situacija2==34:     #niko ne raise,ja nisam imo nis, slike imam
            hand=ruka.koja(jacina2,znak,call)
            if hand>=1: # dobio par, a niko nije raiseao prije toga
                for i in range(blinds):  #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                    
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                situacija=33
                print('veliki raise') #  idemo do kraja

            elif call==1:
                mis2.click(750,670) # call
                mis2.click(750,370) #makni ga sa gumba
                print('call')
                situacija=34
            elif call>1:
                mis2.click(630,670) #fold
                print('fold')

        elif situacija2==108 or situacija2==112: # 2 para i vise, do kraja, slike u boji 
            
            hand=ruka.koja(jacina2,znak,call)
            karte_stol=nastolu.sto(jacina,znak)
            
            if hand<3 and bjezi==1: #mega opasnost
                if call==1: #niko ne raise,ja nemam nis, check
                    mis2.click(750,670) #call
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=112
                    print('call')
                elif call>1: #raise, a ja nista nemam
                    mis2.click(630,670) #fold
                    print('fold')
                    
            elif karte_stol==4 or karte_stol==5 or karte_stol==1:
                if hand==2 and jacina[2:].count(jacina[2])==1 and jacina[2:].count(jacina[3])==1 and jacina[2:].count(jacina[4])==1 and jacina[2:].count(jacina[5])==1 and jacina[2:].count(jacina[6])==1: 
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=112
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=112
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')

                elif hand<3:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=112
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand==3:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=112
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=112
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand==4 and karte_stol<4: #skala i nema 4 of boje
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=112
                    print('veliki raise') #  idemo do kraja
                elif hand==4 and karte_stol>3:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=112
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=112
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand>4:
                        for i in range(blinds):  #koliko puta raiseat
                            mis2.click(1000,625) #raise jos
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=112
                        print('veliki raise') #  idemo do kraja
                    
                        
                else:
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=112
                    print('veliki raise') #  idemo do kraja
            else:
                if opasni_igrac==1: #ako je LAG onda check call
                    if call==2:
                        mis2.click(750,670) #call
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=112
                        print('call')    
                    elif call==3:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('all in')
                        situacija=112
                    elif call==1:
                        mis2.click(750,670) #call
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=112
                        print('check')    
                else:
                    for i in range(blinds/2):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=112
                    print('veliki raise') #  idemo do kraja

        elif situacija2==109 or situacija2==113: #ceko boju, ili sskala s 2 strane jos jednom raise raise
            hand=ruka.koja(jacina2,znak,call)

            karte_stol=nastolu.sto(jacina,znak)
            if karte_stol==4 or karte_stol==5 or karte_stol==1:

                if hand==2 and jacina[2:].count(jacina[2])==1 and jacina[2:].count(jacina[3])==1 and jacina[2:].count(jacina[4])==1 and jacina[2:].count(jacina[5])==1 and jacina[2:].count(jacina[6])==1: 
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=113
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=113
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand<3:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=113
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand==3:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=113
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=113
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand==4 and karte_stol<4: #skala i nema 4 of boje
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=113
                    print('veliki raise') #  idemo do kraja
                elif hand==4 and karte_stol>3: #ima 4 od boje
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=113
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=113
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand>4:
                        for i in range(blinds):  #koliko puta raiseat
                            mis2.click(1000,625) #raise jos
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=113
                        print('veliki raise') #  idemo do kraja
                    
                        
                else:
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=113
                    print('veliki raise') #  idemo do kraja

            elif hand>=3 and opasni_igrac==1:
                if call==2:
                    mis2.click(750,670) #call
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=113
                    print('call')    
                elif call==3:
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    print('all in')
                    situacija=113
                elif call==1:
                    mis2.click(750,670) #call
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=113
                    print('check')    
                
            elif hand>=3: # dobio tris ili vise
                for i in range(blinds/2):  #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                situacija=113
                print('veliki raise') #  idemo do kraja
            elif hand==2 and jacina[2:].count(jacina[2])==1 and jacina[2:].count(jacina[3])==1 and jacina[2:].count(jacina[4])==1 and jacina[2:].count(jacina[5])==1:
                    #2 prava para
                for i in range(blinds):  #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                    
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                situacija=113
                print('veliki raise') #  idemo do kraja     #2 prava para

            
                                
            elif hand==1 or hand==2: #imam par, neko raise
                if jacina.count(jacina[0])>1: #prva karta se uparila
                    if jacina[0]>=max(jacina[2:]): #najjaci par na stolu imam, ili check na 3 na stolu ili ja raise

                        if call==1 and (tri_od_boje==1 or jedan_za_skalu==1 or skala_dvije_strane==1) and len(vrste_igraca2)>0:
                            mis2.click(750,670) #call
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=113
                            print('call')    
                        elif call==1:
                            for i in range(blinds/2):  #koliko puta raiseat
                                mis2.click(1000,625) #raise jos
                    
                            mis2.click(930,670) #raise velik gumb
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=113 # checkirao, pa sam raiseo na najjaci par
                            print('raise')
                        elif call==2 and situacija2==109 and postotak<0.51: #nije reraise
                            if postotak<0.3: #jako mali raise neko napravio
                                for i in range(blinds/2):  #koliko puta raiseat
                                    mis2.click(1000,625) #raise jos
                                    
                                mis2.click(930,670) #raise velik gumb
                                mis2.click(750,370) #makni ga sa gumba
                                situacija=113
                                print('raise')    
                           
                        
                            elif call==3:
                                mis2.click(930,670) #raise velik gumb
                                mis2.click(750,370) #makni ga sa gumba
                                print('all in')
                            else:    
                                mis2.click(750,670) #call
                                mis2.click(750,370) #makni ga sa gumba
                                situacija=113
                                print('call')

                        elif call==2 and postotak<0.53:
                            mis2.click(750,670) #call
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=113 # raiseao je, pa sam samo call-o
                            #print('prvi')
                            print('call')
                        elif call==3 and postotak<0.53:

                            mis2.click(930,670) #raise velik gumb
                            mis2.click(750,370) #na najjaci par pratim all in
                            print('raise')
                        else:
                            mis2.click(630,670) #fold
                            mis2.click(750,370) #makni ga sa gumba
                            print('fold')
                            
                    elif call==1: # prva karta se uparila,ali nije najjaci par
                        mis2.click(750,670) #call
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=113
                        #print('prvi')
                        print('call')
                    elif call>1:
                        if postotak<0.35:
                            if call==2:
                                mis2.click(750,670) #call
                                mis2.click(750,370) #makni ga sa gumba
                                situacija=113
                                #print('prvi')
                                print('call')
                            elif call==3:
                                mis2.click(930,670) #raise velik gumb
                                mis2.click(750,370) #makni ga sa gumba
                                situacija=113 # checkirao, pa sam raiseo na najjaci par
                                print('all in')
                        else:
                            mis2.click(630,670) #fold
                            mis2.click(750,370) #makni ga sa gumba
                            print('fold')
                        
                elif jacina.count(jacina[1])>1:#druga karta se uparila
                    if jacina[1]>=max(jacina[2:]): #najjaci par na stolu imam, 


                        if call==1 and (tri_od_boje==1 or jedan_za_skalu==1 or skala_dvije_strane==1) and len(vrste_igraca2)>0:
                            mis2.click(750,670) #call #gadan flop
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=113
                            print('call')  
                    

                        elif call==1:
                            for i in range(blinds/2):  #koliko puta raiseat
                                mis2.click(1000,625) #raise jos
                                
                            mis2.click(930,670) #raise velik gumb
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=113 # on checkirao, pa sam raiseo na najjaci par
                            print('raise')

                        elif call==2 and situacija2==109 and postotak<0.51: #nije reraise
                            if postotak<0.3: #jako mali raise neko napravio
                                for i in range(blinds/2):  #koliko puta raiseat
                                    mis2.click(1000,625) #raise jos
                                    
                                mis2.click(930,670) #raise velik gumb
                                mis2.click(750,370) #makni ga sa gumba
                                situacija=113
                                print('raise')    
                           
                        
                            elif call==3:
                                mis2.click(930,670) #raise velik gumb
                                mis2.click(750,370) #makni ga sa gumba
                                print('all in')
                            else:    
                                mis2.click(750,670) #call
                                mis2.click(750,370) #makni ga sa gumba
                                situacija=113
                                print('call')
        
                        elif call==2 and postotak<0.60:
                            mis2.click(750,670) #call
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=113 # raiseao je, pa sam samo call-o
                            #print('prvi')
                            print('call')
                        elif call==3 and postotak<0.60:
                            mis2.click(930,670) #raise velik gumb
                            mis2.click(750,370) #na najjaci par pratim all in
                            print('all in')
                        else:
                            mis2.click(630,670) #fold
                            mis2.click(750,370) #makni ga sa gumba
                            print('fold')
                        
                    elif call==1: # druga karta se uparila,ali nije najjaci par
                        mis2.click(750,670) #call
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=113
                        #print('drugi')
                        print('call')
                    elif call>1:
                        if postotak<0.35:
                            if call==2:
                                mis2.click(750,670) #call
                                mis2.click(750,370) #makni ga sa gumba
                                situacija=113
                                #print('prvi')
                                print('call')
                            elif call==3:
                                mis2.click(930,670) #raise velik gumb
                                mis2.click(750,370) #makni ga sa gumba
                                situacija=113 # checkirao, pa sam raiseo na najjaci par
                                print('all in')
                        else:
                            mis2.click(630,670) #fold
                            mis2.click(750,370) #makni ga sa gumba
                            print('fold')
                else:
                    if call==1:
                        mis2.click(750,670) #call
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=113
                        #print('treci')
                        #print(jacina)
                        print('call')    
                    elif call>1:
                        if postotak<0.34:
                            if call==2:
                                mis2.click(750,670) #call
                                mis2.click(750,370) #makni ga sa gumba
                                situacija=113
                                #print('prvi')
                                print('call')
                            elif call==3:
                                mis2.click(930,670) #raise velik gumb
                                mis2.click(750,370) #makni ga sa gumba
                                situacija=113 # checkirao, pa sam raiseo na najjaci par
                                print('all in')
                        else:
                            mis2.click(630,670) #fold
                            mis2.click(750,370) #makni ga sa gumba
                            print('fold')
                        
            elif hand==-1 and call>1 and isplati3==1:
                if call==2:
                    mis2.click(750,670) # call
                    mis2.click(750,370) #makni ga sa gumba
                    print('call')
                    situacija=113
                else:
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=113 # checkirao, pa sam raiseo na najjaci par
                    print('all in')
                    
            elif call==1:
                mis2.click(750,670) # call
                mis2.click(750,370) #makni ga sa gumba
                print('call')
                situacija=113
            elif call>1:
                if boja==1 and isplati2==1:
                    if call==2:
                        mis2.click(750,670) #call
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=113
                        #print('prvi')
                        print('call')
                    elif call==3:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=120 # checkirao, pa sam raiseo na najjaci par
                        print('all in')
                else:
                    mis2.click(630,670) #fold
                    mis2.click(750,370) #makni ga sa gumba
                    print('fold') 

        elif situacija2==110 or situacija2==111 or situacija2==114 or situacija2==115 or situacija2==120 or situacija2==121: #najjaci par, prate me, ili check na flopu a nisam imo nista
            hand=ruka.koja(jacina2,znak,call) #ovaj uvjet dodat stvari, razdvojit itd...
            #karte_stol=nastolu.sto(jacina,znak)
            boja=0
            if znak[0]==znak[1]: # dodatak jer sam situaciju slika izjednacio sa kartama u boji
                

                if znak.count(znak[0])>3:
                    boja=1 # 4 od boje su na stolu
                else:
                    boja=0
            karte_stol=nastolu.sto(jacina,znak)
            if karte_stol==4 or karte_stol==5 or karte_stol==1:
                if hand==2 and jacina[2:].count(jacina[2])==1 and jacina[2:].count(jacina[3])==1 and jacina[2:].count(jacina[4])==1 and jacina[2:].count(jacina[5])==1 and jacina[2:].count(jacina[6])==1: 
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=114
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=114
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                
                elif hand<3:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=120
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand==3:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=120
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=120
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand==4 and karte_stol<4: #skala i nema 4 of boje
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=120
                    print('veliki raise') #  idemo do kraja
                elif hand==4 and karte_stol>3: #ima 4 od boje
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=120
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=120
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand>4:
                        for i in range(blinds):  #koliko puta raiseat
                            mis2.click(1000,625) #raise jos
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=120
                        print('veliki raise') #  idemo do kraja
                    
                        
                else:
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=120
                    print('veliki raise') #  idemo do kraja
            elif hand>=3 and opasni_igrac==1: # LAG-u chekiram
                if call==2:
                    mis2.click(750,670) #call
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=114
                    print('call')    
                elif call==3:
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    print('all in')
                    situacija=114
                elif call==1:
                    mis2.click(750,670) #call
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=114
                    print('check')    
                    
            elif hand>=3: # dobio tris ili vise
                for i in range(blinds/2):  #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                situacija=114
                print('veliki raise') #  idemo do kraja
            elif hand==2 and jacina[2:].count(jacina[2])==1 and jacina[2:].count(jacina[3])==1 and jacina[2:].count(jacina[4])==1 and jacina[2:].count(jacina[5])==1:
                    #2 prava para
                for i in range(blinds):  #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                    
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                situacija=114
                print('veliki raise') #  idemo do kraja     #2 prava para

            elif hand==1 or hand==2: #imam par, neko raise
                if jacina.count(jacina[0])>1: #prva karta se uparila
                    if jacina[0]>=max(jacina[2:]): #najjaci par na stolu imam, ili check na 3 na stolu ili ja raise

                        if situacija2==121 or situacija2==120: #neko reraise, ne zanima me, fold

                            if call==3 and postotak<0.25:
                                mis2.click(930,670) #raise velik gumb
                                mis2.click(750,370) #makni ga sa gumba
                                situacija=121
                                print('allin')

                            elif call==2 and postotak<0.25:
                                mis2.click(750,670) #call
                                mis2.click(750,370) #makni ga sa gumba
                                situacija=121
                                print('call')
                            elif call>1:
                                mis2.click(630,670) #fold
                                mis2.click(750,370) #makni ga sa gumba
                                print('fold')

                        elif call==1 and (tri_od_boje==1 or jedan_za_skalu==1 or skala_dvije_strane==1) and len(vrste_igraca2)>0:
                            mis2.click(750,670) #call
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=121
                            print('call')

                        elif call==1 and (opasni_igrac!=2 and opasni_igrac!=3): #nisu tight
                            for i in range(blinds/2):  #koliko puta raiseat
                                mis2.click(1000,625) #raise jos
                    
                            mis2.click(930,670) #raise velik gumb
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=120 # checkirao, pa sam raiseo na najjaci par
                            print('raise')

                        elif call==2 and (situacija2==110 or situacija2==111) and postotak<0.51: #nije reraise
                            if postotak<0.3: #jako mali raise neko napravio
                                for i in range(blinds/2):  #koliko puta raiseat
                                    mis2.click(1000,625) #raise jos
                                    
                                mis2.click(930,670) #raise velik gumb
                                mis2.click(750,370) #makni ga sa gumba
                                situacija=120
                                print('raise')    
                           
                        
                            elif call==3:
                                mis2.click(930,670) #raise velik gumb
                                mis2.click(750,370) #makni ga sa gumba
                                print('all in')
                            else:    
                                mis2.click(750,670) #call
                                mis2.click(750,370) #makni ga sa gumba
                                situacija=121
                                print('call')

                        elif call==2 and postotak<0.51 and (opasni_igrac!=2 and opasni_igrac!=3):
                            mis2.click(750,670) #call
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=121 # raiseao je, pa sam samo call-o
                            #print('prvi')
                            print('call')
                        elif call==3 and postotak<0.51 and (opasni_igrac!=2 and opasni_igrac!=3):

                            mis2.click(930,670) #raise velik gumb
                            mis2.click(750,370) #na najjaci par pratim all in
                            print('raise')
                        elif call==1:
                            mis2.click(750,670) #call
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=121 # raiseao je, pa sam samo call-o
                            
                            print('call')
                        else:
                            mis2.click(630,670) #fold
                            mis2.click(750,370) #makni ga sa gumba
                            print('fold')
                    
                    elif call==1: # prva karta se uparila,ali nije najjaci par
                        mis2.click(750,670) #call
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=115
                        #print('prvi')
                        print('call')
                    elif call>1:
                        if boja==1 and postotak<0.30:
                            if call==2:
                                mis2.click(750,670) #call
                                mis2.click(750,370) #makni ga sa gumba
                                situacija=115
                                #print('prvi')
                                print('call')
                            elif call==3:
                                mis2.click(930,670) #raise velik gumb
                                mis2.click(750,370) #makni ga sa gumba
                                situacija=120 # checkirao, pa sam raiseo na najjaci par
                                print('all in')
                        elif postotak<0.1 and (opasni_igrac!=2 and opasni_igrac!=3):
                            mis2.click(750,670) #call
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=115
                            #print('prvi')
                            print('call')
                        else:
                            mis2.click(630,670) #fold
                            mis2.click(750,370) #makni ga sa gumba
                            print('fold')
                        
                elif jacina.count(jacina[1])>1:#druga karta se uparila
                    if jacina[1]>=max(jacina[2:]): #najjaci par na stolu imam, 

                        if situacija2==121 or situacija2==120: #neko reraise, ne zanima me, fold

                            if call==3 and postotak<0.25:
                                mis2.click(930,670) #raise velik gumb
                                mis2.click(750,370) #makni ga sa gumba
                                situacija=121
                                print('allin')

                            elif call==2 and postotak<0.25:
                                mis2.click(750,670) #call
                                mis2.click(750,370) #makni ga sa gumba
                                situacija=121
                                print('call')
                            elif call>1:
                                mis2.click(630,670) #fold
                                mis2.click(750,370) #makni ga sa gumba
                                print('fold')



                        elif call==1 and (tri_od_boje==1 or jedan_za_skalu==1 or skala_dvije_strane==1) and len(vrste_igraca2)>0:
                            mis2.click(750,670) #call
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=121
                            print('call')

                        elif call==1 and (opasni_igrac!=2 and opasni_igrac!=3):
                            for i in range(blinds/2):  #koliko puta raiseat
                                mis2.click(1000,625) #raise jos
                                
                            mis2.click(930,670) #raise velik gumb
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=120 # on checkirao, pa sam raiseo na najjaci par
                            print('raise')


                        elif call==2 and (situacija2==110 or situacija2==111) and postotak<0.51: #nije reraise
                            if postotak<0.3: #jako mali raise neko napravio
                                for i in range(blinds/2):  #koliko puta raiseat
                                    mis2.click(1000,625) #raise jos
                                    
                                mis2.click(930,670) #raise velik gumb
                                mis2.click(750,370) #makni ga sa gumba
                                situacija=120
                                print('raise')    
                           
                        
                            elif call==3:
                                mis2.click(930,670) #raise velik gumb
                                mis2.click(750,370) #makni ga sa gumba
                                print('all in')
                            else:    
                                mis2.click(750,670) #call
                                mis2.click(750,370) #makni ga sa gumba
                                situacija=121
                                print('call')

                        elif call==2 and postotak<0.51 and (opasni_igrac!=2 and opasni_igrac!=3):
                            mis2.click(750,670) #call
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=121 # raiseao je, pa sam samo call-o
                            #print('prvi')
                            print('call')
                        elif call==3 and postotak<0.51:
                            mis2.click(930,670) #raise velik gumb
                            mis2.click(750,370) #na najjaci par pratim all in
                            print('all in')
                        elif call==1:
                            mis2.click(750,670) #call
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=121 # raiseao je, pa sam samo call-o
                        
                            print('call')
                        else:
                            mis2.click(630,670) #fold
                            mis2.click(750,370) #makni ga sa gumba
                            print('fold')
                        
                   
                    elif call==1: # prva karta se uparila,ali nije najjaci par
                        mis2.click(750,670) #call
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=115
                        #print('drugi')
                        print('call')
                    elif call>1:
                        if boja==1 and postotak<0.30:
                            if call==2:
                                mis2.click(750,670) #call
                                mis2.click(750,370) #makni ga sa gumba
                                situacija=115
                                #print('prvi')
                                print('call')
                            elif call==3:
                                mis2.click(930,670) #raise velik gumb
                                mis2.click(750,370) #makni ga sa gumba
                                situacija=120 # checkirao, pa sam raiseo na najjaci par
                                print('all in')
                        elif postotak<0.1 and (opasni_igrac!=2 and opasni_igrac!=3): # imam par, a mali je raise
                            mis2.click(750,670) #call
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=115
                            #print('prvi')
                            print('call')
                        else:
                            mis2.click(630,670) #fold
                            mis2.click(750,370) #makni ga sa gumba
                            print('fold')
                else:
                     
                    if call==1 and (tri_od_boje==1 or jedan_za_skalu==1 or skala_dvije_strane==1) and len(vrste_igraca2)>0:
                            mis2.click(750,670) #call
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=121
                            print('call')
                    
                    elif call==1 and len(vrste_igraca2)==0 and (opasni_igrac!=2 and opasni_igrac!=3): #nemam nis, ali svi chek
                        for i in range(blinds/2):  #koliko puta raiseat
                            mis2.click(1000,625) #raise jos
                    
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=121 # checkirao, pa sam raiseo na najjaci par
                        print('raise')

                    elif call==1:
                        mis2.click(750,670) #call
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=115
                        #print('treci')
                        #print(jacina)
                        print('call')    
                    elif call>1:
                        if boja==1 and postotak<0.30: #neka gleda pare, koliko ima treba napravit
                            if call==2:
                                mis2.click(750,670) #call
                                mis2.click(750,370) #makni ga sa gumba
                                situacija=115
                                #print('prvi')
                                print('call')
                            elif call==3:
                                mis2.click(930,670) #raise velik gumb
                                mis2.click(750,370) #makni ga sa gumba
                                situacija=120 # checkirao, pa sam raiseo na najjaci par
                                print('all in')
                        else:
                            mis2.click(630,670) #fold
                            mis2.click(750,370) #makni ga sa gumba
                            print('fold')
            elif hand==-1 and boja==1 and call==2: #i boju i skalu sa 2 strane
                for i in range(blinds/2):  #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                    
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                situacija=121 # checkirao, pa sam raiseo na najjaci par
                print('raise')
            elif hand==-1 and call>1 and isplati3==1:
                if call==2:
                    mis2.click(750,670) # call
                    mis2.click(750,370) #makni ga sa gumba
                    print('call')
                    situacija=120
                else:
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=120 # checkirao, pa sam raiseo na najjaci par
                    print('all in')
           
            elif hand==-1 and boja==1 and call==1:
                
                for i in range(blinds/2):  #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                    
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                situacija=121 # checkirao, pa sam raiseo na najjaci par
                print('raise')
            elif call==1:
                mis2.click(750,670) # call
                mis2.click(750,370) #makni ga sa gumba
                print('call')
                situacija=115
            elif call>1:
                if boja==1 and isplati2==1:
                    if call==2:
                        mis2.click(750,670) #call
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=115
                        #print('prvi')
                        print('call')
                    elif call==3:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=120 # checkirao, pa sam raiseo na najjaci par
                        print('all in')
                else:
                    mis2.click(630,670) #fold
                    mis2.click(750,370) #makni ga sa gumba
                    print('fold')
        
        elif situacija2==16 or situacija2==35 or situacija2==105 or situacija2==106:   #peta situacija, lose karte, besplatni flop, ali dobio 2 para, ili najjaci par
            for i in range(blinds):  #koliko puta raiseat
                mis2.click(1000,625) #raise jos
                    
            mis2.click(930,670) #raise velik gumb
            mis2.click(750,370) #makni ga sa gumba
            situacija=35
            print('veliki raise') #  idemo do kraja
                
        elif situacija2==17 or situacija2==36 or situacija2==37:  #nista ili par, niko ne raisea
            hand=ruka.koja(jacina2,znak,call)
            if hand>=3: # dobio tris ili vise
                for i in range(blinds):  #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                    
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                situacija=36
                print('veliki raise') #  idemo do kraja
            elif hand==2 and jacina[2:].count(jacina[2])==1 and jacina[2:].count(jacina[3])==1 and jacina[2:].count(jacina[4])==1 and jacina[2:].count(jacina[5])==1: #2 para, prava
                for i in range(blinds):  #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                    
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                situacija=36
                print('veliki raise') #  idemo do kraja
            elif call==1:
                mis2.click(750,670) # call
                mis2.click(750,370) #makni ga sa gumba
                print('call')
                situacija=37
            elif call>1:
                mis2.click(630,670) #fold
                print('fold')



                
    else:                                               #5 karata dole
        if situacija2==18: #imam set ili ful, nastavi dizat
            hand=ruka.koja(jacina2,znak,call)
            karte_stol=nastolu.sto(jacina,znak)
            if karte_stol==4 or karte_stol==5 or karte_stol==1: # 4 od skale ili 4 od boje
                if hand==2 and jacina[2:].count(jacina[2])==1 and jacina[2:].count(jacina[3])==1 and jacina[2:].count(jacina[4])==1 and jacina[2:].count(jacina[5])==1 and jacina[2:].count(jacina[6])==1: 
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=18
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=18
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                
                elif hand<3:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=18
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand==3:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=18
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=18
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand==4 and karte_stol<4: #skala i nema 4 of boje
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=18
                    print('veliki raise') #  idemo do kraja
                elif hand==4 and karte_stol>3: #ima 4 od boje
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=18
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=18
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand>4:
                        for i in range(blinds):  #koliko puta raiseat
                            mis2.click(1000,625) #raise jos
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=18
                        print('veliki raise') #  idemo do kraja
                    
                        
                else:
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=18
                    print('veliki raise') #  idemo do kraja



            

            elif karte_stol==2 or karte_stol==3 or karte_stol>7 : # 5 od boje,5 od skale
                if hand<4:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=18
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand==4 and karte_stol==1: #skala i nema 4 of boje
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=18
                    print('veliki raise') #  idemo do kraja
                elif hand==4 and (karte_stol==3 or karte_stol==2): # skala na stolu
                    if (jacina[0]-max(jacina[2:]))==1 or (jacina[1]-max(jacina[2:]))==1: # imam vecu od one na stolu
                        for i in range(blinds):  #koliko puta raiseat
                            mis2.click(1000,625) #raise jos
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=18
                        print('veliki raise') #  idemo do kraja
                    else:
                        if call==1:
                            mis2.click(750,670) # call
                            mis2.click(750,370) #makni ga sa gumba
                            print('call')
                            situacija=18
                        else:
                            mis2.click(630,670) #fold
                            print('fold')
                elif hand==4 and karte_stol>7: #ima 5 od boje
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=18
                    elif call==2 and postotak<0.30:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=18
                    elif call==3 and postotak<0.30: 
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=18
                        print('all in') #do kraja
                    else:
                         mis2.click(630,670) #fold
                         print('fold')
                elif hand==5 and karte_stol>7: #ima 5 od boje
                    if (znak[0]==znak[2] and jacina[0]>max(jacina[2:])) or (znak[1]==znak[2] and jacina[1]>max(jacina[2:])):
                        for i in range(blinds): #koliko puta raiseat
                            mis2.click(1000,625) #raise jos
                
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=18
                        print('veliki raise') #do kraja
                    elif (znak[0]==znak[2] or znak[1]==znak[2]):
                        if call==3:
                            mis2.click(930,670) #raise velik gumb
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=18
                            print('all in') #do kraja
                        else:
                            mis2.click(750,670) # call
                            mis2.click(750,370) #makni ga sa gumba
                            print('call')
                            situacija=18
                    else:
                        if call==1:
                            mis2.click(750,670) # call
                            mis2.click(750,370) #makni ga sa gumba
                            print('call')
                            situacija=18
                        elif call==2 and postotak<0.30:
                            mis2.click(750,670) # call
                            mis2.click(750,370) #makni ga sa gumba
                            print('call')
                            situacija=18
                        elif call==3 and postotak<0.30: 
                            mis2.click(930,670) #raise velik gumb
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=18
                            print('all in') #do kraja
                        else:
                             mis2.click(630,670) #fold
                             print('fold')

                        

                else:
                    for i in range(blinds): #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=18
                    print('veliki raise') #do kraja
            
            else:
                for i in range(blinds):  #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                    
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                situacija=18
                print('veliki raise') #  idemo do kraja
            

        elif situacija2==19: #dobio set ili vise, raise ko lud
            hand=ruka.koja(jacina2,znak,call)
            karte_stol=nastolu.sto(jacina,znak)
            if karte_stol==4 or karte_stol==5 or karte_stol==1: # 4 od skale ili 4 od boje
                if hand==2 and jacina[2:].count(jacina[2])==1 and jacina[2:].count(jacina[3])==1 and jacina[2:].count(jacina[4])==1 and jacina[2:].count(jacina[5])==1 and jacina[2:].count(jacina[6])==1: 
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=19
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=19
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')

                elif hand<3:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=19
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand==3:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=19
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=19
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand==4 and karte_stol<4: #skala i nema 4 of boje
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=19
                    print('veliki raise') #  idemo do kraja
                elif hand==4 and karte_stol>3: #ima 4 od boje
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=19
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=19
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand>4:
                        for i in range(blinds):  #koliko puta raiseat
                            mis2.click(1000,625) #raise jos
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=19
                        print('veliki raise') #  idemo do kraja
                    
                        
                else:
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=19
                    print('veliki raise') #  idemo do kraja



            

            elif karte_stol==2 or karte_stol==3 or karte_stol>7 : # 5 od boje,5 od skale
                if hand<4:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=19
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand==4 and karte_stol==1: #skala i nema 4 of boje
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=19
                    print('veliki raise') #  idemo do kraja
                elif hand==4 and (karte_stol==3 or karte_stol==2): # skala na stolu
                    if (jacina[0]-max(jacina[2:]))==1 or (jacina[1]-max(jacina[2:]))==1: # imam vecu od one na stolu
                        for i in range(blinds):  #koliko puta raiseat
                            mis2.click(1000,625) #raise jos
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=19
                        print('veliki raise') #  idemo do kraja
                    else:
                        if call==1:
                            mis2.click(750,670) # call
                            mis2.click(750,370) #makni ga sa gumba
                            print('call')
                            situacija=19
                        else:
                            mis2.click(630,670) #fold
                            print('fold')
                elif hand==4 and karte_stol>7: #ima 5 od boje
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=19
                    elif call==2 and postotak<0.30:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=19
                    elif call==3 and postotak<0.30: 
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=19
                        print('all in') #do kraja
                    else:
                         mis2.click(630,670) #fold
                         print('fold')
                elif hand==5 and karte_stol>7: #ima 5 od boje
                    if (znak[0]==znak[2] and jacina[0]>max(jacina[2:])) or (znak[1]==znak[2] and jacina[1]>max(jacina[2:])):
                        for i in range(blinds): #koliko puta raiseat
                            mis2.click(1000,625) #raise jos
                
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=19
                        print('veliki raise') #do kraja
                    elif (znak[0]==znak[2] or znak[1]==znak[2]):
                        if call==3:
                            mis2.click(930,670) #raise velik gumb
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=19
                            print('all in') #do kraja
                        else:
                            mis2.click(750,670) # call
                            mis2.click(750,370) #makni ga sa gumba
                            print('call')
                            situacija=19
                    else:
                        if call==1:
                            mis2.click(750,670) # call
                            mis2.click(750,370) #makni ga sa gumba
                            print('call')
                            situacija=19
                        elif call==2 and postotak<0.30:
                            mis2.click(750,670) # call
                            mis2.click(750,370) #makni ga sa gumba
                            print('call')
                            situacija=19
                        elif call==3 and postotak<0.30: 
                            mis2.click(930,670) #raise velik gumb
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=19
                            print('all in') #do kraja
                        else:
                             mis2.click(630,670) #fold
                             print('fold')

                        

                else:
                    for i in range(blinds): #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=19
                    print('veliki raise') #do kraja
            
            else:
                for i in range(blinds):  #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                    
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                situacija=19
                print('veliki raise') #  idemo do kraja

            
        elif situacija2==20: #nije bila dosla karta veca ,nastavi raise, veliki rucni
            hand=ruka.koja(jacina2,znak,call)
            karte_stol=nastolu.sto(jacina,znak)
            if karte_stol==4 or karte_stol==5 or karte_stol==1: # 4 od skale ili 4 od boje
                if hand==2 and jacina[2:].count(jacina[2])==1 and jacina[2:].count(jacina[3])==1 and jacina[2:].count(jacina[4])==1 and jacina[2:].count(jacina[5])==1 and jacina[2:].count(jacina[6])==1: 
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=20
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=20
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')


                elif hand<3:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=20
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand==3:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=20
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=20
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand==4 and karte_stol<4: #skala i nema 4 of boje
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=20
                    print('veliki raise') #  idemo do kraja
                elif hand==4 and karte_stol>3: #ima 4 od boje
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=20
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=20
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand>4:
                        for i in range(blinds):  #koliko puta raiseat
                            mis2.click(1000,625) #raise jos
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=20
                        print('veliki raise') #  idemo do kraja
                    
                        
                else:
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=20
                    print('veliki raise') #  idemo do kraja



            

            elif karte_stol==2 or karte_stol==3 or karte_stol>7 : # 5 od boje,5 od skale
                if hand<4:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=20
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand==4 and karte_stol==1: #skala i nema 4 of boje
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=20
                    print('veliki raise') #  idemo do kraja
                elif hand==4 and (karte_stol==3 or karte_stol==2): # skala na stolu
                    if (jacina[0]-max(jacina[2:]))==1 or (jacina[1]-max(jacina[2:]))==1: # imam vecu od one na stolu
                        for i in range(blinds):  #koliko puta raiseat
                            mis2.click(1000,625) #raise jos
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=20
                        print('veliki raise') #  idemo do kraja
                    else:
                        if call==1:
                            mis2.click(750,670) # call
                            mis2.click(750,370) #makni ga sa gumba
                            print('call')
                            situacija=20
                        else:
                            mis2.click(630,670) #fold
                            print('fold')
                elif hand==4 and karte_stol>7: #ima 5 od boje
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=20
                    elif call==2 and postotak<0.30:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=20
                    elif call==3 and postotak<0.30: 
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=20
                        print('all in') #do kraja
                    else:
                         mis2.click(630,670) #fold
                         print('fold')
                elif hand==5 and karte_stol>7: #ima 5 od boje
                    if (znak[0]==znak[2] and jacina[0]>max(jacina[2:])) or (znak[1]==znak[2] and jacina[1]>max(jacina[2:])):
                        for i in range(blinds): #koliko puta raiseat
                            mis2.click(1000,625) #raise jos
                
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=20
                        print('veliki raise') #do kraja
                    elif (znak[0]==znak[2] or znak[1]==znak[2]):
                        if call==3:
                            mis2.click(930,670) #raise velik gumb
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=20
                            print('all in') #do kraja
                        else:
                            mis2.click(750,670) # call
                            mis2.click(750,370) #makni ga sa gumba
                            print('call')
                            situacija=20
                    else:
                        if call==1:
                            mis2.click(750,670) # call
                            mis2.click(750,370) #makni ga sa gumba
                            print('call')
                            situacija=20
                        elif call==2 and postotak<0.30:
                            mis2.click(750,670) # call
                            mis2.click(750,370) #makni ga sa gumba
                            print('call')
                            situacija=20
                        elif call==3 and postotak<0.30: 
                            mis2.click(930,670) #raise velik gumb
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=20
                            print('all in') #do kraja
                        else:
                             mis2.click(630,670) #fold
                             print('fold')

                        

                else:
                    for i in range(blinds): #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=20
                    print('veliki raise') #do kraja
            
            else:
                for i in range(blinds):  #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                    
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                situacija=20
                print('veliki raise') #  idemo do kraja, ako sam do ovde raiseo, mogu jos malo

            
        elif situacija2==21: #dosla je veca, ali niko ne raise, veliki rucni
            hand=ruka.koja(jacina2,znak,call)

            karte_stol=nastolu.sto(jacina,znak)
            if karte_stol==4 or karte_stol==5 or karte_stol==1: # 4 od skale ili 4 od boje

                if hand==2 and jacina[2:].count(jacina[2])==1 and jacina[2:].count(jacina[3])==1 and jacina[2:].count(jacina[4])==1 and jacina[2:].count(jacina[5])==1 and jacina[2:].count(jacina[6])==1: 
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=21
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=21
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')


                elif hand<3:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=21
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand==3:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=21
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=21
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand==4 and karte_stol<4: #skala i nema 4 of boje
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=21
                    print('veliki raise') #  idemo do kraja
                elif hand==4 and karte_stol>3: #ima 4 od boje
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=21
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=21
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand>4:
                        for i in range(blinds):  #koliko puta raiseat
                            mis2.click(1000,625) #raise jos
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=21
                        print('veliki raise') #  idemo do kraja
                    
                        
                else:
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=21
                    print('veliki raise') #  idemo do kraja



            

            elif karte_stol==2 or karte_stol==3 or karte_stol>7 : # 5 od boje,5 od skale
                if hand<4:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=21
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand==4 and karte_stol==1: #skala i nema 4 of boje
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=21
                    print('veliki raise') #  idemo do kraja
                elif hand==4 and (karte_stol==3 or karte_stol==2): # skala na stolu
                    if (jacina[0]-max(jacina[2:]))==1 or (jacina[1]-max(jacina[2:]))==1: # imam vecu od one na stolu
                        for i in range(blinds):  #koliko puta raiseat
                            mis2.click(1000,625) #raise jos
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=21
                        print('veliki raise') #  idemo do kraja
                    else:
                        if call==1:
                            mis2.click(750,670) # call
                            mis2.click(750,370) #makni ga sa gumba
                            print('call')
                            situacija=21
                        else:
                            mis2.click(630,670) #fold
                            print('fold')
                elif hand==4 and karte_stol>7: #ima 5 od boje
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=21
                    elif call==2 and postotak<0.30:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=21
                    elif call==3 and postotak<0.30: 
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=21
                        print('all in') #do kraja
                    else:
                         mis2.click(630,670) #fold
                         print('fold')
                elif hand==5 and karte_stol>7: #ima 5 od boje
                    if (znak[0]==znak[2] and jacina[0]>max(jacina[2:])) or (znak[1]==znak[2] and jacina[1]>max(jacina[2:])):
                        for i in range(blinds): #koliko puta raiseat
                            mis2.click(1000,625) #raise jos
                
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=21
                        print('veliki raise') #do kraja
                    elif (znak[0]==znak[2] or znak[1]==znak[2]):
                        if call==3:
                            mis2.click(930,670) #raise velik gumb
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=21
                            print('all in') #do kraja
                        else:
                            mis2.click(750,670) # call
                            mis2.click(750,370) #makni ga sa gumba
                            print('call')
                            situacija=21
                    else:
                        if call==1:
                            mis2.click(750,670) # call
                            mis2.click(750,370) #makni ga sa gumba
                            print('call')
                            situacija=21
                        elif call==2 and postotak<0.30:
                            mis2.click(750,670) # call
                            mis2.click(750,370) #makni ga sa gumba
                            print('call')
                            situacija=21
                        elif call==3 and postotak<0.30: 
                            mis2.click(930,670) #raise velik gumb
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=21
                            print('all in') #do kraja
                        else:
                             mis2.click(630,670) #fold
                             print('fold')

                        

                else:
                    for i in range(blinds): #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=21
                    print('veliki raise') #do kraja
            
            elif hand>=3: # dobio tris ili vise
                for i in range(blinds):  #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                    
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                situacija=21
                print('veliki raise') #do kraja
            elif call==1:
                mis2.click(750,670) # call
                mis2.click(750,370) #makni ga sa gumba
                print('call')
                situacija=21
            elif call==2 and postotak<0.2:
                mis2.click(750,670) # call
                mis2.click(750,370) #makni ga sa gumba
                print('call')
                situacija=21
            elif call>1:
                mis2.click(630,670) #fold
                print('fold')
            
        elif situacija2==22: #dobio set ili vise, raise ko lud, rucni veliki, ali bilo vecih na stolu
            hand=ruka.koja(jacina2,znak,call)
            karte_stol=nastolu.sto(jacina,znak)
            if karte_stol==4 or karte_stol==5 or karte_stol==1: # 4 od skale ili 4 od boje
                if hand==2 and jacina[2:].count(jacina[2])==1 and jacina[2:].count(jacina[3])==1 and jacina[2:].count(jacina[4])==1 and jacina[2:].count(jacina[5])==1 and jacina[2:].count(jacina[6])==1: 
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=22
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=22
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
        
                elif hand<3:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=22
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand==3:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=22
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=22
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand==4 and karte_stol<4: #skala i nema 4 of boje
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=22
                    print('veliki raise') #  idemo do kraja
                elif hand==4 and karte_stol>3: #ima 4 od boje
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=22
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=22
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand>4:
                        for i in range(blinds):  #koliko puta raiseat
                            mis2.click(1000,625) #raise jos
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=22
                        print('veliki raise') #  idemo do kraja
                    
                        
                else:
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=22
                    print('veliki raise') #  idemo do kraja



            

            elif karte_stol==2 or karte_stol==3 or karte_stol>7 : # 5 od boje,5 od skale
                if hand<4:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=22
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand==4 and karte_stol==1: #skala i nema 4 of boje
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=22
                    print('veliki raise') #  idemo do kraja
                elif hand==4 and (karte_stol==3 or karte_stol==2): # skala na stolu
                    if (jacina[0]-max(jacina[2:]))==1 or (jacina[1]-max(jacina[2:]))==1: # imam vecu od one na stolu
                        for i in range(blinds):  #koliko puta raiseat
                            mis2.click(1000,625) #raise jos
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=22
                        print('veliki raise') #  idemo do kraja
                    else:
                        if call==1:
                            mis2.click(750,670) # call
                            mis2.click(750,370) #makni ga sa gumba
                            print('call')
                            situacija=22
                        else:
                            mis2.click(630,670) #fold
                            print('fold')
                elif hand==4 and karte_stol>7: #ima 5 od boje
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=22
                    elif call==2 and postotak<0.30:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=22
                    elif call==3 and postotak<0.30: 
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=22
                        print('all in') #do kraja
                    else:
                         mis2.click(630,670) #fold
                         print('fold')
                elif hand==5 and karte_stol>7: #ima 5 od boje
                    if (znak[0]==znak[2] and jacina[0]>max(jacina[2:])) or (znak[1]==znak[2] and jacina[1]>max(jacina[2:])):
                        for i in range(blinds): #koliko puta raiseat
                            mis2.click(1000,625) #raise jos
                
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=22
                        print('veliki raise') #do kraja
                    elif (znak[0]==znak[2] or znak[1]==znak[2]):
                        if call==3:
                            mis2.click(930,670) #raise velik gumb
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=22
                            print('all in') #do kraja
                        else:
                            mis2.click(750,670) # call
                            mis2.click(750,370) #makni ga sa gumba
                            print('call')
                            situacija=22
                    else:
                        if call==1:
                            mis2.click(750,670) # call
                            mis2.click(750,370) #makni ga sa gumba
                            print('call')
                            situacija=22
                        elif call==2 and postotak<0.30:
                            mis2.click(750,670) # call
                            mis2.click(750,370) #makni ga sa gumba
                            print('call')
                            situacija=22
                        elif call==3 and postotak<0.30: 
                            mis2.click(930,670) #raise velik gumb
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=22
                            print('all in') #do kraja
                        else:
                             mis2.click(630,670) #fold
                             print('fold')

                        

                else:
                    for i in range(blinds): #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=22
                    print('veliki raise') #do kraja
            
            else:
                for i in range(blinds):  #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                    
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                situacija=22
                print('veliki raise') #do kraja
            
        elif situacija2==23: #ja rucni par veliki, check na 4 karte
            hand=ruka.koja(jacina2,znak,call)

            karte_stol=nastolu.sto(jacina,znak)
            if karte_stol==4 or karte_stol==5 or karte_stol==1: # 4 od skale ili 4 od boje

                if hand==2 and jacina[2:].count(jacina[2])==1 and jacina[2:].count(jacina[3])==1 and jacina[2:].count(jacina[4])==1 and jacina[2:].count(jacina[5])==1 and jacina[2:].count(jacina[6])==1: 
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=23
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=23
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
        
                elif hand<3:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=23
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand==3:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=23
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=23
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand==4 and karte_stol<4: #skala i nema 4 of boje
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=23
                    print('veliki raise') #  idemo do kraja
                elif hand==4 and karte_stol>3: #ima 4 od boje
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=23
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=23
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand>4:
                        for i in range(blinds):  #koliko puta raiseat
                            mis2.click(1000,625) #raise jos
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=23
                        print('veliki raise') #  idemo do kraja
                    
                        
                else:
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=23
                    print('veliki raise') #  idemo do kraja



            

            elif karte_stol==2 or karte_stol==3 or karte_stol>7 : # 5 od boje,5 od skale
                if hand<4:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=23
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand==4 and karte_stol==1: #skala i nema 4 of boje
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=23
                    print('veliki raise') #  idemo do kraja
                elif hand==4 and (karte_stol==3 or karte_stol==2): # skala na stolu
                    if (jacina[0]-max(jacina[2:]))==1 or (jacina[1]-max(jacina[2:]))==1: # imam vecu od one na stolu
                        for i in range(blinds):  #koliko puta raiseat
                            mis2.click(1000,625) #raise jos
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=23
                        print('veliki raise') #  idemo do kraja
                    else:
                        if call==1:
                            mis2.click(750,670) # call
                            mis2.click(750,370) #makni ga sa gumba
                            print('call')
                            situacija=23
                        else:
                            mis2.click(630,670) #fold
                            print('fold')
                elif hand==4 and karte_stol>7: #ima 5 od boje
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=23
                    elif call==2 and postotak<0.30:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=23
                    elif call==3 and postotak<0.30: 
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=23
                        print('all in') #do kraja
                    else:
                         mis2.click(630,670) #fold
                         print('fold')
                elif hand==5 and karte_stol>7: #ima 5 od boje
                    if (znak[0]==znak[2] and jacina[0]>max(jacina[2:])) or (znak[1]==znak[2] and jacina[1]>max(jacina[2:])):
                        for i in range(blinds): #koliko puta raiseat
                            mis2.click(1000,625) #raise jos
                
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=23
                        print('veliki raise') #do kraja
                    elif (znak[0]==znak[2] or znak[1]==znak[2]):
                        if call==3:
                            mis2.click(930,670) #raise velik gumb
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=23
                            print('all in') #do kraja
                        else:
                            mis2.click(750,670) # call
                            mis2.click(750,370) #makni ga sa gumba
                            print('call')
                            situacija=23
                    else:
                        if call==1:
                            mis2.click(750,670) # call
                            mis2.click(750,370) #makni ga sa gumba
                            print('call')
                            situacija=23
                        elif call==2 and postotak<0.30:
                            mis2.click(750,670) # call
                            mis2.click(750,370) #makni ga sa gumba
                            print('call')
                            situacija=23
                        elif call==3 and postotak<0.30: 
                            mis2.click(930,670) #raise velik gumb
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=23
                            print('all in') #do kraja
                        else:
                             mis2.click(630,670) #fold
                             print('fold')

                        

                else:
                    for i in range(blinds): #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=23
                    print('veliki raise') #do kraja
            
            
            elif hand>=3: # dobio tris ili vise onda do kraja
                for i in range(blinds):  #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                    
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                situacija=23
                print('veliki raise') #do kraja
            elif call==1:
                mis2.click(750,670) # call
                mis2.click(750,370) #makni ga sa gumba
                print('call')
                situacija=23
            elif call>1:
                mis2.click(630,670) #fold
                print('fold')
                
        elif situacija2==24 or situacija2==25: #aq,ak, dobio par, ide se do kraja, je nije
            hand=ruka.koja(jacina2,znak,call)

            karte_stol=nastolu.sto(jacina,znak)
            if karte_stol==4 or karte_stol==5 or karte_stol==1: # 4 od skale ili 4 od boje

                if hand==2 and jacina[2:].count(jacina[2])==1 and jacina[2:].count(jacina[3])==1 and jacina[2:].count(jacina[4])==1 and jacina[2:].count(jacina[5])==1 and jacina[2:].count(jacina[6])==1: 
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=24
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=24
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')

                elif hand<3:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=24
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand==3:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=24
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=24
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand==4 and karte_stol<4: #skala i nema 4 of boje
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=24
                    print('veliki raise') #  idemo do kraja
                elif hand==4 and karte_stol>3: #ima 4 od boje
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=24
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=24
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand>4:
                        for i in range(blinds):  #koliko puta raiseat
                            mis2.click(1000,625) #raise jos
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=24
                        print('veliki raise') #  idemo do kraja
                    
                        
                else:
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=24
                    print('veliki raise') #  idemo do kraja



            

            elif karte_stol==2 or karte_stol==3 or karte_stol>7 : # 5 od boje,5 od skale
                if hand<4:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=24
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand==4 and karte_stol==1: #skala i nema 4 of boje
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=24
                    print('veliki raise') #  idemo do kraja
                elif hand==4 and (karte_stol==3 or karte_stol==2): # skala na stolu
                    if (jacina[0]-max(jacina[2:]))==1 or (jacina[1]-max(jacina[2:]))==1: # imam vecu od one na stolu
                        for i in range(blinds):  #koliko puta raiseat
                            mis2.click(1000,625) #raise jos
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=24
                        print('veliki raise') #  idemo do kraja
                    else:
                        if call==1:
                            mis2.click(750,670) # call
                            mis2.click(750,370) #makni ga sa gumba
                            print('call')
                            situacija=24
                        else:
                            mis2.click(630,670) #fold
                            print('fold')
                elif hand==4 and karte_stol>7: #ima 5 od boje
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=24
                    elif call==2 and postotak<0.30:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=24
                    elif call==3 and postotak<0.30: 
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=24
                        print('all in') #do kraja
                    else:
                         mis2.click(630,670) #fold
                         print('fold')
                elif hand==5 and karte_stol>7: #ima 5 od boje
                    if (znak[0]==znak[2] and jacina[0]>max(jacina[2:])) or (znak[1]==znak[2] and jacina[1]>max(jacina[2:])):
                        for i in range(blinds): #koliko puta raiseat
                            mis2.click(1000,625) #raise jos
                
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=24
                        print('veliki raise') #do kraja
                    elif (znak[0]==znak[2] or znak[1]==znak[2]):
                        if call==3:
                            mis2.click(930,670) #raise velik gumb
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=24
                            print('all in') #do kraja
                        else:
                            mis2.click(750,670) # call
                            mis2.click(750,370) #makni ga sa gumba
                            print('call')
                            situacija=24
                    else:
                        if call==1:
                            mis2.click(750,670) # call
                            mis2.click(750,370) #makni ga sa gumba
                            print('call')
                            situacija=24
                        elif call==2 and postotak<0.30:
                            mis2.click(750,670) # call
                            mis2.click(750,370) #makni ga sa gumba
                            print('call')
                            situacija=24
                        elif call==3 and postotak<0.30: 
                            mis2.click(930,670) #raise velik gumb
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=24
                            print('all in') #do kraja
                        else:
                             mis2.click(630,670) #fold
                             print('fold')

                        

                else:
                    for i in range(blinds): #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=24
                    print('veliki raise') #do kraja


            else:
                if hand==1:
                    for i in range(blinds/2):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=24
                    print('veliki raise') #  idemo do kraja
                else:
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=24
                    print('veliki raise') #do kraja
        
            
        elif situacija2==26: #aq dosad nemam nis, svi check
            hand=ruka.koja(jacina2,znak,call)

            karte_stol=nastolu.sto(jacina,znak)
            if karte_stol==4 or karte_stol==5 or karte_stol==1: # 4 od skale ili 4 od boje

                if hand==2 and jacina[2:].count(jacina[2])==1 and jacina[2:].count(jacina[3])==1 and jacina[2:].count(jacina[4])==1 and jacina[2:].count(jacina[5])==1 and jacina[2:].count(jacina[6])==1: 
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=26
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=26
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                        
                elif hand<3:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=26
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand==3:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=26
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=26
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand==4 and karte_stol<4: #skala i nema 4 of boje
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=26
                    print('veliki raise') #  idemo do kraja
                elif hand==4 and karte_stol>3: #ima 4 od boje
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=26
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=26
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand>4:
                        for i in range(blinds):  #koliko puta raiseat
                            mis2.click(1000,625) #raise jos
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=26
                        print('veliki raise') #  idemo do kraja
                    
                        
                else:
                    if hand==1:
                        for i in range(blinds/2):  #koliko puta raiseat
                            mis2.click(1000,625) #raise jos
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=26
                        print('veliki raise') #  idemo do kraja
                    else:
                        for i in range(blinds):  #koliko puta raiseat
                            mis2.click(1000,625) #raise jos
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=26
                        print('veliki raise') #do kraja



            

            elif karte_stol==2 or karte_stol==3 or karte_stol>7 : # 5 od boje,5 od skale
                if hand<4:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=26
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand==4 and karte_stol==1: #skala i nema 4 of boje
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=26
                    print('veliki raise') #  idemo do kraja
                elif hand==4 and (karte_stol==3 or karte_stol==2): # skala na stolu
                    if (jacina[0]-max(jacina[2:]))==1 or (jacina[1]-max(jacina[2:]))==1: # imam vecu od one na stolu
                        for i in range(blinds):  #koliko puta raiseat
                            mis2.click(1000,625) #raise jos
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=26
                        print('veliki raise') #  idemo do kraja
                    else:
                        if call==1:
                            mis2.click(750,670) # call
                            mis2.click(750,370) #makni ga sa gumba
                            print('call')
                            situacija=26
                        else:
                            mis2.click(630,670) #fold
                            print('fold')
                elif hand==4 and karte_stol>7: #ima 5 od boje
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=26
                    elif call==2 and postotak<0.30:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=26
                    elif call==3 and postotak<0.30: 
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=26
                        print('all in') #do kraja
                    else:
                         mis2.click(630,670) #fold
                         print('fold')
                elif hand==5 and karte_stol>7: #ima 5 od boje
                    if (znak[0]==znak[2] and jacina[0]>max(jacina[2:])) or (znak[1]==znak[2] and jacina[1]>max(jacina[2:])):
                        for i in range(blinds): #koliko puta raiseat
                            mis2.click(1000,625) #raise jos
                
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=26
                        print('veliki raise') #do kraja
                    elif (znak[0]==znak[2] or znak[1]==znak[2]):
                        if call==3:
                            mis2.click(930,670) #raise velik gumb
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=26
                            print('all in') #do kraja
                        else:
                            mis2.click(750,670) # call
                            mis2.click(750,370) #makni ga sa gumba
                            print('call')
                            situacija=26
                    else:
                        if call==1:
                            mis2.click(750,670) # call
                            mis2.click(750,370) #makni ga sa gumba
                            print('call')
                            situacija=26
                        elif call==2 and postotak<0.30:
                            mis2.click(750,670) # call
                            mis2.click(750,370) #makni ga sa gumba
                            print('call')
                            situacija=26
                        elif call==3 and postotak<0.30: 
                            mis2.click(930,670) #raise velik gumb
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=26
                            print('all in') #do kraja
                        else:
                             mis2.click(630,670) #fold
                             print('fold')

                        

                else:
                    for i in range(blinds): #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=26
                    print('veliki raise') #do kraja

                
            elif hand>=1: #dobio par ili vise, to je to
                for i in range(blinds):  #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                    
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                situacija=26
                print(' raise')
            elif call==1:
                mis2.click(750,670) # call
                mis2.click(750,370) #makni ga sa gumba
                print('call')
                situacija=26
            elif call>1:
                mis2.click(630,670) #fold
                print('fold')
                
        elif situacija2==27 or situacija2==28 : #mali rucni par+set
            hand=ruka.koja(jacina2,znak,call)
            karte_stol=nastolu.sto(jacina,znak)
            if karte_stol==4 or karte_stol==5 or karte_stol==1: # 4 od skale ili 4 od boje
                if hand==2 and jacina[2:].count(jacina[2])==1 and jacina[2:].count(jacina[3])==1 and jacina[2:].count(jacina[4])==1 and jacina[2:].count(jacina[5])==1 and jacina[2:].count(jacina[6])==1: 
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=27
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=27
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')

                elif hand<3:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=27
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand==3:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=27
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=27
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand==4 and karte_stol<4: #skala i nema 4 of boje
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=27
                    print('veliki raise') #  idemo do kraja
                elif hand==4 and karte_stol>3: #ima 4 od boje
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=27
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=27
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand>4:
                        for i in range(blinds):  #koliko puta raiseat
                            mis2.click(1000,625) #raise jos
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=27
                        print('veliki raise') #  idemo do kraja
                    
                        
                else:
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=27
                    print('veliki raise') #  idemo do kraja



            

            elif karte_stol==2 or karte_stol==3 or karte_stol>7 : # 5 od boje,5 od skale
                if hand<4:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=27
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand==4 and karte_stol==1: #skala i nema 4 of boje
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=27
                    print('veliki raise') #  idemo do kraja
                elif hand==4 and (karte_stol==3 or karte_stol==2): # skala na stolu
                    if (jacina[0]-max(jacina[2:]))==1 or (jacina[1]-max(jacina[2:]))==1: # imam vecu od one na stolu
                        for i in range(blinds):  #koliko puta raiseat
                            mis2.click(1000,625) #raise jos
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=27
                        print('veliki raise') #  idemo do kraja
                    else:
                        if call==1:
                            mis2.click(750,670) # call
                            mis2.click(750,370) #makni ga sa gumba
                            print('call')
                            situacija=27
                        else:
                            mis2.click(630,670) #fold
                            print('fold')
                elif hand==4 and karte_stol>7: #ima 5 od boje
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=27
                    elif call==2 and postotak<0.30:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=27
                    elif call==3 and postotak<0.30: 
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=27
                        print('all in') #do kraja
                    else:
                         mis2.click(630,670) #fold
                         print('fold')
                elif hand==5 and karte_stol>7: #ima 5 od boje
                    if (znak[0]==znak[2] and jacina[0]>max(jacina[2:])) or (znak[1]==znak[2] and jacina[1]>max(jacina[2:])):
                        for i in range(blinds): #koliko puta raiseat
                            mis2.click(1000,625) #raise jos
                
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=27
                        print('veliki raise') #do kraja
                    elif (znak[0]==znak[2] or znak[1]==znak[2]):
                        if call==3:
                            mis2.click(930,670) #raise velik gumb
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=27
                            print('all in') #do kraja
                        else:
                            mis2.click(750,670) # call
                            mis2.click(750,370) #makni ga sa gumba
                            print('call')
                            situacija=27
                    else:
                        if call==1:
                            mis2.click(750,670) # call
                            mis2.click(750,370) #makni ga sa gumba
                            print('call')
                            situacija=27
                        elif call==2 and postotak<0.30:
                            mis2.click(750,670) # call
                            mis2.click(750,370) #makni ga sa gumba
                            print('call')
                            situacija=27
                        elif call==3 and postotak<0.30: 
                            mis2.click(930,670) #raise velik gumb
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=27
                            print('all in') #do kraja
                        else:
                             mis2.click(630,670) #fold
                             print('fold')

                        

                else:
                    for i in range(blinds): #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=27
                    print('veliki raise') #do kraja

            
            else:
                for i in range(blinds/2): #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                situacija=27
                print('veliki raise') #do kraja


            
            
            
        elif situacija2==29: #mali rucni par,niko nije raise, ja nis
            hand=ruka.koja(jacina2,znak,call)

            karte_stol=nastolu.sto(jacina,znak)
            if karte_stol==4 or karte_stol==5 or karte_stol==1: # 4 od skale ili 4 od boje
                if hand==2 and jacina[2:].count(jacina[2])==1 and jacina[2:].count(jacina[3])==1 and jacina[2:].count(jacina[4])==1 and jacina[2:].count(jacina[5])==1 and jacina[2:].count(jacina[6])==1: 
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=29
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=29
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')

                elif hand<3:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=29
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand==3:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=29
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=29
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand==4 and karte_stol<4: #skala i nema 4 of boje
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=29
                    print('veliki raise') #  idemo do kraja
                elif hand==4 and karte_stol>3: #ima 4 od boje
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=29
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=29
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand>4:
                        for i in range(blinds):  #koliko puta raiseat
                            mis2.click(1000,625) #raise jos
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=29
                        print('veliki raise') #  idemo do kraja
                    
                        
                else:
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=29
                    print('veliki raise') #  idemo do kraja



            

            elif karte_stol==2 or karte_stol==3 or karte_stol>7 : # 5 od boje,5 od skale
                if hand<4:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=29
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand==4 and karte_stol==1: #skala i nema 4 of boje
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=29
                    print('veliki raise') #  idemo do kraja
                elif hand==4 and (karte_stol==3 or karte_stol==2): # skala na stolu
                    if (jacina[0]-max(jacina[2:]))==1 or (jacina[1]-max(jacina[2:]))==1: # imam vecu od one na stolu
                        for i in range(blinds):  #koliko puta raiseat
                            mis2.click(1000,625) #raise jos
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=29
                        print('veliki raise') #  idemo do kraja
                    else:
                        if call==1:
                            mis2.click(750,670) # call
                            mis2.click(750,370) #makni ga sa gumba
                            print('call')
                            situacija=29
                        else:
                            mis2.click(630,670) #fold
                            print('fold')
                elif hand==4 and karte_stol>7: #ima 5 od boje
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=29
                    elif call==2 and postotak<0.30:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=29
                    elif call==3 and postotak<0.30: 
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=29
                        print('all in') #do kraja
                    else:
                         mis2.click(630,670) #fold
                         print('fold')
                elif hand==5 and karte_stol>7: #ima 5 od boje
                    if (znak[0]==znak[2] and jacina[0]>max(jacina[2:])) or (znak[1]==znak[2] and jacina[1]>max(jacina[2:])):
                        for i in range(blinds): #koliko puta raiseat
                            mis2.click(1000,625) #raise jos
                
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=29
                        print('veliki raise') #do kraja
                    elif (znak[0]==znak[2] or znak[1]==znak[2]):
                        if call==3:
                            mis2.click(930,670) #raise velik gumb
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=29
                            print('all in') #do kraja
                        else:
                            mis2.click(750,670) # call
                            mis2.click(750,370) #makni ga sa gumba
                            print('call')
                            situacija=29
                    else:
                        if call==1:
                            mis2.click(750,670) # call
                            mis2.click(750,370) #makni ga sa gumba
                            print('call')
                            situacija=29
                        elif call==2 and postotak<0.30:
                            mis2.click(750,670) # call
                            mis2.click(750,370) #makni ga sa gumba
                            print('call')
                            situacija=29
                        elif call==3 and postotak<0.30: 
                            mis2.click(930,670) #raise velik gumb
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=29
                            print('all in') #do kraja
                        else:
                             mis2.click(630,670) #fold
                             print('fold')

                        

                else:
                    for i in range(blinds): #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=29
                    print('veliki raise') #do kraja

            
            elif hand>=3: #dobio tris ili vise, to je to
                for i in range(blinds): #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                situacija=29
                print('veliki raise') #do kraja

            elif  jacina[0]>=max(jacina):
                for i in range(blinds):  #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                print('veliki raise')
                situacija=29
            elif call==1 and velicina_pota<9:
                for i in range(blinds/2):  #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                print('veliki raise')
                situacija=29
            elif call==1:
                mis2.click(750,670) # call
                mis2.click(750,370) #makni ga sa gumba
                print('call')
                situacija=29
            elif call==2 and postotak<0.21:
                mis2.click(750,670) # call
                mis2.click(750,370) #makni ga sa gumba
                print('call')
                situacija=29
            elif call==3 and postotak<0.21:
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                print('all in')
                
            elif call>1:
                mis2.click(630,670) #fold
                print('fold')

            
        elif situacija2==30: #2 para i vise, s glupim slikama
            for i in range(blinds): #koliko puta raiseat
                mis2.click(1000,625) #raise jos
                
            mis2.click(930,670) #raise velik gumb
            mis2.click(750,370) #makni ga sa gumba
            situacija=30
            print('veliki raise') #do kraja
            
            
        elif situacija2==31: #neko raiseao, ja samo par, s glupim slikak, dobio 2 para, preispitat
            for i in range(blinds): #koliko puta raiseat
                mis2.click(1000,625) #raise jos
                
            mis2.click(930,670) #raise velik gumb
            mis2.click(750,370) #makni ga sa gumba
            situacija=31
            print('veliki raise') #do kraja
            
        elif situacija2==32: #ja samo par, s glupim slikama, checkirali svi
            hand=ruka.koja(jacina2,znak,call)
            if hand>=3: #dobio tris ili vise, to je to
                for i in range(blinds): #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                    
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                situacija=32
                print('veliki raise') #do kraja
            elif call==1:
                mis2.click(750,670) # call
                mis2.click(750,370) #makni ga sa gumba
                print('call')
                situacija=32
            elif call>1:
                mis2.click(630,670) #fold
                print('fold')
            
        elif situacija2==33: # dobio par, a niko nije raiseao prije toga
            hand=ruka.koja(jacina2,znak,call)
            if hand>=3: #dobio tris ili vise, to je to
                for i in range(blinds): #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                    
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                situacija=33
                print('veliki raise') #do kraja
            elif call==1:
                mis2.click(750,670) # call
                mis2.click(750,370) #makni ga sa gumba
                print('call')
                situacija=33
            elif call>1:
                mis2.click(630,670) #fold
                print('fold')
                
        elif situacija2==34: #niko ne raise,ja nisam imo nis,
            hand=ruka.koja(jacina2,znak,call)
            if hand>=3: #dobio tris ili vise, to je to
                for i in range(blinds): #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
            
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                situacija=34
                print('veliki raise') #do kraja
            elif call==1:
                mis2.click(750,670) # call
                mis2.click(750,370) #makni ga sa gumba
                print('call')
                situacija=34
            elif call>1:
                mis2.click(630,670) #fold
                print('fold')


        elif situacija2==112 or situacija2==114: # karte u boji, dobio 2 para i vise do kraja
            #karte_stol=nastolu.sto(jacina,znak)
            hand=ruka.koja(jacina2,znak,call)
            karte_stol=nastolu.sto(jacina,znak)
            if hand<3 and bjezi==1: #mega opasnost
                if call==1: #niko ne raise,ja nemam nis, check
                    mis2.click(750,670) #call
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=114
                    print('call')
                elif call>1: #raise, a ja nista nemam
                    mis2.click(630,670) #fold
                    print('fold')
            elif karte_stol==4 or karte_stol==5 or karte_stol==1: # 4 od skale ili 4 od boje
                if hand==2 and jacina[2:].count(jacina[2])==1 and jacina[2:].count(jacina[3])==1 and jacina[2:].count(jacina[4])==1 and jacina[2:].count(jacina[5])==1 and jacina[2:].count(jacina[6])==1: 
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=112
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=112
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand<3:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=112
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand==3:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=112
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=112
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand==4 and karte_stol<4: #skala i nema 4 of boje
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=112
                    print('veliki raise') #  idemo do kraja
                elif hand==4 and karte_stol>3: #ima 4 od boje
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=112
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=112
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand>4:
                        for i in range(blinds):  #koliko puta raiseat
                            mis2.click(1000,625) #raise jos
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=112
                        print('veliki raise') #  idemo do kraja
                    
                        
                else:
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=112
                    print('veliki raise') #  idemo do kraja



            

            elif karte_stol==2 or karte_stol==3 or karte_stol>7 : # 5 od boje,5 od skale
                if hand<4:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=112
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand==4 and karte_stol==1: #skala i nema 4 of boje
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=112
                    print('veliki raise') #  idemo do kraja
                elif hand==4 and (karte_stol==3 or karte_stol==2): # skala na stolu
                    if (jacina[0]-max(jacina[2:]))==1 or (jacina[1]-max(jacina[2:]))==1: # imam vecu od one na stolu
                        for i in range(blinds):  #koliko puta raiseat
                            mis2.click(1000,625) #raise jos
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=112
                        print('veliki raise') #  idemo do kraja
                    else:
                        if call==1:
                            mis2.click(750,670) # call
                            mis2.click(750,370) #makni ga sa gumba
                            print('call')
                            situacija=112
                        else:
                            mis2.click(630,670) #fold
                            print('fold')
                elif hand==4 and karte_stol>7: #ima 5 od boje
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=112
                    elif call==2 and postotak<0.30:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=112
                    elif call==3 and postotak<0.30: 
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=112
                        print('all in') #do kraja
                    else:
                         mis2.click(630,670) #fold
                         print('fold')
                elif hand==5 and karte_stol>7: #ima 5 od boje
                    if (znak[0]==znak[2] and jacina[0]>max(jacina[2:])) or (znak[1]==znak[2] and jacina[1]>max(jacina[2:])):
                        for i in range(blinds): #koliko puta raiseat
                            mis2.click(1000,625) #raise jos
                
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=112
                        print('veliki raise') #do kraja
                    elif (znak[0]==znak[2] or znak[1]==znak[2]):
                        if call==3:
                            mis2.click(930,670) #raise velik gumb
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=112
                            print('all in') #do kraja
                        else:
                            mis2.click(750,670) # call
                            mis2.click(750,370) #makni ga sa gumba
                            print('call')
                            situacija=112
                    else:
                        if call==1:
                            mis2.click(750,670) # call
                            mis2.click(750,370) #makni ga sa gumba
                            print('call')
                            situacija=112
                        elif call==2 and postotak<0.30:
                            mis2.click(750,670) # call
                            mis2.click(750,370) #makni ga sa gumba
                            print('call')
                            situacija=112
                        elif call==3 and postotak<0.30: 
                            mis2.click(930,670) #raise velik gumb
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=112
                            print('all in') #do kraja
                        else:
                             mis2.click(630,670) #fold
                             print('fold')

                        

                else:
                    for i in range(blinds): #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=112
                    print('veliki raise') #do kraja
            else:
                for i in range(blinds): #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                situacija=112
                print('veliki raise') #do kraja

        elif situacija2==113 or situacija2==115: # karte u boji, dizo na cekanje boje
            hand=ruka.koja(jacina2,znak,call)
            karte_stol=nastolu.sto(jacina,znak)
            if karte_stol==4 or karte_stol==5 or karte_stol==1: # 4 od skale ili 4 od boje
                if hand==2 and jacina[2:].count(jacina[2])==1 and jacina[2:].count(jacina[3])==1 and jacina[2:].count(jacina[4])==1 and jacina[2:].count(jacina[5])==1 and jacina[2:].count(jacina[6])==1: 
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=113
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=113
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand<3:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=113
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand==3:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=113
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=113
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand==4 and karte_stol<4: #skala i nema 4 of boje
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=113
                    print('veliki raise') #  idemo do kraja
                elif hand==4 and karte_stol>3: #ima 4 od boje
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=113
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=113
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand>4:
                        for i in range(blinds):  #koliko puta raiseat
                            mis2.click(1000,625) #raise jos
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=113
                        print('veliki raise') #  idemo do kraja
                    
                        
                else:
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=113
                    print('veliki raise') #  idemo do kraja



            

            elif karte_stol==2 or karte_stol==3 or karte_stol>7 : # 5 od boje,5 od skale
                if hand<4:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=113
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand==4 and karte_stol==1: #skala i nema 4 of boje
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=113
                    print('veliki raise') #  idemo do kraja
                elif hand==4 and (karte_stol==3 or karte_stol==2): # skala na stolu
                    if (jacina[0]-max(jacina[2:]))==1 or (jacina[1]-max(jacina[2:]))==1: # imam vecu od one na stolu
                        for i in range(blinds):  #koliko puta raiseat
                            mis2.click(1000,625) #raise jos
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=113
                        print('veliki raise') #  idemo do kraja
                    else:
                        if call==1:
                            mis2.click(750,670) # call
                            mis2.click(750,370) #makni ga sa gumba
                            print('call')
                            situacija=113
                        else:
                            mis2.click(630,670) #fold
                            print('fold')
                elif hand==4 and karte_stol>7: #ima 5 od boje
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=113
                    elif call==2 and postotak<0.30:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=113
                    elif call==3 and postotak<0.30: 
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=113
                        print('all in') #do kraja
                    else:
                         mis2.click(630,670) #fold
                         print('fold')
                elif hand==5 and karte_stol>7: #ima 5 od boje
                    if (znak[0]==znak[2] and jacina[0]>max(jacina[2:])) or (znak[1]==znak[2] and jacina[1]>max(jacina[2:])):
                        for i in range(blinds): #koliko puta raiseat
                            mis2.click(1000,625) #raise jos
                
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=113
                        print('veliki raise') #do kraja
                    elif (znak[0]==znak[2] or znak[1]==znak[2]):
                        if call==3:
                            mis2.click(930,670) #raise velik gumb
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=113
                            print('all in') #do kraja
                        else:
                            mis2.click(750,670) # call
                            mis2.click(750,370) #makni ga sa gumba
                            print('call')
                            situacija=113
                    else:
                        if call==1:
                            mis2.click(750,670) # call
                            mis2.click(750,370) #makni ga sa gumba
                            print('call')
                            situacija=113
                        elif call==2 and postotak<0.30:
                            mis2.click(750,670) # call
                            mis2.click(750,370) #makni ga sa gumba
                            print('call')
                            situacija=113
                        elif call==3 and postotak<0.30: 
                            mis2.click(930,670) #raise velik gumb
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=113
                            print('all in') #do kraja
                        else:
                             mis2.click(630,670) #fold
                             print('fold')

                        

                else:
                    for i in range(blinds): #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=113
                    print('veliki raise') #do kraja

            elif hand<3 and bjezi==1: #mega opasnost
                if call==1: #niko ne raise,ja nemam nis, check
                    mis2.click(750,670) #call
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=113
                    print('call')
                elif call>1: #raise, a ja nista nemam
                    mis2.click(630,670) #fold
                    print('fold')
            
            elif hand>=3: #dobio tris ili vise, to je to
                if situacija2==115:
                    for i in range(blinds):
                        mis2.click(1000,625) #raise jos
                else:
                    for i in range(blinds): #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                situacija=113
                print('veliki raise') #do kraja
                
            elif hand==2 and jacina[2:].count(jacina[2])==1 and jacina[2:].count(jacina[3])==1 and jacina[2:].count(jacina[4])==1 and jacina[2:].count(jacina[5])==1 and jacina[2:].count(jacina[6])==1:
            #2 prava para
        
                for i in range(blinds/2): #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                        
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                situacija=113
                print('veliki raise') #do kraja        
                
                        
            elif (hand==1 or hand==2) and (jacina[0]+jacina[1])>23: #imam aq i par
                for i in range(blinds/2): #koliko puta raiseat
                    mis2.click(1000,625) #raise jo
                        
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                situacija=113
                print('veliki raise') #do kraja


            elif (hand==1 or hand==2) and call==1: #imam najjaci par, niko raise
                if jacina.count(jacina[0])>1: #prva karta se uparila


                    if jacina[0]>=max(jacina[2:]) and opasni_igrac!=2 and opasni_igrac!=3: #najjaci par na stolu imam,niko nije raise  raise
                        if call==1 and (tri_od_boje==1 or jedan_za_skalu==1 or skala_dvije_strane==1) and len(vrste_igraca2)>0:
                            mis2.click(750,670) #call
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=113
                            print('call')
                        elif call==2 and postotak<0.51:
                            mis2.click(750,670) #call
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=113
                            print('call')
                        elif call==3 and postotak<0.51:
                            mis2.click(930,670) #raise velik gumb
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=113
                            print('all in')
                        else:
                            for i in range(blinds/2):  #koliko puta raiseat
                                mis2.click(1000,625) #raise jos
                            
                            mis2.click(930,670) #raise velik gumb
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=113
                            print('raise')
                    elif call==1 and len(vrste_igraca2)==0: #svi chekirali , ja neki sugavi par
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=120
                        print('veliki raise') #mini raise
                    elif call==1: #nemam najjaci par
                        mis2.click(750,670) #call
                        mis2.click(750,370) #makni ga sa gumba
                        print('1')
                        situacija=113
                        print('call')
                    elif call==2 and postotak<0.33 and opasni_igrac!=2 and opasni_igrac!=3:
                        mis2.click(750,670) #call
                        mis2.click(750,370) #makni ga sa gumba
                        print('1')
                        situacija=113
                        print('call')
                    elif call==3 and postotak<0.33 and opasni_igrac!=2 and opasni_igrac!=3:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=113
                        print('all in')
                    elif call>1:
                        mis2.click(630,670) #fold
                        mis2.click(750,370) #makni ga sa gumba
                        print('fold')
                    
                elif jacina.count(jacina[1])>1:#druga karta se uparila
                    if jacina[1]>=max(jacina[2:]) and opasni_igrac!=2 and opasni_igrac!=3: #najjaci par na stolu imam, niko nije raise , raise
                        if call==1 and (tri_od_boje==1 or jedan_za_skalu==1 or skala_dvije_strane==1) and len(vrste_igraca2)>0:
                            mis2.click(750,670) #call
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=113
                            print('call')
                        elif call==2 and postotak<0.51:
                            mis2.click(750,670) #call
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=113
                            print('call')
                        elif call==3 and postotak<0.51:
                            mis2.click(930,670) #raise velik gumb
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=113
                            print('all in')
                        else:
                            for i in range(blinds/2):  #koliko puta raiseat
                                mis2.click(1000,625) #raise jos
                            
                            mis2.click(930,670) #raise velik gumb
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=113
                            print('raise')
                    elif call==1 and len(vrste_igraca2)==0: #svi chekirali , ja neki sugavi par
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=120
                        print('veliki raise') #mini raise
                    elif call==1: #nemam najjaci par
                        mis2.click(750,670) #call
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=113
                        print('2')
                        print('call')
                    elif call==2 and postotak<0.33 and opasni_igrac!=2 and opasni_igrac!=3:
                        mis2.click(750,670) #call
                        mis2.click(750,370) #makni ga sa gumba
                        print('1')
                        situacija=113
                        print('call')
                    elif call==3 and postotak<0.33 and opasni_igrac!=2 and opasni_igrac!=3:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=113
                        print('all in')

                    elif call>1:
                        mis2.click(630,670) #fold
                        mis2.click(750,370) #makni ga sa gumba
                        print('fold')
                        
                else:
                    mis2.click(750,670) #call
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=113
                    print('3')
                    print('call')


            elif (hand==1 or hand==2) and call>1: #imam najjaci par, neko raise
                if jacina.count(jacina[0])>1: #prva karta se uparila
                    if jacina[0]>=max(jacina[2:]) and postotak<0.51 and opasni_igrac!=2 and opasni_igrac!=3: #najjaci par na stolu imam, call na njegov raise
                        if call==2:
                            mis2.click(750,670) #call
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=113
                            print('call')
                        elif call==3:
                            mis2.click(930,670) #raise velik gumb
                            mis2.click(750,370) #makni ga sa gumba
                            print('all in')
                    elif call==1: #nemam najjaci par
                        mis2.click(750,670) #call
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=113
                        print('4')
                        print('call')
                    elif call==2 and postotak<0.33 and opasni_igrac!=2 and opasni_igrac!=3:
                        mis2.click(750,670) #call
                        mis2.click(750,370) #makni ga sa gumba
                        print('1')
                        situacija=113
                        print('call')
                    elif call==3 and postotak<0.33 and opasni_igrac!=2 and opasni_igrac!=3:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=113
                        print('all in')
                    elif call>1:
                        mis2.click(630,670) #fold
                        mis2.click(750,370) #makni ga sa gumba
                        print('fold')
                    
                elif jacina.count(jacina[1])>1:#druga karta se uparila
                    if jacina[1]>=max(jacina[2:]) and postotak<0.51 and opasni_igrac!=2 and opasni_igrac!=3: #najjaci par na stolu imam, neko je raise, call
                        if call==2:
                            mis2.click(750,670) #call
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=113
                            print('call')
                        elif call==3:
                            mis2.click(930,670) #raise velik gumb
                            mis2.click(750,370) #makni ga sa gumba
                            print('all in')
                    elif call==1: #nemam najjaci par
                        mis2.click(750,670) #call
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=113
                        print('5')
                        print('call')
                    elif call==2 and postotak<0.33 and opasni_igrac!=2 and opasni_igrac!=3:
                        mis2.click(750,670) #call
                        mis2.click(750,370) #makni ga sa gumba
                        print('1')
                        situacija=113
                        print('call')
                    elif call==3 and postotak<0.33 and opasni_igrac!=2 and opasni_igrac!=3:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=113
                        print('all in')
                    elif call>1:
                        mis2.click(630,670) #fold
                        mis2.click(750,370) #makni ga sa gumba
                        print('fold')
                        
                else:
                    mis2.click(750,670) #call
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=113
                    print('6')
                    print('call')
                      

            

            elif call==1:
                mis2.click(750,670) # call
                mis2.click(750,370) #makni ga sa gumba
                print('call')
                situacija=113
            elif call>1:
                mis2.click(630,670) #fold
                print('fold')
    
        elif  situacija2==120 or situacija2==121: # on checkirao, pa sam raiseo na najjaci par , 2 para prava i vise raise, sve ostalo call, osim all in fold
            hand=ruka.koja(jacina2,znak,call)

            karte_stol=nastolu.sto(jacina,znak)
            if karte_stol==4 or karte_stol==5 or karte_stol==1: # 4 od skale ili 4 od boje
                if hand==2 and jacina[2:].count(jacina[2])==1 and jacina[2:].count(jacina[3])==1 and jacina[2:].count(jacina[4])==1 and jacina[2:].count(jacina[5])==1 and jacina[2:].count(jacina[6])==1: 
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=112
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=112
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand<3:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=120
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand==3:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=120
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=120
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand==4 and karte_stol<4: #skala i nema 4 of boje
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=120
                    print('veliki raise') #  idemo do kraja
                elif hand==4 and karte_stol>3: #ima 4 od boje
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=120
                    elif call==2 and postotak<0.34:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=120
                    elif call==3 and postotak<0.34:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        print('allin')
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand>4:
                        for i in range(blinds):  #koliko puta raiseat
                            mis2.click(1000,625) #raise jos
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=120
                        print('veliki raise') #  idemo do kraja
                    
                        
                else:
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=120
                    print('veliki raise') #  idemo do kraja



            

            elif karte_stol==2 or karte_stol==3 or karte_stol>7 : # 5 od boje,5 od skale
                if hand<4:
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=120
                    else:
                        mis2.click(630,670) #fold
                        print('fold')
                elif hand==4 and karte_stol==1: #skala i nema 4 of boje
                    for i in range(blinds):  #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=120
                    print('veliki raise') #  idemo do kraja
                elif hand==4 and (karte_stol==3 or karte_stol==2): # skala na stolu
                    if (jacina[0]-max(jacina[2:]))==1 or (jacina[1]-max(jacina[2:]))==1: # imam vecu od one na stolu
                        for i in range(blinds):  #koliko puta raiseat
                            mis2.click(1000,625) #raise jos
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=120
                        print('veliki raise') #  idemo do kraja
                    else:
                        if call==1:
                            mis2.click(750,670) # call
                            mis2.click(750,370) #makni ga sa gumba
                            print('call')
                            situacija=120
                        else:
                            mis2.click(630,670) #fold
                            print('fold')
                elif hand==4 and karte_stol>7: #ima 5 od boje
                    if call==1:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=120
                    elif call==2 and postotak<0.30:
                        mis2.click(750,670) # call
                        mis2.click(750,370) #makni ga sa gumba
                        print('call')
                        situacija=120
                    elif call==3 and postotak<0.30: 
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=120
                        print('all in') #do kraja
                    else:
                         mis2.click(630,670) #fold
                         print('fold')
                elif hand==5 and karte_stol>7: #ima 5 od boje
                    if (znak[0]==znak[2] and jacina[0]>max(jacina[2:])) or (znak[1]==znak[2] and jacina[1]>max(jacina[2:])):
                        for i in range(blinds): #koliko puta raiseat
                            mis2.click(1000,625) #raise jos
                
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=120
                        print('veliki raise') #do kraja
                    elif (znak[0]==znak[2] or znak[1]==znak[2]):
                        if call==3:
                            mis2.click(930,670) #raise velik gumb
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=120
                            print('all in') #do kraja
                        else:
                            mis2.click(750,670) # call
                            mis2.click(750,370) #makni ga sa gumba
                            print('call')
                            situacija=120
                    else:
                        if call==1:
                            mis2.click(750,670) # call
                            mis2.click(750,370) #makni ga sa gumba
                            print('call')
                            situacija=120
                        elif call==2 and postotak<0.30:
                            mis2.click(750,670) # call
                            mis2.click(750,370) #makni ga sa gumba
                            print('call')
                            situacija=120
                        elif call==3 and postotak<0.30: 
                            mis2.click(930,670) #raise velik gumb
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=120
                            print('all in') #do kraja
                        else:
                             mis2.click(630,670) #fold
                             print('fold')

                        

                else:
                    for i in range(blinds): #koliko puta raiseat
                        mis2.click(1000,625) #raise jos
                
                    mis2.click(930,670) #raise velik gumb
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=120
                    print('veliki raise') #do kraja

            elif hand<3 and bjezi==1: #mega opasnost
                if call==1: #niko ne raise,ja nemam nis, check
                    mis2.click(750,670) #call
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=120
                    print('call')
                elif call>1: #raise, a ja nista nemam
                    mis2.click(630,670) #fold
                    print('fold')
            

            elif hand>=3: #dobio tris ili vise, to je to
                for i in range(blinds): #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                    
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                situacija=120
                print('veliki raise') #do kraja
            elif hand==2 and jacina[2:].count(jacina[2])==1 and jacina[2:].count(jacina[3])==1 and jacina[2:].count(jacina[4])==1 and jacina[2:].count(jacina[5])==1 and jacina[2:].count(jacina[6])==1:
            #2 prava para

                
                for i in range(blinds): #koliko puta raiseat
                    mis2.click(1000,625) #raise jos

                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                situacija=120
                print('veliki raise') #do kraja
                
            
            elif (hand==1 or hand==2) and call==1: #imam najjaci par, niko raise
                if jacina.count(jacina[0])>1: #prva karta se uparila
                    if jacina[0]>=max(jacina[2:]) and opasni_igrac!=2 and opasni_igrac!=3: #najjaci par na stolu imam,niko nije raise  raise
                        if call==1 and (tri_od_boje==1 or jedan_za_skalu==1 or skala_dvije_strane==1) and len(vrste_igraca2)>0:
                            mis2.click(750,670) #call
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=120
                            print('call')
                        elif call==2 and postotak<0.51:
                            mis2.click(750,670) #call
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=120
                            print('call')
                        elif call==3 and postotak<0.51:
                            mis2.click(930,670) #raise velik gumb
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=120
                            print('all in')
                        else:
                            for i in range(blinds/2):  #koliko puta raiseat
                                mis2.click(1000,625) #raise jos
                            
                            mis2.click(930,670) #raise velik gumb
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=120
                            print('raise')
                    elif call==1 and len(vrste_igraca2)==0: #svi chekirali , ja neki sugavi par
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=120
                        print('veliki raise') #mini raise
                    elif call==1: #nemam najjaci par
                        mis2.click(750,670) #call
                        mis2.click(750,370) #makni ga sa gumba
                        print('1')
                        situacija=120
                        print('call')
                    elif call==2 and postotak<0.33 and opasni_igrac!=2 and opasni_igrac!=3:
                        mis2.click(750,670) #call
                        mis2.click(750,370) #makni ga sa gumba
                        print('1')
                        situacija=113
                        print('call')
                    elif call==3 and postotak<0.33 and opasni_igrac!=2 and opasni_igrac!=3:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=113
                        print('all in')
                    elif call>1:
                        mis2.click(630,670) #fold
                        mis2.click(750,370) #makni ga sa gumba
                        print('fold')
                    
                elif jacina.count(jacina[1])>1:#druga karta se uparila
                    if jacina[1]>=max(jacina[2:]) and opasni_igrac!=2 and opasni_igrac!=3: #najjaci par na stolu imam, niko nije raise , raise
                        if call==1 and (tri_od_boje==1 or jedan_za_skalu==1 or skala_dvije_strane==1) and len(vrste_igraca2)>0:
                            mis2.click(750,670) #call
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=120
                            print('call')
                        elif call==2 and postotak<0.51:
                            mis2.click(750,670) #call
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=120
                            print('call')
                        elif call==3 and postotak<0.51:
                            mis2.click(930,670) #raise velik gumb
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=120
                            print('all in')
                        else:
                            for i in range(blinds/2):  #koliko puta raiseat
                                mis2.click(1000,625) #raise jos
                            
                            mis2.click(930,670) #raise velik gumb
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=120
                            print('raise')
                    elif call==1 and len(vrste_igraca2)==0: #svi chekirali , ja neki sugavi par
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=120
                        print('veliki raise') #mini raise
                    elif call==1: #nemam najjaci par
                        mis2.click(750,670) #call
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=120
                        print('2')
                        print('call')
                    elif call==2 and postotak<0.33 and opasni_igrac!=2 and opasni_igrac!=3:
                        mis2.click(750,670) #call
                        mis2.click(750,370) #makni ga sa gumba
                        print('1')
                        situacija=113
                        print('call')
                    elif call==3 and postotak<0.33 and opasni_igrac!=2 and opasni_igrac!=3:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=113
                        print('all in')
                    elif call>1:
                        mis2.click(630,670) #fold
                        mis2.click(750,370) #makni ga sa gumba
                        print('fold')
                        
                else:
                    mis2.click(750,670) #call
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=120
                    print('3')
                    print('call')


            elif (hand==1 or hand==2) and call>1: #imam najjaci par, neko raise
                if jacina.count(jacina[0])>1: #prva karta se uparila
                    if jacina[0]>=max(jacina[2:]) and postotak<0.51 and opasni_igrac!=2 and opasni_igrac!=3: #najjaci par na stolu imam, call na njegov raise
                        if call==2:
                            mis2.click(750,670) #call
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=120
                            print('call')
                        elif call==3:
                            mis2.click(930,670) #raise velik gumb
                            mis2.click(750,370) #makni ga sa gumba
                            print('all in')
                        
                    elif call==1 and len(vrste_igraca2)==0: #svi chekirali , ja neki sugavi par
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=120
                        print('veliki raise') #mini raise    
                    elif call==1: #nemam najjaci par
                        mis2.click(750,670) #call
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=120
                        print('4')
                        print('call')
                    elif call==2 and postotak<0.33 and opasni_igrac!=2 and opasni_igrac!=3:
                        mis2.click(750,670) #call
                        mis2.click(750,370) #makni ga sa gumba
                        print('1')
                        situacija=113
                        print('call')
                    
                        
                    elif call==3 and postotak<0.33 and opasni_igrac!=2 and opasni_igrac!=3:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=113
                        print('all in')
                    elif call>1:
                        mis2.click(630,670) #fold
                        mis2.click(750,370) #makni ga sa gumba
                        print('fold')
                    
                elif jacina.count(jacina[1])>1:#druga karta se uparila
                    if jacina[1]>=max(jacina[2:]) and postotak<0.51 and opasni_igrac!=2 and opasni_igrac!=3: #najjaci par na stolu imam, neko je raise, call
                        if call==2:
                            mis2.click(750,670) #call
                            mis2.click(750,370) #makni ga sa gumba
                            situacija=120
                            print('call')
                        elif call==3:
                            mis2.click(930,670) #raise velik gumb
                            mis2.click(750,370) #makni ga sa gumba
                            print('all in')
                    elif call==1: #nemam najjaci par
                        mis2.click(750,670) #call
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=120
                        print('5')
                        print('call')
                    elif call==2 and postotak<0.33 and opasni_igrac!=2 and opasni_igrac!=3:
                        mis2.click(750,670) #call
                        mis2.click(750,370) #makni ga sa gumba
                        print('1')
                        situacija=113
                        print('call')
                    elif call==3 and postotak<0.33 and opasni_igrac!=2 and opasni_igrac!=3:
                        mis2.click(930,670) #raise velik gumb
                        mis2.click(750,370) #makni ga sa gumba
                        situacija=113
                        print('all in')
                    elif call>1:
                        mis2.click(630,670) #fold
                        mis2.click(750,370) #makni ga sa gumba
                        print('fold')
                        
                else:
                    mis2.click(750,670) #call
                    mis2.click(750,370) #makni ga sa gumba
                    situacija=120
                    print('6')
                    print('call')
                      

            
            elif call==1:
                mis2.click(750,670) # call
                mis2.click(750,370) #makni ga sa gumba
                print('call')
                situacija=120
            elif call>1:
                mis2.click(630,670) #fold
                print('fold')

                            
        elif situacija2==35: #peta situacija, lose karte, besplatni flop, ali dobio 2 para
            for i in range(blinds): #koliko puta raiseat
                mis2.click(1000,625) #raise jos
                
            mis2.click(930,670) #raise velik gumb
            mis2.click(750,370) #makni ga sa gumba
            situacija=35
            print('veliki raise') #do kraja
            
        elif situacija2==36: # dobio tris ili vise
            for i in range(blinds): #koliko puta raiseat
                mis2.click(1000,625) #raise jos
                
            mis2.click(930,670) #raise velik gumb
            mis2.click(750,370) #makni ga sa gumba
            situacija=36
            print('veliki raise') #do kraja
            
        elif situacija2==37: #nista ili par, niko ne raisea, lose karte
            hand=ruka.koja(jacina2,znak,call)
            if hand>=3: #dobio tris ili vise, to je to
                for i in range(blinds): #koliko puta raiseat
                    mis2.click(1000,625) #raise jos
                    
                mis2.click(930,670) #raise velik gumb
                mis2.click(750,370) #makni ga sa gumba
                situacija=37
                print('veliki raise') #do kraja
            elif call==1:
                mis2.click(750,670) # call
                mis2.click(750,370) #makni ga sa gumba
                print('call')
                situacija=37
            elif call>1:
                mis2.click(630,670) #fold
                print('fold')
            

    return situacija
    #print(jacina[2])
    
