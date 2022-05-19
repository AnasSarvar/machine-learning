#!/usr/bin/env python
# coding: utf-8

# In[15]:


import numpy as np

import pandas as pd

data = pd.DataFrame(data=pd.read_csv('play1.csv'))

print(data)


# In[17]:


conc = np.array(data.iloc[:,0:-1])
print(conc)


# In[19]:


tar = np.array(data.iloc[:,-1])
print(tar)


# In[20]:


def cand(conc, tar): 

    specific = conc[0].copy()
    
    print("\nSpecific Boundary: ", specific)
    general = [["?" for i in range(len(specific))] for i in range(len(specific))]
    print("\nGeneric Boundary: ",general)  

    
    for i, val in enumerate(conc):
        print("\nInstance", i+1 , "is ", val)

        if tar[i] == "yes":
            print("Instance is Positive ")
            for x in range(len(specific)): 
                if val[x]!= specific[x]:                    
                    specific[x] ='?'                     
                    general[x][x] ='?'
                
        if tar[i] == "no":            
            print("Instance is Negative ")
            for x in range(len(specific)): 
                if val[x]!= specific[x]:                    
                    general[x][x] = specific[x]                              
                else:                    
                    general[x][x] = '?'        
        
        print("Specific Bundary after ", i+1, "Instance is ", specific)         
        print("Generic Boundary after ", i+1, "Instance is ", general)
        print("\n")

    indices = [i for i, val in enumerate(general)
     if val == ['?', '?', '?', '?', '?', '?']]    
    
    for i in indices:   
        general.remove(['?', '?', '?', '?', '?', '?']) 
    
    return specific, general 
s_final, g_final = cand(conc, tar)

print("Final Specific: ", s_final, sep="\n")

print("Final General: ", g_final, sep="\n")


# In[ ]:




