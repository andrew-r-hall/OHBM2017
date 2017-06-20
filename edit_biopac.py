import matplotlib.pyplot as plt
import nibabel as nib
import numpy as np
import sys
import os

#phys = np.genfromtxt(sys.argv[1], dtype=None)
phys = np.genfromtxt('L11_1706092017-06-09T15_16_20_rest.txt', dtype=None)


triggers = np.where(np.diff(phys[:,3]) > 3)
triggers = triggers[0]
if(len(triggers) > 0):
    delta = np.diff(triggers)
        
    resp_raw = phys[:,1]
    card_raw = phys[:,2]
    resp_bold = resp_raw[triggers[1:-1:2]]
    card_bold = card_raw[triggers[1:-1:2]]
    
    #resp_vaso = resp_raw[triggers[0]:triggers[-2]]
    #card_vaso = card_raw[triggers[0]:triggers[-2]]
               
    resp_bold.tofile('resp_bold.1D', sep='\n')
    card_bold.tofile('card_bold.1D', sep='\n') 
    resp_raw.tofile('raw_resp.1D' , sep='\n')
    card_raw.tofile('raw_card.1D' , sep='\n')
    #resp_vaso.tofile('resp_vaso.1D', sep='\n')
    #card_vaso.tofile('card_vaso.1D', sep='\n')        
