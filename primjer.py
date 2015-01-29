from PIL import Image
import folder


def spremi(vrijeme,situacija):
    dir=folder.get()
    im1 = Image.open(dir+'slika.jpg')
    print(dir+'primjeri\\slika')
    im1.save(dir+'primjeri\\slika'+str(vrijeme)+'_'+str(situacija)+'.jpg','JPEG')
   

