from PIL import Image
from PIL import ImageChops
import folder

def koja(dat):
    dir=folder.get()	
    im = Image.open(dir+"%d"%(dat+1)+'.jpg')

    im2=im.convert('P').convert('1')

    pix = im2.load()
    velicina=im2.getbbox()
    im2.save(dir+'karta3.jpg')
    x=(velicina[2])
    y=(velicina[3])

    nula=0
    nula1=0
    nula2=0
    nula3=0
    nula4=0

    for j in range(3):  

        for i in range(x):
            #print(i+2,j+2,pix[i+2,j+2])
            if pix[i,j+23]==0:
                nula4+=1
    #print(nula4)
    if nula4>20:
        #print('nije karta')
        return 0

    for j in range(y-33):  

        for i in range(x-12):
            #print(i+2,j+2,pix[i+2,j+2])
            if pix[i+2,j+2]==0:
                nula+=1

    for j in range(y-33):  

        for i in range(x-12):
            #print(i+10,j+2,pix[i+10,j+2])
            if pix[i+10,j+2]==0:
                nula1+=1


    for j in range(y-33):  

        for i in range(x-12):
            #print(i+10,j+11,pix[i+10,j+11])
            if pix[i+10,j+11]==0:
                nula2+=1


    for j in range(y-33):  

        for i in range(x-12):
            #print(i+2,j+11,pix[i+2,j+11])
            if pix[i+2,j+11]==0:
                nula3+=1

    #nula4=nula+nula1+nula2+nula3
    #print(nula)
    #print(jedan)
    #print(dva)
    #print(tri)
    #print(nula+jedan+dva+tri)

    dva=0

    #rjecnik={'dva':0,'tri':0, 'cetiri':0,'pet':0,'sest':0,'sedam':0,'osam':0,'devet':0, 'deset':0,'decko':0, 'dama':0,'kralj':0,'asic':0}

    tri=0
    cetiri=0
    pet=0
    sest=0
    sedam=0
    osam=0
    devet=0
    deset=0
    decko=0
    dama=0
    kralj=0
    asic=0



    if nula<5:
        decko+=5;
    
    elif nula<10:
        
        
        asic+=1
    elif nula<15:
        
        sedam+=1
        
        dama+=1
        
        
    elif nula<20:
       
        
        
        dama+=1
    
    
        
    
    
    
        
    
        
       
        
        
    if nula1<20:
       
       
        
       
        decko+=1
        dama+=1
        
        
    elif nula1<25: 
        
        
        sedam+=1
        
        decko+=1
        dama+=1
   
    else:
        
        sedam+=1

    if nula2<15:
        sedam+=2
        
    elif nula2<20:
        
        
        sedam+=1
        decko+=1
        
    elif nula2<25: 
        
       
        
        devet+=1
        decko+=1 
          
        
        
        
        
    elif nula2<35:
        
        
        dama+=1
        
        
    else:
        dama+=2

    if nula3<5:
        sedam+=2
        
    elif nula3<10:
       
        sedam+=1
        
    elif nula3<15:
       
        
        
        decko+=1
        
    elif nula3<20:
        
        
        
        decko+=1
        
    elif nula3<25:
        
        dama+=1
    
    elif nula3<30:
       
        dama+=1
        
        
        

    a1=0
    for i in range(11):
        if pix[6+i,17]==0 and pix[6+i,18]==0:
            a1+=1        
    
    if a1>9:
        dva+=12

    a2=0
    for i in range(5):
        if pix[8,5+i]==0 and pix[13,5+i]==0:
            a2+=1

    for i in range(5):
        if pix[7,12+i]==0 and pix[14,12+i]==0:
            a2+=1
        
    if a2>9:
        osam+=11


    a3=0
    for i in range(11):
        if pix[6,7+i]==0 and pix[7,7+i]==0:
            a3+=1

    for i in range(3):
        if pix[7+i,10]==0:
            a3+=1
        
    if a3>13:
        kralj+=11
        

    a4=0
    for i in range(13):
        if pix[6,i+5]==0 and pix[7,i+5]==0:
            a4+=1

    for i in range(7):
        if pix[9,i+8]==0 and pix[10,i+8]==0 and pix[15,i+8]==0:
            a4+=1

    if a4>19:
        deset+=11

    a5=0
    for i in range(9):
        if pix[6+i,13]==0 and pix[6+i,14]==0:
            a5+=1
    
    for i in range(8):
        if pix[12,5+i]==0 and pix[13,5+i]==0:
            a5+=1

    
    if a5>15:
        cetiri+=11

    a6=0
    for i in range(4):
        if pix[5+i,18]==0 and pix[13+i,18]==0:
            a6+=1
    for i in range(6):
        if pix[8+i,12]==0 and pix[8+i,13]==0:
            a6+=1

    if a6>8:
        asic+=11

    if pix[10,5]==0 and pix[7,8]==0 and pix[14,13]==0 and pix[7,13]==255 and pix[6,13]==255 and pix[5,13]==255  and pix[14,7]==255 and pix[13,7]==255:
        pet+=11

    if (pix[12,17]==0 or pix[12,17]==0) and (pix[13,8]==0 or pix[14,8]==0) and (pix[11,10]==0 or pix[10,10]==0) and (pix [11,5]==0 or pix[10,5]==0) and (pix[14,13]==0 or pix[14,12]==0) and pix[8,6]==0 and pix[7,12]==255 and pix[8,13]==255 and pix[7,9]==255 and pix[7,8]==255:
        tri+=11
        
    if pix[8,17]==0 and pix[6,11]==0 and pix[14,14]==0 and pix[8,5]==0 and pix[6,14]==0 and pix[13,8]==255 and pix[14,8]==255:
        sest+=11    

    if pix[9,17]==0 and pix[12,12]==0 and pix[7,11]==0 and pix[7,6]==0 and pix[13,6]==0 and pix[14,10]==0 and pix[6,14]==255 and pix[6,14]==255:
        devet+=11
    
    pitanje=max(dva,tri,cetiri,pet,sest,sedam,osam,devet,deset,decko,dama,kralj,asic)

    if pitanje==sest and pitanje==devet: 
            if (nula1+nula2)>(nula+nula3+1):
                devet+=2
            else:
                sest+=2

    pitanje=max(dva,tri,cetiri,pet,sest,sedam,osam,devet,deset,decko,dama,kralj,asic)

    provjer=0        
    if dva==pitanje:
        #print('dva')
        povrat=1
        provjer+=1
        
    if tri==pitanje:
        #print('tri')
        povrat=5
        provjer+=1
        
    if cetiri==pitanje:
        #print('cetiri')
        povrat=9
        provjer+=1
        
    if pet==pitanje:
        #print('pet')
        povrat=13
        provjer+=1
        
    if sest==pitanje:
        #print('sest')
        povrat=17
        provjer+=1

    if sedam==pitanje:
        #print('sedam')
        povrat=21
        provjer+=1

    if osam==pitanje:
        #print('osam')
        povrat=25
        provjer+=1

    if devet==pitanje:
        #print('devet')
        povrat=29
        provjer+=1
        
    if deset==pitanje:
        #print('deset')
        povrat=33
        provjer+=1
        
    if decko==pitanje:
        #print('decko')
        povrat=37
        provjer+=1
        
    if dama==pitanje:
        #print('dama')
        povrat=41
        provjer+=1
        
    if kralj==pitanje:
        #print('kralj')
        povrat=45
        provjer+=1
    if asic==pitanje:
        #print('asic')
        povrat=49
        provjer+=1

    if provjer>1:
        return 53
    
    if pix[5,25]==0 and pix[15,25]==0:
        #print('srce')
        povrat2=0

    elif pix[12,27]==255 and pix[8,27]==255:
        #print('tref')
        povrat2=1

    elif pix[3,30]==0 and pix[17,30]==0 and pix[10,37]==0:
        #print('karo')
        povrat2=2
    else:
        #print('pik')
        povrat2=3

    return (povrat+povrat2)



























































































    
