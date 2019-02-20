# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 18:35:38 2018

@author: piskorz
"""

import numpy as np
from MDAnalysis.analysis.rms import rmsd


#%%

cell_vector = np.array([[  0.        ,   0.        ,   0.        ],       [ -1.71320009, -36.21490097,   0.        ],       [  1.71320009,  36.21490097,   0.        ],       [ 41.12530136,   0.        ,   0.        ],       [-41.12530136,   0.        ,   0.        ],       [ -0.48000002, -17.02689934,  36.91479874],       [  1.23320007,  19.18800163,  36.91479874],       [  0.48000002,  17.02689934, -36.91479874],       [ 39.41210175, -36.21490097,   0.        ],       [-39.41210175,  36.21490097,   0.        ],       [ -1.23320007, -19.18800163, -36.91479874],       [-39.89210129,  19.18800163,  36.91479874],       [ 40.64530182, -17.02689934,  36.91479874],       [ 39.89210129, -19.18800163, -36.91479874],       [-41.6053009 , -17.02689934,  36.91479874],       [-40.64530182,  17.02689934, -36.91479874],       [ 42.83850098,  36.21490097,   0.        ],       [ 41.6053009 ,  17.02689934, -36.91479874],       [ 42.35850143,  19.18800163,  36.91479874],       [-42.83850098, -36.21490097,   0.        ],       [-42.35850143, -19.18800163, -36.91479874],       [  2.19320011,  53.2417984 , -36.91479874],       [ -2.19320011, -53.2417984 ,  36.91479874],       [-38.9321022 ,  53.2417984 , -36.91479874],       [ 38.9321022 , -53.2417984 ,  36.91479874],       [-43.31850052, -53.2417984 ,  36.91479874],       [ 43.31850052,  53.2417984 , -36.91479874]], dtype=np.float32)

def inside(lst,reference,positions,positions2, cell_vector): 
    global upper
    global finished
    if len(lst)>0:
        for a in lst:
            temp_pos = positions2[a:a+1]
            
            # permutate over the periodic boundary conditions
            for vector in range(len(cell_vector)):

                rmsd1= rmsd(reference[:len(positions)+1], np.append(positions, temp_pos+cell_vector[vector],axis=0), superposition=True)
               
                if rmsd1<=upper:
                    positions1=np.append(positions, temp_pos+cell_vector[vector],axis=0)
                    lst_i=lst[:]
                    lst_i.remove(a)                                                     
                    inside(lst_i,reference,positions1,positions2, cell_vector)
    else:
        temp=rmsd(reference[:len(positions)], positions, superposition=True) 
        if upper>=temp:
            upper=temp

def rmsd_perm(lista, cell_vector=[[0.0, 0.0, 0.0]]):
    
    reference = lista[0]
    positions2 = lista[1]
    N=len(reference)
    global upper    
    lst0= range(N)
    
    # computation time of RMSD grows expotentially with the RMSD
    # thefore you might consider using cut-off, i.g.:
    # upper=4.0
    # instead of:
    upper=rmsd(reference,positions2,superposition=True)
    # becasue most of the time you are only intrested in close things not the things which are far apart
    
    # If it is the same frame return 0.0
    if (np.all(reference-positions2 < 10e-6)):
        return 0.0
    
    for a in lst0:
        lst1=lst0[:]
        lst1.remove(a)
        positions=positions2[a:a+1]
        inside(lst1,reference,positions,positions2, cell_vector)
    
    return upper
    

#%%%


















#%%



