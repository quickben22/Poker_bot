from PIL import Image
from PIL import ImageChops
import oduzmi
import folder

def pamti(broj,pomak,pomak2):
    dir=folder.get()
    im = Image.open(dir+'slika.jpg')

    if broj==1:
        size=(298-pomak2,467+pomak,400-pomak2,482+pomak) #povecat za 1 kad bude trebalo
        im2=im.crop(size) 
        im3=im2.convert('P').convert('1')
        pix2 = im3.load()
        im3.save(dir+'ime1.jpg') #ime1
    elif broj==2:
        size=(26-pomak2,387+pomak,128-pomak2,402+pomak) #povecat za 1 kad bude trebalo
        im2=im.crop(size) 
        im3=im2.convert('P').convert('1')
        pix2 = im3.load()
        im3.save(dir+'ime2.jpg') #ime2
    elif broj==3:
        size=(21-pomak2,148+pomak,123-pomak2,163+pomak) #povecat za 1 kad bude trebalo
        im2=im.crop(size) 
        im3=im2.convert('P').convert('1')
        pix2 = im3.load()
        im3.save(dir+'ime3.jpg') #ime3
    elif broj==4:

        size=(905-pomak2,148+pomak,1007-pomak2,163+pomak) #povecat za 1 kad bude trebalo
        im2=im.crop(size) 
        im3=im2.convert('P').convert('1')
        pix2 = im3.load()
        im3.save(dir+'ime4.jpg') #ime4
    elif broj==5:

        size=(896-pomak2,386+pomak,998-pomak2,401+pomak) #povecat za 1 kad bude trebalo
        im2=im.crop(size) 
        im3=im2.convert('P').convert('1')
        pix2 = im3.load()
        im3.save(dir+'ime5.jpg') #ime5

   # size=(632-pomak2,467+pomak,734-pomak2,482+pomak) #povecat za 1 kad bude trebalo
   # im2=im.crop(size) 
   # im3=im2.convert('P').convert('1')
   # pix2 = im3.load()
   # im3.save('ime6.jpg') #ime6

    

    
    pomoc4=[]
    pomoc3=[]
    pomoc2=[]
    b=0
    for i in range(102):
        for j in range(15):#ime
            if pix2[i,j]>0:
                b+=1
        pomoc4.append(b)
        b=0
    #print(pomoc) #ime
    #print(pomoc2) #novac
    for i in range(102):
        for j in range(15):
            if pix2[i,j]==0:
                b+=1
        pomoc3.append(b)
        b=0

    
    #print (sum(pomoc3),sum(pomoc4))
    if sum(pomoc3)>1450 or sum(pomoc4)<50:
        return 'xxxxxxxx'
    if sum(pomoc3)<sum(pomoc4):
        pomoc2=pomoc3[:]
        situacija=2 #svjetleca situacija
    else:
        pomoc2=pomoc4[:]
        situacija=1 # normalna situacija

    #print(pomoc2)
    z=1
    broj13=0
    while z:
        if len(pomoc2)>0:
            if pomoc2[0]==0:
                pomoc2.remove(0)
                broj13+=1
            else:
                pomoc2.insert(0,0)
                broj13-=1
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
                            #print((nule_gdje[broj-1]+5-broj2))
                            #print( novi[(nule_gdje[broj-1]+5-broj2):])
                            novi[(nule_gdje[broj-1]+5-broj2)+novi[(nule_gdje[broj-1]+5-broj2):].index(3)]=0
                        except ValueError:
                            try:
                                #print((nule_gdje[broj-1]+5-broj2))
                                #print( novi[(nule_gdje[broj-1]+5-broj2):])
                                novi[(nule_gdje[broj-1]+5-broj2)+novi[(nule_gdje[broj-1]+5-broj2):].index(3)]=0
                            except ValueError:
                                try:
                                    #print((nule_gdje[broj-1]+5-broj2))
                                    #print( novi[(nule_gdje[broj-1]+5-broj2):])
                                    novi[(nule_gdje[broj-1]+5-broj2)+novi[(nule_gdje[broj-1]+5-broj2):].index(4)]=0
                                except ValueError:
                                    try:
                                        #print((nule_gdje[broj-1]+5-broj2))
                                        #print( novi[(nule_gdje[broj-1]+5-broj2):])
                                        novi[(nule_gdje[broj-1]+5-broj2)+novi[(nule_gdje[broj-1]+5-broj2):].index(5)]=0
                                    except ValueError:
                                        try:
                                            #print((nule_gdje[broj-1]+5-broj2))
                                            #print( novi[(nule_gdje[broj-1]+5-broj2):])
                                            novi[(nule_gdje[broj-1]+5-broj2)+novi[(nule_gdje[broj-1]+5-broj2):].index(6)]=0
                                        except ValueError:
                                            try:
                                                #print((nule_gdje[broj-1]+5-broj2))
                                                #print( novi[(nule_gdje[broj-1]+5-broj2):])
                                                novi[(nule_gdje[broj-1]+5-broj2)+novi[(nule_gdje[broj-1]+5-broj2):].index(7)]=0
                                            except ValueError:
                                                return 'xxxxxxxx'
               
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
        
        fourth=[3, 5, 6, 6, 11, 11, 2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        fifth=[8, 10, 9, 6, 8, 10, 7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        
        sixth=[7, 10, 9, 6, 8, 10, 7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        seventh=[2, 6, 9, 8, 6, 4, 3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        eigth=[6, 11, 10, 6, 8, 11, 8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        nineth=[7, 10, 8, 6, 9, 9, 7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        aa=[4, 6, 6, 7, 8, 8, 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        bb=[11, 11, 6, 4, 6, 8, 6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        cc=[5, 8, 5, 5, 6, 4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        dd=[5, 8, 6, 4, 6, 11, 11,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ee=[4, 8, 7, 6, 6, 7, 4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ff=[2, 11, 11, 4, 4, 2, 2, 2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        gg=[8, 10, 8, 5, 7, 10, 10,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        hh=[11, 11, 2, 2, 2, 8, 7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ii=[10,10,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        jj=[1, 1, 12, 12,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        kk=[11, 11, 3, 5, 8, 4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ll=[11, 11,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        mm=[8, 8, 2, 2, 8, 8, 3, 2, 8, 7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        nn=[8, 8, 3, 2, 2, 8, 8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        oo=[4, 8, 6, 4, 6, 8, 5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        pp=[10, 10, 6, 4, 7, 7, 6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        qq=[5, 8, 6, 4, 5, 10, 10,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        rr=[8, 8, 3, 2, 2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ss=[4, 7, 6, 6, 7, 4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        tt=[2, 10, 10, 4, 4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        uu=[7, 8, 3, 2, 3, 8, 8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        vv=[1, 3, 6, 6, 3, 5, 6, 3, 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ww=[2, 6, 8, 4, 8, 4, 8, 4, 7, 6, 2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        xx=[4, 8, 6, 6, 8, 4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        xx2=[1, 4, 8, 5, 6, 8, 4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        yy=[3, 7, 9, 6, 8, 6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        zz=[5, 6, 7, 7, 6, 5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        dot=[1, 1, 1, 1, 1, 1, 1, 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif situacija==2:
        zeroth=[5, 9, 4, 4, 4, 9, 5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        first=[2, 2, 3, 11, 11,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        second=[3, 6, 6, 6, 6, 7, 4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        third=[1, 5, 4, 6, 6, 9, 5, 8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        fourth=[3, 5, 6, 6, 11, 11, 2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        fifth=[9, 6, 6, 6, 8, 6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        sixth=[5, 9, 4, 6, 6, 7, 3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        seventh=[2, 6, 9, 8, 6, 4, 3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        eigth=[4, 9, 6, 6, 6, 9, 5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        nineth=[4, 7, 6, 6, 5, 9, 5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        aa=[2, 6, 4, 4, 7, 7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        bb=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        cc=[4, 6, 4, 4, 4, 2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        dd=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ee=[4, 6, 6, 6, 6, 5, 3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ff=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        gg=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        hh=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ii=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        jj=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        kk=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ll=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        mm=[8, 8, 1, 2, 8, 7, 1, 2, 8, 7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        nn=[8, 8, 1, 2, 2, 8, 7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        oo=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        pp=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        qq=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        rr=[8, 8, 1, 2, 2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ss=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        tt=[2, 8, 9, 4, 3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        uu=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        vv=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ww=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        xx=[2, 6, 4, 3, 6, 2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        xx2=[2, 6, 4, 3, 6, 2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        
        yy=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        zz=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        dot=[1, 1, 1, 1, 1, 1, 1, 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        
    broj3=0
    potraga='-'
    oduz=[]
    vjerojatnost=[]
    broj3=nule_gdje[0]+1
    #print(nule_gdje)
    broj14=[]
    brojilo=0
    for i in nule_gdje:
            
        if len(pomoc2[broj3:i])>1:
            broj14.append(broj3)
            broj14.append(i)
            #print(pomoc2[broj3:i])

       
            if pomoc2[broj3:i]==[2,2]:
                potraga+='.'
                brojilo+=1
            else:
                za_oduzimane=[]
                za_oduzimanje=pomoc2[broj3:i]
                za_oduzimanje.append(0)
                za_oduzimanje.append(0)
                oduz=oduzmi.liste(za_oduzimanje,zeroth)
                vjerojatnost.append(sum(oduz))
               
                oduz=oduzmi.liste(za_oduzimanje,first)
                vjerojatnost.append(sum(oduz))
                
                oduz=oduzmi.liste(za_oduzimanje,second)
                vjerojatnost.append(sum(oduz))
                
            
                oduz=oduzmi.liste(za_oduzimanje,third)
                vjerojatnost.append(sum(oduz))
               
        
                oduz=oduzmi.liste(za_oduzimanje,fourth)
                vjerojatnost.append(sum(oduz))
                oduz=oduzmi.liste(za_oduzimanje,fifth)
                vjerojatnost.append(sum(oduz))
                
                oduz=oduzmi.liste(za_oduzimanje,sixth)
                vjerojatnost.append(sum(oduz))
                
                oduz=oduzmi.liste(za_oduzimanje,seventh)
                vjerojatnost.append(sum(oduz))
                oduz=oduzmi.liste(za_oduzimanje,eigth)
                vjerojatnost.append(sum(oduz))
                oduz=oduzmi.liste(za_oduzimanje,nineth)
                vjerojatnost.append(sum(oduz))
                oduz=oduzmi.liste(za_oduzimanje,aa)
                vjerojatnost.append(sum(oduz))
                oduz=oduzmi.liste(za_oduzimanje,bb)
                vjerojatnost.append(sum(oduz))
                oduz=oduzmi.liste(za_oduzimanje,cc)
                vjerojatnost.append(sum(oduz))
                oduz=oduzmi.liste(za_oduzimanje,dd)
                vjerojatnost.append(sum(oduz))
                oduz=oduzmi.liste(za_oduzimanje,ee)
                vjerojatnost.append(sum(oduz))
                oduz=oduzmi.liste(za_oduzimanje,ff)
                vjerojatnost.append(sum(oduz))
                oduz=oduzmi.liste(za_oduzimanje,gg)
                vjerojatnost.append(sum(oduz))
                oduz=oduzmi.liste(za_oduzimanje,hh)
                vjerojatnost.append(sum(oduz))
                oduz=oduzmi.liste(za_oduzimanje,ii)
                vjerojatnost.append(sum(oduz))
                oduz=oduzmi.liste(za_oduzimanje,jj)
                vjerojatnost.append(sum(oduz))
                oduz=oduzmi.liste(za_oduzimanje,kk)
                vjerojatnost.append(sum(oduz))
                oduz=oduzmi.liste(za_oduzimanje,ll)
                vjerojatnost.append(sum(oduz))
                oduz=oduzmi.liste(za_oduzimanje,mm)
                vjerojatnost.append(sum(oduz))
                oduz=oduzmi.liste(za_oduzimanje,nn)
                vjerojatnost.append(sum(oduz))
                oduz=oduzmi.liste(za_oduzimanje,oo)
                vjerojatnost.append(sum(oduz))
                oduz=oduzmi.liste(za_oduzimanje,pp)
                vjerojatnost.append(sum(oduz))
                oduz=oduzmi.liste(za_oduzimanje,qq)
                vjerojatnost.append(sum(oduz))
                oduz=oduzmi.liste(za_oduzimanje,rr)
                vjerojatnost.append(sum(oduz))
                oduz=oduzmi.liste(za_oduzimanje,ss)
                vjerojatnost.append(sum(oduz))
                oduz=oduzmi.liste(za_oduzimanje,tt)
                vjerojatnost.append(sum(oduz))
                oduz=oduzmi.liste(za_oduzimanje,uu)
                vjerojatnost.append(sum(oduz))
                oduz=oduzmi.liste(za_oduzimanje,vv)
                vjerojatnost.append(sum(oduz))
                oduz=oduzmi.liste(za_oduzimanje,ww)
                vjerojatnost.append(sum(oduz))
                oduz=oduzmi.liste(za_oduzimanje,xx)
                vjerojatnost.append(sum(oduz))
                
                oduz=oduzmi.liste(za_oduzimanje,yy)
                vjerojatnost.append(sum(oduz))
                oduz=oduzmi.liste(za_oduzimanje,zz)
                vjerojatnost.append(sum(oduz))
                oduz=oduzmi.liste(za_oduzimanje,xx2)
                vjerojatnost.append(sum(oduz))
                oduz=oduzmi.liste(za_oduzimanje,dot)
                vjerojatnost.append(sum(oduz))

                if vjerojatnost.index(min(vjerojatnost))==0:
                    potraga+='0'
                
                elif vjerojatnost.index(min(vjerojatnost))==1:
                    potraga+='1'
                elif vjerojatnost.index(min(vjerojatnost))==2:
                    potraga+='2'
                elif vjerojatnost.index(min(vjerojatnost))==3:
                    potraga+='3'
                elif vjerojatnost.index(min(vjerojatnost))==4:
                    potraga+='4'
                elif vjerojatnost.index(min(vjerojatnost))==5:
                    potraga+='5'
                elif vjerojatnost.index(min(vjerojatnost))==6:
                    potraga+='6'
                elif vjerojatnost.index(min(vjerojatnost))==7:
                    potraga+='7'
                elif vjerojatnost.index(min(vjerojatnost))==8:
                    potraga+='8'
                elif vjerojatnost.index(min(vjerojatnost))==9:
                    potraga+='9'

                elif vjerojatnost.index(min(vjerojatnost))==10:
                    potraga+='a'
                elif vjerojatnost.index(min(vjerojatnost))==11:
                    potraga+='b'
                elif vjerojatnost.index(min(vjerojatnost))==12:
                    potraga+='c'
                elif vjerojatnost.index(min(vjerojatnost))==13:
                    potraga+='d'
                elif vjerojatnost.index(min(vjerojatnost))==14:
                    potraga+='e'
                elif vjerojatnost.index(min(vjerojatnost))==15:
                    potraga+='f'
                elif vjerojatnost.index(min(vjerojatnost))==16:
                    potraga+='g'
                elif vjerojatnost.index(min(vjerojatnost))==17:
                    potraga+='h'
                elif vjerojatnost.index(min(vjerojatnost))==18:
                    potraga+='i'
                elif vjerojatnost.index(min(vjerojatnost))==19:
                    potraga+='j'
                elif vjerojatnost.index(min(vjerojatnost))==20:
                    potraga+='k'
                elif vjerojatnost.index(min(vjerojatnost))==21:
                    potraga+='l'
                elif vjerojatnost.index(min(vjerojatnost))==22:
                    potraga+='m'
                elif vjerojatnost.index(min(vjerojatnost))==23:
                    potraga+='r'
                elif vjerojatnost.index(min(vjerojatnost))==24:
                    potraga+='o'
                elif vjerojatnost.index(min(vjerojatnost))==25:
                    potraga+='b'
                elif vjerojatnost.index(min(vjerojatnost))==26:
                    potraga+='q'
                elif vjerojatnost.index(min(vjerojatnost))==27:
                    potraga+='r'
                elif vjerojatnost.index(min(vjerojatnost))==28:
                    potraga+='s'
                elif vjerojatnost.index(min(vjerojatnost))==29:
                    potraga+='t'
                elif vjerojatnost.index(min(vjerojatnost))==30:
                    potraga+='u'
                elif vjerojatnost.index(min(vjerojatnost))==31:
                    potraga+='v'
                elif vjerojatnost.index(min(vjerojatnost))==32:
                    potraga+='w'
                elif vjerojatnost.index(min(vjerojatnost))==33:
                    potraga+='x'
                elif vjerojatnost.index(min(vjerojatnost))==34:
                    potraga+='y'
                elif vjerojatnost.index(min(vjerojatnost))==35:
                    potraga+='z'
                elif vjerojatnost.index(min(vjerojatnost))==36:
                    potraga+='x'
                elif vjerojatnost.index(min(vjerojatnost))==37:
                    potraga+='_'
                    
                brojilo+=1
                
                #print(potraga)    
                if potraga[brojilo]=='5' and situacija==1:
                    if pix2[(broj13+broj3),9]==0:
                        potraga=potraga[:brojilo]+'9'
                    elif pix2[(broj13+broj3),8]!=0 and pix2[(broj13+broj3+6),5]==0:
                        potraga=potraga[:brojilo]+'6'
                    elif pix2[(broj13+broj3),8]!=0:
                        potraga=potraga[:brojilo]+'8'
                        
                elif potraga[brojilo]=='6' and situacija==1:
                    if pix2[(broj13+broj3),9]==0:
                        potraga=potraga[:brojilo]+'9'
                    elif pix2[(broj13+broj3),8]==0:
                        potraga=potraga[:brojilo]+'5'
                    elif pix2[(broj13+broj3+6),5]>0:
                        potraga=potraga[:brojilo]+'8'
                        
                elif potraga[brojilo]=='9' and situacija==1:
                    if pix2[(broj13+broj3),9]!=0 and pix2[(broj13+broj3),8]!=0 and pix2[(broj13+broj3+6),5]==0:
                        potraga=potraga[:brojilo]+'6'
                    elif pix2[(broj13+broj3),8]==0 and pix2[(broj13+broj3),9]!=0:
                        potraga=potraga[:brojilo]+'5'
                    elif pix2[(broj13+broj3+6),5]>0 and pix2[(broj13+broj3),9]!=0 and pix2[(broj13+broj3),8]!=0:
                        potraga=potraga[:brojilo]+'8'
                        
                elif potraga[brojilo]=='8' and situacija==1:
                    #print(broj13+broj3+6)
                    if pix2[(broj13+broj3+6),5]==0:
                        potraga=potraga[:brojilo]+'6'
                        
                
                
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
                
                
        vjerojatnost=[]
        broj3=i+1

    #print(potraga)
    
    
    






    #print(broj14)
    #print(pomoc2)
    

    return (potraga)



    
