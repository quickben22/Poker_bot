from PIL import Image
from PIL import ImageChops
import folder

def kamo():
    dir=folder.get()	
    im = Image.open(dir+'pomak.jpg')
    im2=im.convert('P').convert('1')

    pix = im2.load()
    im2.save(dir+'pomak_cb.jpg')
    pomoc=0
    pomoc2=0
    for j in range(16):
        pomoc2=0
        if pomoc>0:
            break
        for i in range(6):
            if pix[i,j]>0:  
                pomoc2+=1
            if  pomoc2>5:
                pomoc=j # red u kojem se prvi put pojavi crno ** kod mene, 
                break

    #print(pomoc)
    pomoc2=pomoc-10
    return pomoc2
