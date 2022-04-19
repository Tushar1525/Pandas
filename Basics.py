#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


tab1 = {
    "Name":["Tushar", "Suman", "Rishi"],
    "Subject":["DSA","DBMS","MCO"],
    "Marks":[97,85,90]
}


# In[3]:


df = pd.DataFrame(tab1)


# In[4]:


df


# In[5]:


df.to_csv('Marks.csv')


# In[6]:


df.describe()


# In[7]:


newdf = pd.DataFrame(np.random.rand(300,5), index = np.arange(300))


# In[8]:


newdf.head()


# In[9]:


newdf.dtypes


# In[10]:


df.dtypes


# In[11]:


ser = pd.Series(np.random.rand(10))


# In[12]:


ser


# In[13]:


df.loc[[0,1]]


# In[14]:


df = pd.read_csv('Marks.csv')


# In[15]:


df


# In[16]:


employee = {
    "ID":[101 ,102 ,103 ,104 ,105 ],
    "Name":["Tushar","Suman","Rishi","Dev","Ayush"],
    "Designation":["Buisness Analyst","Technical Architect","Manager","HR Analyst","Salesman"],
    "Salary":[50000,60000,70000,45000,35000]
}


# In[17]:


df = pd.DataFrame(employee)


# In[18]:


df


# In[19]:


df.to_csv('Employee.csv')


# In[20]:


employee['Name'][2]


# In[21]:


employee['Salary'][2] = 65000


# In[22]:


df = pd.DataFrame(employee)


# In[23]:


df


# In[24]:


df.set_index("ID")


# In[25]:


type(df)


# In[26]:


emp = df


# In[27]:


emp


# In[28]:


emp.rename(columns = {'Name' : 'emp_name'}, inplace = True)


# In[29]:


emp


# In[30]:


city = ['Delhi', 'Bangalore', 'Chennai', 'Patna', 'Mumbai']


# In[31]:


emp['City'] = city


# In[32]:


emp


# In[33]:


emp['ID']


# In[34]:


df = pd.read_csv('Employee.csv')


# In[ ]:




