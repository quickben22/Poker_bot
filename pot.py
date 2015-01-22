from PIL import Image
from PIL import ImageChops
import oduzmi
import folder

def koji(pomak,pomak2):
    dir=folder.get()
    im = Image.open(dir+'slika.jpg')

    size=(476-pomak2,52+pomak,556-pomak2,71+pomak) #povecat za 1 kad bude trebalo
    im2=im.crop(size)
    im2.save(dir+'pot.jpg','JPEG')
    
    #im3=im2.convert('P').convert('1')
    #im2 = Image.open('pot_cb7.jpg')
    im3=im2.convert('P').convert('1')
    pix = im3.load()
    im3.save(dir+'pot_cb.jpg')

    pomoc=0
    pomoc2=0
    for i in range(80):
        if pomoc>12 and pomoc<17:
            break
        else:
            pomoc=0
        
        for j in range(19):
            if pix[i,j]==0:
                pomoc+=1
            if pomoc>12:
                pomoc2=i # mjesto gdje je sredina od $
                #break
    #print(pomoc2)

    pomoc3=[]
    pomoc=-1
    for i in range(80-pomoc2-5):
        if pomoc>17:
            break
        if pomoc>-1:
            pomoc3.append(pomoc)
        pomoc=0
            
        for j in range(19):
            if pix[i+pomoc2+5,j]==0:
                pomoc+=1
            
    #pomoc3.append(pomoc)
    #print(pomoc3)
    pomoc4=[]
    pomoc5=0
    pomoc6=0
    flag=0

    if len(pomoc3)>0:
        if pomoc3[0]==0:
            pomoc3.remove(0)

    novi=[]
    novi=pomoc3[:]
    novi2=[]
    nule_gdje=[]
    z=1
    broj=0
    broj2=0
    while (z): #
        try:
            nule_gdje.append(novi.index(0)+broj+broj2)
        except ValueError:
            z=0
            continue
        else:
            novi.remove(0)
        
        #if len(nule_gdje)>1:
           # if (nule_gdje[broj]-nule_gdje[broj-1])<4:
              #  broj-=1
              #  broj2+=1
              #  nule_gdje.pop()

        broj+=1    
            
    #print(nule_gdje)
    broj3=0
    potraga=[]
    oduz=[]
    vjerojatnost=[]
    zeroth=[5,9,4,4,4,9,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    first=[2,2,2,11,11,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    second=[3,6,6,6,6,7,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    third=[1,5,4,6,6,9,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    third2=[5,4,6,6,9,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    fourth=[2,4,4,4,11,11,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    fifth=[2,9,6,6,6,8,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    sixth=[5,9,4,6,6,7,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    seventh=[2,4,8,5,4,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    eigth=[5,9,6,6,6,9,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    nineth=[4,7,6,6,4,9,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in nule_gdje:
        if len(pomoc3[broj3:i])>1: # ako su nule jedna pored druge
            #print(pomoc3[broj3:i])
            
            if pomoc3[broj3:i]==[2,2]:
                potraga.append(10)
            else:
                oduz=oduzmi.liste(pomoc3[broj3:i],zeroth)
                vjerojatnost.append(sum(oduz))
                oduz=oduzmi.liste(pomoc3[broj3:i],first)
                vjerojatnost.append(sum(oduz))
                oduz=oduzmi.liste(pomoc3[broj3:i],second)
                vjerojatnost.append(sum(oduz))
                oduz=oduzmi.liste(pomoc3[broj3:i],third)
                vjerojatnost.append(sum(oduz))
                oduz=oduzmi.liste(pomoc3[broj3:i],third2)
                vjerojatnost.append(sum(oduz))
                oduz=oduzmi.liste(pomoc3[broj3:i],fourth)
                vjerojatnost.append(sum(oduz))
                oduz=oduzmi.liste(pomoc3[broj3:i],fifth)
                vjerojatnost.append(sum(oduz))
                oduz=oduzmi.liste(pomoc3[broj3:i],sixth)
                vjerojatnost.append(sum(oduz))
                oduz=oduzmi.liste(pomoc3[broj3:i],seventh)
                vjerojatnost.append(sum(oduz))
                oduz=oduzmi.liste(pomoc3[broj3:i],eigth)
                vjerojatnost.append(sum(oduz))
                oduz=oduzmi.liste(pomoc3[broj3:i],nineth)
                vjerojatnost.append(sum(oduz))

                if vjerojatnost.index(min(vjerojatnost))>3:
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

    #print('u potu ima %.2f$'%(float(dizati)/100))
        
    
    return dizati
