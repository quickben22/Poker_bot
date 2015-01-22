

def igraca(bet_raise,check_call,foldic,vide_flop):

    #premalo podataka    
    if bet_raise==0 or check_call==0 or vide_flop==0:
        return 0
    #LAG puno raisea malo check_call, puno flopa igra, malo folda, 
    if bet_raise>=check_call and vide_flop>0.4: #vise raise nego check_call
        return 1 #LAG
    
    #TP Malo raise, puno check_call,   malo flopa igra,       puno fold
    if check_call>bet_raise and vide_flop<=0.4:
        return 2 #TP
    #TAG Raisea puno, malo check_call,  malo flopa igra,      puno fold 
    if bet_raise>=check_call and vide_flop<=0.4:
        return 3  #TAG
    #LP Malo raise, puno check call,   puno flopa igra,    malo fold
    if check_call>bet_raise and vide_flop>0.4:
        return 4 #LP
