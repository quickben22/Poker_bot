import shelve
#ovdje se uzima iz fajla
def spremi(ime_igraca,broj): #,popis_igraca,popis_igraca1,popis_igraca0,popis_igraca2,popis_igraca3,popis_igraca4,popis_igraca5

    if broj==8:
        d1 = shelve.open('CB_igraca') # open, with (g)dbm filename -- no suffix
        if ime_igraca in d1:
            return d1[ime_igraca]
        else:    
            return [0,0,0,0]
    elif broj==2:
        d1 = shelve.open('popis_igraca2') # open, with (g)dbm filename -- no suffix
        if ime_igraca in d1:
            return d1[ime_igraca]
        else:    
            return [0,0,0,0]

    elif broj==1:
        d1 = shelve.open('popis_igraca') # open, with (g)dbm filename -- no suffix
        if ime_igraca in d1:
            return d1[ime_igraca]
        else:    
            return [0,0,0,0,0,0,0,0,0,0]

    elif broj==3:
        d1 = shelve.open('popis_igraca3') # open, with (g)dbm filename -- no suffix
        if ime_igraca in d1:
            return d1[ime_igraca]
        else:    
            return [0,0,0,0]

    elif broj==4:
        d1 = shelve.open('popis_igraca4') # open, with (g)dbm filename -- no suffix
        if ime_igraca in d1:
            return d1[ime_igraca]
        else:    
            return [0,0,0,0]

    elif broj==5:
        d1 = shelve.open('popis_igraca5') # open, with (g)dbm filename -- no suffix
        if ime_igraca in d1:
            return d1[ime_igraca]
        else:    
            return [0,0,0,0]
        
    elif broj==6:
        d1 = shelve.open('popis_igraca1') # open, with (g)dbm filename -- no suffix
        if ime_igraca in d1:
            return d1[ime_igraca]
        else:    
            return [0,0,0,0]
        
    elif broj==7:
        d1 = shelve.open('popis_igraca0') # open, with (g)dbm filename -- no suffix
        if ime_igraca in d1:
            return d1[ime_igraca]
        else:    
            return [0,0,0,0,0,0]

    
           #  CB_igraca[i]
             
    #d[key] = data   # store data at key (overwrites old data if
                # using an existing key)
    #data = d[key]   # retrieve data at key (raise KeyError if no
                # such key)
    #del d[key]      # delete data stored at key (raises KeyError
                # if no such key)
    #flag = d.has_key(key)   # true if the key exists if ime_igraca in d1:
    #list = d.keys() # a list of all existing keys (slow!)

    d1.close()       # close it
