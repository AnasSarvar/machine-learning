#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np


# In[4]:


data = pd.read_csv('play1.csv')


# In[5]:



data


# In[6]:


concepts = np.array(data)[:,:-1]


# In[7]:



concepts


# In[8]:


target = np.array(data)[:,-1]


# In[9]:



target


# In[27]:


def train(con, tar):
    for i, val in enumerate(tar):
        if val == 'yes':
            specific_h = con[i].copy()
            break
            
    for i, val in enumerate(con):
        if tar[i] == 'yes':
            for x in range(len(specific_h)):
                if val[x] != specific_h[x]:
                    specific_h[x] = '?'
                else:
                    pass
            print (specific_h)


# In[29]:


print(train(concepts, target))


# In[ ]:




