from PIL import Image
from PIL import ImageChops
import folder

def kamo():
    dir=folder.get()	
    im = Image.open(dir+'pomak2.jpg')
    im2=im.convert('P').convert('1')

    pix = im2.load()
    im2.save(dir+'pomak_cb2.jpg')
    pomoc=0
    pomoc2=0
    for i in range(22):
        if pomoc>0:
            break
        for j in range(5):
            if pix[i,j]==0:
                pomoc=i # stupac u kojem se prvi put pojavi crno ** kod mene, 
                break

    #print(pomoc)
    pomoc2=pomoc-9
    return pomoc2
