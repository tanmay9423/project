#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt 
import numpy as np 
from sklearn import datasets, linear_model 
import pandas as pd 


# In[6]:


# Load CSV and columns 
df = pd.read_csv("C:\\Users\\tanma\\Downloads\\avg readings.csv") 
   
Y = df['Mean'] 
X = df['Time']
print(X)
print(Y)


# In[3]:


X=X.values.reshape(len(X),1) 
Y=Y.values.reshape(len(Y),1) 


# In[5]:


print(X)
print(Y)


# In[7]:


# Split the targets into training/testing sets
from sklearn.model_selection import train_test_split 
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.4, 
                                                    random_state=1) 
print(X_train)
print(X_test)
print(Y_train)
print(Y_test)


# In[8]:


# Plot outputs 
plt.scatter(X_test, Y_test,  color='black') 
plt.title('Test Data') 
plt.xlabel('Time') 
plt.ylabel('Mean') 
plt.xticks(()) 
plt.yticks(()) 


# In[10]:


# Create linear regression object 
regr = linear_model.LinearRegression() 
print(regr)


# In[12]:


# Train the model using the training sets 
regr.fit([X_train], [Y_train]) 


# In[21]:


# Plot outputs 
plt.plot([X_test], regr.predict([X_test]), color='red',linewidth=1) 
plt.show() 


# In[ ]:




