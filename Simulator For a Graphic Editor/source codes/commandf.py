from numpy import *
import __main__ 

# function for command(F)

def run(fx,fy,fc):
    a = __main__.image  # create local variable(a) of variable(image) from grapheditor.py 
    fx = int(fx)        # convert string to integer values    
    fy = int(fy)

    fx = (fx - 1)       # compensate for base zero arrays
    fy = (fy - 1) 

    oc = a[fx,fy]       # store original color of pixel(X,Y)
    a[fx,fy] = fc       # change color of pixel(X,Y) to colour(C)

    # define common sides of pixel(X,Y)
    top = [fx - 1,fy]       
    bottom = [fx + 1,fy]
    left = [fx,fy - 1]
    right = [fx,fy + 1]

    # change colours of the common sides shared with pixel(X,Y)
    a[top[0],top[1]] = fc
    a[bottom[0],bottom[1]] = fc
    a[left[0],left[1]] = fc
    a[right[0],right[1]] = fc

    # extract information on the image features
    shape = a.shape
    xmax = shape[0]
    ymax = shape[1]

    # initialise counters
    ax = 0
    ay = 0

    # looping through the entire image to create a region common to pixel(X,Y) based on its common sides and original colour
    for x in xrange(a.size + 4):
        if ay != (ymax):
            if a[ax,ay] == oc:
                a[ax,ay] = fc
                ay = ay + 1
            else:
                ay = ay + 1
        else:
            if ax != (xmax):
                ax = ax + 1
                ay = 0
                continue

    return a    # pass the newly created image back to __main__
