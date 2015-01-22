import shelve
#ovdje se pise u fajl
def spremi(ime_igraca,podaci,broj): #,popis_igraca,popis_igraca1,popis_igraca0,popis_igraca2,popis_igraca3,popis_igraca4,popis_igraca5

    if broj==8:    
        d1 = shelve.open('CB_igraca') # open, with (g)dbm filename -- no suffix

        d1[ime_igraca]=podaci
        
        
    elif broj==2:
        d1 = shelve.open('popis_igraca2') # open, with (g)dbm filename -- no suffix

        d1[ime_igraca]=podaci

    elif broj==1:
        d1 = shelve.open('popis_igraca') # open, with (g)dbm filename -- no suffix

        d1[ime_igraca]=podaci
    elif broj==3:
        d1 = shelve.open('popis_igraca3') # open, with (g)dbm filename -- no suffix

        d1[ime_igraca]=podaci
    elif broj==4:
        d1 = shelve.open('popis_igraca4') # open, with (g)dbm filename -- no suffix

        d1[ime_igraca]=podaci
    elif broj==5:
        d1 = shelve.open('popis_igraca5') # open, with (g)dbm filename -- no suffix

        d1[ime_igraca]=podaci
    elif broj==6:
        d1 = shelve.open('popis_igraca1') # open, with (g)dbm filename -- no suffix

        d1[ime_igraca]=podaci
    elif broj==7:
        d1 = shelve.open('popis_igraca0') # open, with (g)dbm filename -- no suffix

        d1[ime_igraca]=podaci
        
        

        
    d1.close()
