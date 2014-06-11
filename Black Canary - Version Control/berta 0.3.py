#PERSONAL PROJECT - VERSION CONTROL SYSTEM - SIMILAR TO GIT (BUT VERY MINIMALISTIC)
# STILL UNDER DEVELOPMENT

import threading, time, os, shutil, win32api, win32con, verfind

filepath = "C:/Users/Mr S/Desktop/new/"
prefn = os.listdir(filepath)
prelenfn = len(prefn)

c = 0
fn = []

for x in xrange(prelenfn):
    if '.' in prefn[c]:
        fn.append(prefn[c])
        c = c + 1
    else:
        c = c + 1
        continue

lenfn = len(fn)



#check filename + 'version' exists? --> extract numbers --> analyse numbers --> +1 --> move --> make file attr NORMAL

class monitor(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        while True:
            prestatinfo = os.stat(self.name) # TAKING PRE META STAT INFO
            premodtime = prestatinfo.st_mtime

            splitvar = os.path.split(self.name) # ADDING ~ TO TEMP FILE
            fname = splitvar[1].replace('.','~',10)

            destination = filepath + fname
            while True:               
                try:
                    shutil.copy2(self.name,destination) # CREAT TEMP FILE
                    break
                except:
                    os.remove(destination)# REMOVE UNWANTED PRE-EXISTING TEMP FILES
                    
            win32api.SetFileAttributes(destination,win32con.FILE_ATTRIBUTE_HIDDEN) #MAKE TEMP FILE HIDDEN         
            
            while True:
                poststatinfo = os.stat(self.name) #MONITOR POST META STAT
                postmodtime = poststatinfo.st_mtime              
                if premodtime != postmodtime: #IF META STAT HAS CHANGED THEN EXECUTE:
                    print 'File %s has been modified' %(self.name)
                    hver = verfind.highestversion(filepath,splitvar[1])
                    src = destination
                    dfname = splitvar[1].replace('.',' version %s.') %(hver + 1)
                    dstn = filepath + dfname
                    shutil.move(src,dstn)
                    win32api.SetFileAttributes(dstn, win32con.FILE_ATTRIBUTE_NORMAL)
                    break

r = 0
for x in xrange(lenfn):
    filename = fn[r]   
    name = filepath + filename
    hname = filename + str(r)
    r = r + 1
    hname = monitor(name)
    hname.start()

        
