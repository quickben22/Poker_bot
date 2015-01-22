from PIL import Image
from PIL import ImageChops
import folder

def prekid():
    dir=folder.get()
    im = Image.open(dir+'10.jpg')
    im2=im.convert('P').convert('1')

    pix = im2.load()
    velicina=im2.getbbox()
    im2.save(dir+'screen1.jpg')
        

    nula=0
    nula2=0
    for j in range(42):  

        for i in range(20):
            if pix[i,j]==0:
                nula+=1

    im = Image.open(dir+'11.jpg')
    im2=im.convert('P').convert('1')

    pix = im2.load()
    velicina=im2.getbbox()
    im2.save(dir+'screen2.jpg')

        
    for j in range(42):  

        for i in range(20):
            if pix[i,j]==0:
                nula2+=1

    #print(nula,nula2)

    if nula>20 and nula<170 and nula2>20 and nula2<170:
        return 1
    else:
        return 0
