
def sto(jacina,znak):

    stolic=jacina[2:]
    pomocni=stolic[:]
    pomocni.sort()
    pomocni2=znak[2:]
    z=0
    if pomocni2.count(1)==3 or pomocni2.count(2)==3 or pomocni2.count(3)==3 or pomocni2.count(4)==3:
        print('3 od boje na stolu')
        z=2
    elif pomocni2.count(1)==2 or pomocni2.count(2)==2 or pomocni2.count(3)==2 or pomocni2.count(4)==2:
        print('2 od boje na stolu')
        z=1

    if pomocni.count(0)==2:
        pomocni.remove(0)

    elif pomocni.count(0)==1:
        pomocni.remove(0)

    for i in pomocni: #sve razlicite karte, nema parova
        if pomocni.count(i)>1:
            pomocni.remove(i)

    za_skalu=[]
    kombinacija6=0
    for j in range(1):
        if pomocni.count(13)==1:
            pomocni.append(0)
            pomocni.sort()
                
        for i in range(len(pomocni)-1):
            za_skalu.append((pomocni[len(pomocni)-1-i] - pomocni[len(pomocni)-2-i]))


        #for i in range(len(za_skalu)-1):

            
    #    if len(za_skalu)==2:
   #         if (za_skalu[0]+za_skalu[1])==2:
  #              kombinacija=3
 #           elif (za_skalu[0]+za_skalu[1])==3:
#                kombinacija=2
                
       # elif len(za_skalu)==3:
      #      if (za_skalu[0]+za_skalu[1]+za_skalu[2])==4:
     #           kombinacija=20
    #        elif za_skalu[0]==2 and za_skalu[1]==1 and za_skalu[2]==2:
   #             kombinacija=3
  #          elif (za_skalu[0]+za_skalu[1]+za_skalu[2])==5:
 #               kombinacija=2
#            elif (za_skalu[0]+za_skalu[1])==2:
         #       kombinacija=3
        #    elif (za_skalu[0]+za_skalu[1])==3:
       #         kombinacija=2
      #      elif (za_skalu[1]+za_skalu[2])==2:
     #           kombinacija=3
    #        elif (za_skalu[1]+za_skalu[2])==3:
   #             kombinacija=2

  #          
 #       elif len(za_skalu)==4:
            

#        elif len(za_skalu)==5:
            
        
            
        uvjet1=0
        uvjet2=0
        uvjet3=0
        uvjet4=0
        uvjet5=0
        uvjet6=0
        kombinacija=0
  #      kombinacija2=0
   #     kombinacija3=0
    #    kombinacija4=0
     #   kombinacija5=0
      #  kombinacija6=0
       # kombinacija0=1
        for i in range(len(za_skalu)-1):
            if za_skalu[i+1]==1 and za_skalu[i]==1:
                #kombinacija+=3
                uvjet1=1
                if uvjet2==1 and za_skalu[i-1]==2:
                    kombinacija=20
                    
                
            elif (za_skalu[i+1]==1 and za_skalu[i]==2) :
                uvjet2=1
                #kombinacija+=2
                
                
            elif (za_skalu[i+1]==2 and za_skalu[i]==1):
                if uvjet1==1 and za_skalu[i-1]==1:
                    kombinacija=20
                    
                if uvjet2==1 and za_skalu[i-1]==1: 
                    kombinacija=20

                if uvjet2==1 and uvjet1==1 and za_skalu[i-1]==1 and za_skalu[i-2]==2:
                    kombinacija=40
                    break
                
                uvjet3=1
                #kombinacija+=2
               
                    
            #elif (za_skalu[i+1]==2 and za_skalu[i]==2):
            #    uvjet4=1    
                
             
            #elif (za_skalu[i+1]==1 and za_skalu[i]==3):
             #   uvjet5=1
                
            #elif (za_skalu[i+1]==3 and za_skalu[i]==1):
           #     uvjet6=1
            
   #     if len(za_skalu)>3:
  #          if za_skalu[0]==2 and za_skalu[1]==1 and za_skalu[2]==1 and za_skalu[3]==2:
 #               kombinacija=40
#        if len(za_skalu)>2:
         #   if za_skalu[0]==1 and za_skalu[1]==2 and za_skalu[2]==1:
        #        kombinacija=20
       #     elif za_skalu[1]==1 and za_skalu[2]==2 and za_skalu[3]==1:
      #          kombinacija=20
                
     #       if pomocni[0]==0 and pomocni[1]==1 and pomocni[2]==2:
    #            kombinacija-=2
   #         elif pomocni[0]==0 and pomocni[1]==1 and pomocni[2]==3:
  #              kombinacija-=1
 #           elif pomocni[0]==0 and pomocni[1]==2 and pomocni[2]==3:
#                kombinacija-=1
            #elif pomocni[0]==1 and pomocni[1]==2 and pomocni[2]==3:
           #    kombinacija-=1
            
          #      
         #   if pomocni[-1]==13 and pomocni[-2]==12 and pomocni[-3]==11:
        #        kombinacija-=2
       #     elif pomocni[-1]==13 and pomocni[-2]==11 and pomocni[-3]==10:
      #          kombinacija-=1
     #       elif pomocni[-1]==13 and pomocni[-2]==12 and pomocni[-3]==10:
    #            kombinacija-=1
   #         elif pomocni[-1]==12 and pomocni[-2]==11 and pomocni[-3]==10:
  #              kombinacija-=1
        
        
        #if kombinacija6>kombinacija:
        #    kombinacija=kombinacija6
       # kombinacija6=kombinacija
    
    print(za_skalu,pomocni,kombinacija)


    return [int(kombinacija),z] #vece ili jednako 10=> skala, vece ili jednako 30 skala sa 2 strane
