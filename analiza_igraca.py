from PIL import Image
from PIL import ImageChops
import oduzmi
import folder

def kakav(slika,pomak,pomak2):
    dir=folder.get()	
    b=[]
    #c=[]
    a=0
    
    im = Image.open(dir+'slika.jpg')

    if slika==1:
        size=(213-pomak2,470+pomak,268-pomak2,486+pomak) #povecat za 1 kad bude trebalo
        im2=im.crop(size) 
        im3=im2.convert('P').convert('1')
        pix1 = im3.load()
        im3.save(dir+'krug1.jpg') #krug1
    
    
    elif slika==2:
        size=(50-pomak2,324+pomak,105-pomak2,340+pomak) #povecat za 1 kad bude trebalo
        im2=im.crop(size) 
        im3=im2.convert('P').convert('1')
        pix1 = im3.load()
        im3.save(dir+'krug2.jpg') #krug2

    
    elif slika==3:
        size=(157-pomak2,159+pomak,212-pomak2,175+pomak) #povecat za 1 kad bude trebalo
        im2=im.crop(size) 
        im3=im2.convert('P').convert('1')
        pix1 = im3.load()
        im3.save(dir+'krug3.jpg') #krug3

   
    elif slika==4:
        size=(821-pomak2,160+pomak,876-pomak2,176+pomak) #povecat za 1 kad bude trebalo
        im2=im.crop(size) 
        im3=im2.convert('P').convert('1')
        pix1 = im3.load()
        im3.save(dir+'krug4.jpg') #krug4

    
    elif slika==5:
        size=(924-pomak2,324+pomak,979-pomak2,340+pomak) #povecat za 1 kad bude trebalo
        im2=im.crop(size) 
        im3=im2.convert('P').convert('1')
        pix1 = im3.load()
        im3.save(dir+'krug5.jpg') #krug5

    c=0
    for i in range(55):
        if pix1[i,0]==0:
            c+=1

    if c>4:
        #print('ne zanima me to')
        return 0
    #print(c)
    d=0
    a=0
    for i in range(55):
        for j in range(16):
            if pix1[i,j]==0:
                a+=1
                   
    
    if a<100:
        #print('ne zanima me to')
        return 0
    
    for i in range(55):
        a=0
        for j in range(16):
            if pix1[i,j]==0:
                a+=1
            else:
                a=0
            if a==7:
                d+=1
    #print(d)
    a=0

    pomoc2=[]
    b=0
    for i in range(55):
        for j in range(16):#novac
            if pix1[i,j]==0:
                b+=1
        pomoc2.append(b)
        b=0
        
    z=1
    broj13=0
    while z: #makni sve nule do prvog znaka
        if len(pomoc2)>0:
            if pomoc2[0]==0:
                pomoc2.remove(0)
                broj13+=1
            else:
                z=0


    
    check=[1, 8, 10, 12, 9, 4, 3, 5, 5, 7, 5, 2, 12, 12, 12, 6, 4, 8, 8, 6, 5, 7, 9, 8, 5, 8, 9, 6, 7, 8, 9, 7, 6, 8, 6, 4, 13, 12, 13, 9, 9, 10, 9, 8, 4, 6, 3, 8, 2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    call=[1, 7, 10, 12, 10, 3, 5, 6, 5, 7, 4, 2, 5, 9, 8, 8, 8, 8, 5, 3, 12, 12, 12, 5, 6, 12, 13, 12, 8, 0, 3, 1, 4, 2, 4, 4, 3, 3, 6, 3, 7, 5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    raisic=[1, 3, 11, 12, 13, 11, 9, 11, 12, 10, 5, 2, 1, 6, 8, 8, 8, 7, 7, 7, 3, 9, 12, 12, 7, 3, 8, 7, 9, 9, 8, 7, 7, 8, 9, 8, 10, 9, 6, 4, 4, 4, 4, 5, 4, 7, 4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]  
    fold=[1, 2, 12, 12, 12, 8, 4, 6, 8, 4, 3, 6, 8, 6, 4, 7, 8, 7, 6, 13, 12, 11, 7, 2, 6, 9, 8, 8, 12, 12, 14, 12, 6, 2, 1, 3, 3, 2, 6, 3, 5, 5, 5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    potraga=-1
    oduz=[]
    vjerojatnost=[]
    #print(pomoc2)

    oduz=oduzmi.liste(pomoc2,check)
    vjerojatnost.append(sum(oduz))
    oduz=oduzmi.liste(pomoc2,call)
    vjerojatnost.append(sum(oduz))
    oduz=oduzmi.liste(pomoc2,raisic)
    vjerojatnost.append(sum(oduz))
    oduz=oduzmi.liste(pomoc2,fold)
    vjerojatnost.append(sum(oduz))
    
    potraga=(vjerojatnost.index(min(vjerojatnost))+1)
    
    #print ('prozor broj',slika,potraga)
    return potraga

    
