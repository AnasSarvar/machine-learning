#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv("gender_baseline.csv")
df


# In[2]:


df.isna().sum()


# In[3]:


df.head()


# In[4]:


df.hist()


# In[5]:


df.boxplot()


# In[6]:


print(df.describe())


# In[15]:


df.loc[0,'passenger_id'] = ''
df.loc[0,'survived']=''
df.to_csv("gender_baseline.csv")
df


# In[8]:


df.isna().sum()


# In[10]:


import pandas as pd
df = pd.read_csv("gender_baseline.csv")
df


# In[11]:


df.hist()


# In[12]:


df.boxplot()


# In[13]:


df.hist('survived')


# In[14]:


df.mean()


# In[ ]:




