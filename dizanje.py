
from PIL import ImageChops
from PIL import Image
import oduzmi
import folder

def koliki(call):
    dir=folder.get()
    if call==2:
        im = Image.open(dir+'8.jpg')
    else:
        im = Image.open(dir+'9.jpg')
        
    
    #im3=im2.convert('P').convert('1')
    #im2 = Image.open('pot_cb7.jpg')
    im2=im.convert('P').convert('1')
    pix = im2.load()
    im2.save(dir+'raise_cb.jpg')

    pomoc=0
    pomoc2=[]
    for i in range(110-30):
        
        
        for j in range(56-36):
            if pix[i+16,j+24]>0:
              pomoc+=1  
        
        pomoc2.append(pomoc)
        pomoc=0
    z=1
    while z:
        if len(pomoc2)>0:
            if pomoc2[0]==0:
                pomoc2.remove(0)
            else:
                z=0
    #print (pomoc2)
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
                #print(novi[(nule_gdje[broj-1]+5-broj2):].index(2))
                #print((nule_gdje[broj-1]+5-broj2))
                #print(novi)
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
                #print()
                #print(novi[(nule_gdje[broj-1]+5-broj2):].index(1))
                #print((nule_gdje[broj-1]+5-broj2))
                #print(novi)
                continue
                #prevelik=1
        novi.remove(0)
        broj+=1
    #print (nule_gdje)
    broj=0
    #while prevelik:
        #print(prevelik)
            
     #   prevelik=0
        
    zeroth=[1, 9, 12, 4, 3, 2, 9, 12, 7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    zeroth2=[9, 13, 4, 3, 2, 11, 12, 8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    first=[1, 2, 2, 10, 13, 13,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    first2=[1, 3, 10, 13, 14, 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    second=[1, 4, 6, 6, 6, 5, 9, 8, 6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    second2=[1, 1, 4, 6, 6, 6, 5, 9, 8, 6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    second3=[ 4, 6, 6, 6, 5, 9, 8, 6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    third=[2, 3, 2, 5, 8, 11, 9, 5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    third2=[1, 2, 5, 3, 4, 6, 12, 11, 4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    third3=[1, 1, 2, 4, 3, 5, 8, 10, 9, 5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    fourth=[1, 4, 4, 4, 3, 10, 13, 14, 2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    fifth=[3, 9, 5, 5, 5, 7, 9, 4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    sixth=[7, 10, 7, 4, 4, 6, 7, 6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    seventh=[4, 2, 3, 6, 6, 6, 5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    eigth=[7, 12, 8, 5, 5, 8, 11, 5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    nineth=[6, 8, 5, 5, 3, 10, 11, 7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    broj3=0
    potraga=[]
    oduz=[]
    vjerojatnost=[]
    broj3=nule_gdje[0]+1
    for i in nule_gdje:
            
        if len(pomoc2[broj3:i])>1:
            #print(pomoc2[broj3:i])

       
            if pomoc2[broj3:i]==[3,3] or pomoc2[broj3:i]==[1,3,3] or pomoc2[broj3:i]==[1,3,2] or pomoc2[broj3:i]==[3,2] or pomoc2[broj3:i]==[2,3] or pomoc2[broj3:i]==[1,2,3] :
                potraga.append(10)
            else:
                oduz=oduzmi.liste(pomoc2[broj3:i],zeroth)
                vjerojatnost.append(sum(oduz))
                oduz=oduzmi.liste(pomoc2[broj3:i],zeroth2)
                vjerojatnost.append(sum(oduz))
                oduz=oduzmi.liste(pomoc2[broj3:i],first)
                vjerojatnost.append(sum(oduz))
                oduz=oduzmi.liste(pomoc2[broj3:i],first2)
                vjerojatnost.append(sum(oduz))
                oduz=oduzmi.liste(pomoc2[broj3:i],second)
                vjerojatnost.append(sum(oduz))
                oduz=oduzmi.liste(pomoc2[broj3:i],second2)
                vjerojatnost.append(sum(oduz))
                oduz=oduzmi.liste(pomoc2[broj3:i],second3)
                vjerojatnost.append(sum(oduz))
                oduz=oduzmi.liste(pomoc2[broj3:i],third)
                vjerojatnost.append(sum(oduz))
                oduz=oduzmi.liste(pomoc2[broj3:i],third2)
                vjerojatnost.append(sum(oduz))
                oduz=oduzmi.liste(pomoc2[broj3:i],third3)
                vjerojatnost.append(sum(oduz))
                oduz=oduzmi.liste(pomoc2[broj3:i],fourth)
                vjerojatnost.append(sum(oduz))
                oduz=oduzmi.liste(pomoc2[broj3:i],fifth)
                vjerojatnost.append(sum(oduz))
                oduz=oduzmi.liste(pomoc2[broj3:i],sixth)
                vjerojatnost.append(sum(oduz))
                oduz=oduzmi.liste(pomoc2[broj3:i],seventh)
                vjerojatnost.append(sum(oduz))
                oduz=oduzmi.liste(pomoc2[broj3:i],eigth)
                vjerojatnost.append(sum(oduz))
                oduz=oduzmi.liste(pomoc2[broj3:i],nineth)
                vjerojatnost.append(sum(oduz))

                if vjerojatnost.index(min(vjerojatnost))>8:
                    potraga.append(vjerojatnost.index(min(vjerojatnost))-6)
                elif vjerojatnost.index(min(vjerojatnost))>7:
                    potraga.append(vjerojatnost.index(min(vjerojatnost))-5)
                elif vjerojatnost.index(min(vjerojatnost))>5:
                    potraga.append(vjerojatnost.index(min(vjerojatnost))-4)
                elif vjerojatnost.index(min(vjerojatnost))>4:
                    potraga.append(vjerojatnost.index(min(vjerojatnost))-3)
                elif vjerojatnost.index(min(vjerojatnost))>2:
                    potraga.append(vjerojatnost.index(min(vjerojatnost))-2)
                elif vjerojatnost.index(min(vjerojatnost))>0:
                    potraga.append(vjerojatnost.index(min(vjerojatnost))-1)
                else:
                    potraga.append(vjerojatnost.index(min(vjerojatnost)))

                            
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

    #print('raise je bio %.2f$'%(float(dizati)/100))
        
    
    return (dizati)
