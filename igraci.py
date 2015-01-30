from PIL import Image
from PIL import ImageChops
import oduzmi
import folder

def podaci(slika,pomak,pomak2): #koliko para igrac ima?
    dir=folder.get()
    im = Image.open(dir+'slika.jpg')

    if slika==1:
        size=(298-pomak2,485+pomak,400-pomak2,500+pomak) #povecat za 1 kad bude trebalo
        im2=im.crop(size) 
        im3=im2.convert('P').convert('1')
        pix1 = im3.load()
        im3.save(dir+'novac1.jpg') #novac1

        

    
    elif slika==2:
        size=(26-pomak2,406+pomak,128-pomak2,421+pomak) #povecat za 1 kad bude trebalo
        im2=im.crop(size) 
        im3=im2.convert('P').convert('1')
        pix1 = im3.load()
        im3.save(dir+'novac2.jpg') #novac2

        


    elif slika==3:
        size=(21-pomak2,169+pomak,123-pomak2,184+pomak) #povecat za 1 kad bude trebalo
        im2=im.crop(size) 
        im3=im2.convert('P').convert('1')
        pix1 = im3.load()
        im3.save(dir+'novac3.jpg') #novac3

        

    elif slika==4:
        size=(905-pomak2,169+pomak,1007-pomak2,184+pomak) #povecat za 1 kad bude trebalo
        im2=im.crop(size) 
        im3=im2.convert('P').convert('1')
        pix1 = im3.load()
        im3.save(dir+'novac4.jpg') #novac4

        

    elif slika==5:
        size=(896-pomak2,405+pomak,998-pomak2,420+pomak) #povecat za 1 kad bude trebalo
        im2=im.crop(size) 
        im3=im2.convert('P').convert('1')
        pix1 = im3.load()
        im3.save(dir+'novac5.jpg') #novac5

        

    elif slika==6:
        size=(632-pomak2,485+pomak,734-pomak2,500+pomak) #povecat za 1 kad bude trebalo
        im2=im.crop(size) 
        im3=im2.convert('P').convert('1')
        pix1 = im3.load()
        im3.save(dir+'novac6.jpg') #novac6


    
    
    

        
    pomoc4=[]
    pomoc3=[]
    pomoc2=[]
    b=0
    for i in range(102):
        for j in range(15):#novac
            if pix1[i,j]>0:
                b+=1
        pomoc4.append(b)
        b=0
    #print(pomoc) #ime
    #print(pomoc2) #novac
    for i in range(102):
        for j in range(15):
            if pix1[i,j]==0:
                b+=1
        pomoc3.append(b)
        b=0

    #print (sum(pomoc3),sum(pomoc4))
    if sum(pomoc3)>1450 or sum(pomoc4)<50:
        return 0
    if sum(pomoc3)<sum(pomoc4):
        pomoc2=pomoc3[:]
        situacija=2 #svjetleca situacija
    else:
        pomoc2=pomoc4[:]
        situacija=1 # normalna situacija

    #print(pomoc2)
    z=1
    broj13=0
    while z: #makni sve nule do prvog znaka
        if len(pomoc2)>0:
            if pomoc2[0]==0:
                pomoc2.remove(0)
                broj13+=1
            else:
                z=0
    #print (pomoc2)
    #print(sum(pomoc2))
    #print(broj13)
    novi=[]
    novi=pomoc2[:]
    z=1
    broj=0
    broj2=0
    nule_gdje=[]
    prevelik=0
    while (z): #
        try:
            nule_gdje.append(novi.index(0)+broj)
        except ValueError:
            z=0
            continue
        else:
            broj2+=1
            
        
        if len(nule_gdje)>1:
            #print(len(nule_gdje))
            #print(broj)
            if (nule_gdje[broj]-nule_gdje[broj-1])>12:
                #broj-=1
                #broj2+=1
                nule_gdje.pop()
                try:
                    novi[(nule_gdje[broj-1]+5-broj2)+novi[(nule_gdje[broj-1]+5-broj2):].index(1)]=0
                except ValueError:
                    try:
                        novi[(nule_gdje[broj-1]+5-broj2)+novi[(nule_gdje[broj-1]+5-broj2):].index(2)]=0
                    except ValueError:
                        try:    
                            novi[(nule_gdje[broj-1]+5-broj2)+novi[(nule_gdje[broj-1]+5-broj2):].index(3)]=0
                        except ValueError:
                            return 99999999999
               
                #print(novi[(nule_gdje[broj-1]+5-broj2):].index(1))
                #print(novi[(nule_gdje[broj-1]+5-broj2):])
                #print(novi)
                continue
                #prevelik=1
        novi.remove(0)
        broj+=1
    #print (nule_gdje)
    #print(broj2)
    broj=0
    #while prevelik:
        #print(prevelik)
            
     #   prevelik=0
        
    if situacija==1:   
        zeroth=[9, 10, 6, 4, 7, 10, 9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        first=[2, 2, 3, 11, 11,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        second=[5, 7, 7, 7, 7, 8, 6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
       
        third=[4, 7, 6, 6, 8, 11, 8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        third2=[4, 7, 6, 6, 8, 11, 8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        
        fourth=[3, 5, 6, 6, 11, 11, 2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        fifth=[8, 10, 9, 6, 8, 10, 7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        fifth2=[8, 10, 9, 6, 8, 10, 7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        
        sixth=[7, 10, 9, 6, 8, 10, 7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        seventh=[2, 6, 9, 8, 6, 4, 3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        eigth=[6, 11, 10, 6, 8, 11, 8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        nineth=[7, 10, 8, 6, 9, 9, 7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif situacija==2:
        zeroth=[5, 9, 4, 4, 4, 9, 5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        first=[2, 2, 3, 11, 11,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        second=[3, 6, 6, 6, 6, 7, 4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        third=[1, 5, 4, 6, 6, 9, 5, 8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        third2=[5, 5, 6, 6, 7, 10, 6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        fourth=[3, 5, 6, 6, 11, 11, 2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        fifth=[9, 6, 6, 6, 8, 6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        fifth2=[2, 9, 6, 6, 6, 8, 6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        sixth=[5, 9, 4, 6, 6, 7, 3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        seventh=[2, 6, 9, 8, 6, 4, 3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        eigth=[4, 9, 6, 6, 6, 9, 5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        nineth=[4, 7, 6, 6, 5, 9, 5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    broj3=0
    potraga=[]
    oduz=[]
    vjerojatnost=[]
    if len(nule_gdje)<1:
        return 99999999999
    broj3=nule_gdje[0]+1
    #print(nule_gdje)
    broj14=[]
    brojilo=-1
    for i in nule_gdje:
            
        if len(pomoc2[broj3:i])>1:
            broj14.append(broj3)
            broj14.append(i)
            #print(pomoc2[broj3:i])

       
            if pomoc2[broj3:i]==[2,2]:
                potraga.append(10)
                brojilo+=1
            else:
                oduz=oduzmi.liste(pomoc2[broj3:i],zeroth)
                vjerojatnost.append(sum(oduz))
               
                oduz=oduzmi.liste(pomoc2[broj3:i],first)
                vjerojatnost.append(sum(oduz))
                
                oduz=oduzmi.liste(pomoc2[broj3:i],second)
                vjerojatnost.append(sum(oduz))
                
            
                oduz=oduzmi.liste(pomoc2[broj3:i],third)
                vjerojatnost.append(sum(oduz))
                oduz=oduzmi.liste(pomoc2[broj3:i],third2)
                vjerojatnost.append(sum(oduz))
               
        
                oduz=oduzmi.liste(pomoc2[broj3:i],fourth)
                vjerojatnost.append(sum(oduz))
                oduz=oduzmi.liste(pomoc2[broj3:i],fifth)
                vjerojatnost.append(sum(oduz))
                oduz=oduzmi.liste(pomoc2[broj3:i],fifth2)
                vjerojatnost.append(sum(oduz))
                
                oduz=oduzmi.liste(pomoc2[broj3:i],sixth)
                vjerojatnost.append(sum(oduz))
                
                oduz=oduzmi.liste(pomoc2[broj3:i],seventh)
                vjerojatnost.append(sum(oduz))
                oduz=oduzmi.liste(pomoc2[broj3:i],eigth)
                vjerojatnost.append(sum(oduz))
                
                oduz=oduzmi.liste(pomoc2[broj3:i],nineth)
                vjerojatnost.append(sum(oduz))

                
                
                if vjerojatnost.index(min(vjerojatnost))>6:
                    potraga.append(vjerojatnost.index(min(vjerojatnost))-2)
                elif vjerojatnost.index(min(vjerojatnost))>3:
                    potraga.append(vjerojatnost.index(min(vjerojatnost))-1)

                else:
                    potraga.append(vjerojatnost.index(min(vjerojatnost)))
                brojilo+=1
                #print(potraga[brojilo],(broj13+broj3))
                #if potraga[brojilo]==5 and situacija==2:
                   # if pix1[(broj13+broj3),9]==0
                   # elif pix1[(broj13+broj3),8]!=0:
                        
                     #   potraga.pop()
                    #    potraga.append(6)
                #elif potraga[brojilo]==6 and situacija==2:
                   # if pix1[(broj13+broj3),8]==0:
                    #    potraga.pop()
                    #    potraga.append(5)
                #print(potraga[brojilo])
                if potraga[brojilo]==5 and situacija==1:
                    if pix1[(broj13+broj3),9]==0:
                        potraga.pop()
                        potraga.append(9)
                    elif pix1[(broj13+broj3),8]!=0 and pix1[(broj13+broj3+6),5]==0:
                        potraga.pop()
                        potraga.append(6)
                    elif pix1[(broj13+broj3),8]!=0:
                        potraga.pop()
                        potraga.append(8)
                elif potraga[brojilo]==6 and situacija==1:
                    if pix1[(broj13+broj3),9]==0:
                        potraga.pop()
                        potraga.append(9)
                    elif pix1[(broj13+broj3),8]==0:
                        potraga.pop()
                        potraga.append(5)
                    elif pix1[(broj13+broj3+6),5]>0:
                        potraga.pop()
                        potraga.append(8)
                elif potraga[brojilo]==9 and situacija==1:
                    if pix1[(broj13+broj3),9]!=0 and pix1[(broj13+broj3),8]!=0 and pix1[(broj13+broj3+6),5]==0:
                        potraga.pop()
                        potraga.append(6)
                    elif pix1[(broj13+broj3),8]==0 and pix1[(broj13+broj3),9]!=0:
                        potraga.pop()
                        potraga.append(5)
                    elif pix1[(broj13+broj3+6),5]>0 and pix1[(broj13+broj3),9]!=0 and pix1[(broj13+broj3),8]!=0:
                        potraga.pop()
                        potraga.append(8)
                elif potraga[brojilo]==8 and situacija==1:
                    if pix1[(broj13+broj3+6),5]==0:
                        potraga.pop()
                        potraga.append(6)
                
        vjerojatnost=[]
        broj3=i+1

    #print(potraga)
    jakost=100
    if potraga.count(10)>0:
        potraga.remove(10)
        jakost=1

    dizati=0
    
    for i in range(len(potraga)):
        dizati+=potraga[i]*jakost*(10**(len(potraga)-1-i))

    #print 'igrac%(broj1)d ima %(broj2).2f $  ' %{"broj1": slika, "broj2": (float(dizati)/100)}
    
    
    






    #print(broj14)
    #print(pomoc2)
    
    if dizati>1000000:
        return 0
    return (dizati)










    
