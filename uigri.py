from PIL import Image
from PIL import ImageChops
import folder

def tko(pomak,pomak2):

    dir=folder.get()
    im = Image.open(dir+'slika.jpg')

    size=(236-pomak2,395+pomak,248-pomak2,418+pomak) #povecat za 1 kad bude trebalo
    im2=im.crop(size) 
    im3=im2.convert('P').convert('1')
    pix1 = im3.load()
    im3.save(dir+'spil1.jpg') #karte1
    b=[]
    #c=[]
    a=0
    for i in range(12):
        for j in range(23):
            if pix1[i,j]>0:
                a+=1
    if a>220:
        b.append(1)
    a=0
    
    size=(146-pomak2,302+pomak,158-pomak2,325+pomak) #povecat za 1 kad bude trebalo
    im2=im.crop(size) 
    im3=im2.convert('P').convert('1')
    pix1 = im3.load()
    im3.save(dir+'spil2.jpg') #karte2

    for i in range(12):
        for j in range(23):
            if pix1[i,j]>0:
                a+=1
    if a>220:
         b.append(2)
    a=0

    size=(242-pomak2,185+pomak,254-pomak2,208+pomak) #povecat za 1 kad bude trebalo
    im2=im.crop(size) 
    im3=im2.convert('P').convert('1')
    pix1 = im3.load()
    im3.save(dir+'spil3.jpg') #karte3

    for i in range(12):
        for j in range(23):
            if pix1[i,j]>0:
                a+=1
    if a>220:
         b.append(3)
    a=0

    size=(782-pomak2,188+pomak,794-pomak2,211+pomak) #povecat za 1 kad bude trebalo
    im2=im.crop(size) 
    im3=im2.convert('P').convert('1')
    pix1 = im3.load()
    im3.save(dir+'spil4.jpg') #karte4

    for i in range(12):
        for j in range(23):
            if pix1[i,j]>0:
                a+=1
    if a>220:
         b.append(4)
    a=0

    size=(877-pomak2,303+pomak,889-pomak2,326+pomak) #povecat za 1 kad bude trebalo
    im2=im.crop(size) 
    im3=im2.convert('P').convert('1')
    pix1 = im3.load()
    im3.save(dir+'spil5.jpg') #karte5


    for i in range(12):
        for j in range(23):
            if pix1[i,j]>0:
              a+=1
    if a>220:
         b.append(5)
    
    #print('u igri su =', b)
    return b
    
