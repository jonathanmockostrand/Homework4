###########################################################
##                                                       ##
##    Jonathan Mocko-Strand                              ##
##    Dept. of Geology & Geophysics, TAMU. 2013-10-22    ##
##    Python for Geoscientists                           ##
##    Homework Assignment 4                              ##
##                                                       ##
###########################################################

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import urllib

def url_cm_import(filename):

    '''
    This function will import a specific color map directly from:
        http://geography.uoregon.edu/datagraphics/
    The available color map options can be found on the website.
    
    The imput file is the .txt color map filename
    
    The output is a 100x100 cell plot of randomly generated numbers
    with the chosen color bar. 
    
    '''
    url = 'http://geography.uoregon.edu/datagraphics/color/'+filename
    
    cm_data = urllib.urlopen(url)
    
    r=[]; g=[]; b=[];
    
    for line in cm_data.readlines()[2:]:
        colors = line.split()
        r.append(float(colors[0]))
        g.append(float(colors[1]))
        b.append(float(colors[2]))
        
    cm_length = len(r)
    red_component   = [((float(n)/(cm_length-1)), r[n-1], r[n]) for n in range(cm_length)]
    green_component = [((float(n)/(cm_length-1)), g[n-1], g[n]) for n in range(cm_length)]
    blue_component  = [((float(n)/(cm_length-1)), b[n-1], b[n]) for n in range(cm_length)]
    
    cdict = {'red'  : red_component,
             'green': green_component,
             'blue' : blue_component}

    return matplotlib.colors.LinearSegmentedColormap('url_cm_import',cdict,256)
    
if __name__ == '__main__': 
    url_cm_import = url_cm_import('GrMg_16.txt')
    plt.title('GrMg_16 Color Map of Randomly Generated Numbers\n' )
    plt.pcolor(np.random.rand(100,100),cmap=url_cm_import)
    plt.colorbar()
    plt.show()
    plt.savefig("My_colormap.pdf")