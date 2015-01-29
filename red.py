from PIL import Image
from PIL import ImageChops
import folder

def tko(dat):
    dir=folder.get()	
    im = Image.open(dir+"%d"%dat+'.jpg')
    im3 = Image.open(dir+"%d"%(dat+1)+'.jpg')
    im2=im.convert('P').convert('1')
    im4=im3.convert('P').convert('1')
    
    pix = im2.load()
    velicina=im2.getbbox()
    im2.save(dir+'cb_test.jpg')
    x=(velicina[2])
    y=(velicina[3])

    pix2 = im4.load()
    velicina2=im4.getbbox()
    im4.save(dir+'cb_test2.jpg')
    x1=(velicina2[2])
    y1=(velicina2[3])
    
    nula4=0
    nula1=0
    for j in range(y):  

        for i in range(x):
            #print(i+2,j+2,pix[i+2,j+2])
            if pix[i,j]==0:
                nula4+=1

    for j in range(y1):  

        for i in range(x1):
            #print(i+2,j+2,pix[i+2,j+2])
            if pix2[i,j]==0:
                nula1+=1
    #print(nula4)
    #print(nula1)
    #print(x,y,x1,y1)
    
    if nula4>2000:
        #print('na redu')
        if pix[26,24]==255 and pix[26,25]==255 and pix[26,26]==255:
            print('check')
            return 1
        else:
            print('call')
            return 2
    elif nula1>2000:
        if pix2[4,23]==255 and pix2[5,24]==255 and pix2[6,24]==255 and pix2[7,25]==255 and pix2[56,26]==255 and pix2[56,25]==255 and pix2[56,24]==255 and pix2[101,27]==255 and pix2[102,27]==255:
            #print('nije na redu')
            return 0
        else:
            print('call')
            return 3
    else:
        #print('nije na redu')
        return 0
