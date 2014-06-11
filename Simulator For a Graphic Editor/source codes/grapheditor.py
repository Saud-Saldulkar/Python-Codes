#-------------------------------------------------------
#HEADER TEXT
print '''
\t \t +-------------------------------------+  
\t \t |***SIMULATOR FOR A GRAPHIC EDITOR*** |
\t \t |       Author: Saud Saldulkar        |
\t \t |       Email: saud28@hotmail.com     |
\t \t +-------------------------------------+

\t \t Note: Command(I) needs to executed first
\t \t               Type(X) to exit
'''
#HEADER TEXT
#-------------------------------------------------------

#-------------------------------------------------------
#Libraries used: NUMPY: For creating and handling arrays
#                RE:    For string pattern recognition
#          commandf:    Function for COMMAND F
#              time:    Module to access time functionality
from numpy import *
import re, commandf,time
#-------------------------------------------------------

#-------------------------------------------------------
#Initialize our IMAGE variable which would be used by the command functions.
image = []
#-------------------------------------------------------

#-------------------------------------------------------
#MAIN function executed when the program runs. This extracts the input commands and analyzes them.
def main():
    io = raw_input('Command Prompt$:')    
    analyze(io)
#-------------------------------------------------------

#-------------------------------------------------------
#create list of commands
cd = ['I','C','L','V','H','F','S','X','']
#create variable to hold the length of variable (cd)
c = len(cd)
#-------------------------------------------------------

#-------------------------------------------------------
#sub function of MAIN function. This function analyzes which command was executed,extracts input and executes related command function.
def analyze(io):
    index = 0
    for x in xrange(c):
        
        alze = io.startswith(cd[index]) #extract input string
        
        if alze is True:
            # checks if command 'I' is executed.
            if index == 0:
                iv = re.findall(r'\b\d+\b', io) #extract digits outside word boundaries.
                command_i(iv[0],iv[1])          #outputs extracted input to command function
                break

            #checks if command 'C' is executed.
            if index == 1:
                command_c()
                break

            #checks if command 'L' is executed.
            if index == 2:
                lv = re.findall(r'\b\d+\b', io)
                lastlv = io[-1]                 #extracts last character of input
                command_l(lv[0],lv[1],lastlv)   
                break

            #checks if command 'V' is executed.
            if index == 3:
                vv = re.findall(r'\b\d+\b', io)
                lastvv = io[-1]
                command_v(vv[0],vv[1],vv[2],lastvv)
                break
            
            #checks if command 'H' is executed.
            if index == 4:
                hv = re.findall(r'\b\d+\b', io)
                lasthv = io[-1]                
                command_h(hv[0],hv[1],hv[2],lasthv)
                break

            #checks if command 'F' is executed.
            if index == 5:
                fv = re.findall(r'\b\d+\b', io)
                lastfv = io[-1]
                command_f(fv[0],fv[1],lastfv)                
                break

            #checks if command 'S' is executed.
            if index == 6:
                command_s()
                break
            
            #checks if command 'X' is executed.
            if index == 7:
                command_x()
                break
            
            #checks if no command has been executed.
            if index == 8:
                main()        
        else:
            index = index + 1

#-------------------------------------------------------

#-------------------------------------------------------
#Function for command 'I':            
def command_i(i_m,i_n):
    global image                                    # create global variable, so that it can be accessed by other functions.
    image = zeros((int(i_m),int(i_n)),dtype='a5')   # create an array from the given inputs.
    image[:,:] = 'O'                                # set all array elements as color ('O')
    main()                                          # return to MAIN function
#-------------------------------------------------------

#-------------------------------------------------------    
#Function for command 'C':
def command_c():
    global image
    image[:,:] = 'O'                                # clear and set all array elements as color ('O')
    main()
#-------------------------------------------------------

#-------------------------------------------------------
#Function for command 'L':
def command_l(l_x,l_y,l_c):
    global image
    #convert string to integer values.
    l_x = int(l_x)
    l_y = int(l_y)

    #compensate for base zero array.
    l_x = (l_x - 1)
    l_y = (l_y - 1)
   
    image[l_x,l_y] = l_c                            # set colour of image at pixel(X,Y) to colour (C)  
    main()
#-------------------------------------------------------

#-------------------------------------------------------    
#Function for command 'V':
def command_v(v_x,v_yo,v_yt,v_c):
    global image
    v_x = int(v_x)
    v_yo = int(v_yo)
    v_yt = int(v_yt)
    
    v_x  = (v_x - 1)
    v_yo = (v_yo - 1)

    
    image[v_yo:v_yt,v_x] = v_c                      # vertical segment at column(X), between row(Y1) and (Y2) of colour (C)
    main()    
#-------------------------------------------------------

#-------------------------------------------------------    
#Function for command 'H':
def command_h(h_xo,h_xt,h_y,h_c):
    global image
    h_xo = int(h_xo)
    h_xt = int(h_xt)  

    h_xo = (h_xo - 1)
    h_y = (h_y - 1)
    
    image[h_y,h_xo:h_xt] = h_c                      # horizontal segment at row(Y), between column (X1) and (X2) of colour (C)
    main()
#-------------------------------------------------------

#-------------------------------------------------------    
#Function for command 'F':
def command_f(fx,fy,fc):
    image = commandf.run(fx,fy,fc)                  # execute function for command(F) and pass input data.
    main()
#-------------------------------------------------------

#-------------------------------------------------------    
#Function for command 'S':
def command_s():
    imagex = image                                  
    print str(imagex).replace(' ','').replace('.','').replace('[','').replace(']','').replace("'"," ") # display the IMAGE array after it has been filtered from array syntaxes
    main()
#-------------------------------------------------------

#-------------------------------------------------------    
#Function for command 'X':
def command_x():                                        # function to exit COMMAND PROMPT
    print 'TERMINATING THE PROGRAM NOW...PLEASE WAIT'   
    time.sleep(2)
    
#-------------------------------------------------------

#-------------------------------------------------------    
#Execute MAIN function
main()
#-------------------------------------------------------
