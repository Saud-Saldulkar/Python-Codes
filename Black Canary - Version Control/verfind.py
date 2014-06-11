import os

def highestversion(filepath,filename):   
    c = 1
    while True:
        fname = filename.replace('.',' version %s.',10) %(c)
        chkfile = filepath + fname        
        chk = os.path.isfile(chkfile)
        if chk is True:            
            c = c + 1            
            continue
        else:
            f = c - 1                       
            break        
    return f       
