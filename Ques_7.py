#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import re
import json
import pandas as pd
import urllib.parse


# In[2]:


finpathsback = pd.read_csv('finished-paths-back.csv',encoding='utf-8')
finpathsnoback= pd.read_csv('finished-paths-no-back.csv',encoding='utf-8')


# In[4]:


equal=0
onemore=0
twomore=0
threemore=0
fourmore=0
fivemore=0
sixmore=0
sevenmore=0
eightmore=0
ninemore=0
tenmore=0
elevenormore=0
cntpaths=0
for index,row in finpathsback.iterrows():
    if int(row['Human_Path_Length'])-int(row['Shortest_Path_Length'])==0:
        equal+=1
    elif int(row['Human_Path_Length'])-int(row['Shortest_Path_Length'])==1:
        onemore+=1
    elif int(row['Human_Path_Length'])-int(row['Shortest_Path_Length'])==2:
        twomore+=1
    elif int(row['Human_Path_Length'])-int(row['Shortest_Path_Length'])==3:
        threemore+=1
    elif int(row['Human_Path_Length'])-int(row['Shortest_Path_Length'])==4:
        fourmore+=1
    elif int(row['Human_Path_Length'])-int(row['Shortest_Path_Length'])==5:
        fivemore+=1
    elif int(row['Human_Path_Length'])-int(row['Shortest_Path_Length'])==6:
        sixmore+=1
    elif int(row['Human_Path_Length'])-int(row['Shortest_Path_Length'])==7:
        sevenmore+=1
    elif int(row['Human_Path_Length'])-int(row['Shortest_Path_Length'])==8:
        eightmore+=1
    elif int(row['Human_Path_Length'])-int(row['Shortest_Path_Length'])==9:
        ninemore+=1
    elif int(row['Human_Path_Length'])-int(row['Shortest_Path_Length'])==10:
        tenmore+=1
    elif int(row['Human_Path_Length'])-int(row['Shortest_Path_Length'])>10:
        elevenormore+=1
    cntpaths+=1
equal=equal*100/cntpaths
onemore=onemore*100/cntpaths
twomore=twomore*100/cntpaths
threemore=threemore*100/cntpaths
fourmore=fourmore*100/cntpaths
fivemore=fivemore*100/cntpaths
sixmore=sixmore*100/cntpaths
sevenmore=sevenmore*100/cntpaths
eightmore=eightmore*100/cntpaths
ninemore=ninemore*100/cntpaths
tenmore=tenmore*100/cntpaths
elevenormore=elevenormore*100/cntpaths


# In[5]:


equall=0
onemoree=0
twomoree=0
threemoree=0
fourmoree=0
fivemoree=0
sixmoree=0
sevenmoree=0
eightmoree=0
ninemoree=0
tenmoree=0
elevenormoree=0
cntpaths=0
for index,row in finpathsnoback.iterrows():
    if int(row['Human_Path_Length'])-int(row['Shortest_Path_Length'])==0:
        equall+=1
    elif int(row['Human_Path_Length'])-int(row['Shortest_Path_Length'])==1:
        onemoree+=1
    elif int(row['Human_Path_Length'])-int(row['Shortest_Path_Length'])==2:
        twomoree+=1
    elif int(row['Human_Path_Length'])-int(row['Shortest_Path_Length'])==3:
        threemoree+=1
    elif int(row['Human_Path_Length'])-int(row['Shortest_Path_Length'])==4:
        fourmoree+=1
    elif int(row['Human_Path_Length'])-int(row['Shortest_Path_Length'])==5:
        fivemoree+=1
    elif int(row['Human_Path_Length'])-int(row['Shortest_Path_Length'])==6:
        sixmoree+=1
    elif int(row['Human_Path_Length'])-int(row['Shortest_Path_Length'])==7:
        sevenmoree+=1
    elif int(row['Human_Path_Length'])-int(row['Shortest_Path_Length'])==8:
        eightmoree+=1
    elif int(row['Human_Path_Length'])-int(row['Shortest_Path_Length'])==9:
        ninemoree+=1
    elif int(row['Human_Path_Length'])-int(row['Shortest_Path_Length'])==10:
        tenmoree+=1
    elif int(row['Human_Path_Length'])-int(row['Shortest_Path_Length'])>10:
        elevenormoree+=1
    cntpaths+=1
equall=equall*100/cntpaths
onemoree=onemoree*100/cntpaths
twomoree=twomoree*100/cntpaths
threemoree=threemoree*100/cntpaths
fourmoree=fourmoree*100/cntpaths
fivemoree=fivemoree*100/cntpaths
sixmoree=sixmoree*100/cntpaths
sevenmoree=sevenmoree*100/cntpaths
eightmoree=eightmoree*100/cntpaths
ninemoree=ninemoree*100/cntpaths
tenmoree=tenmoree*100/cntpaths
elevenormoree=elevenormoree*100/cntpaths

    


# In[6]:


wbc = {'Equal_Length':  [equal],
        'Larger_by_1': [onemore],
       'Larger_by_2': [twomore],
       'Larger_by_3': [threemore],
       'Larger_by_4': [fourmore],
       'Larger_by_5': [fivemore],
       'Larger_by_6': [sixmore],
       'Larger_by_7': [sevenmore],
       'Larger_by_8': [eightmore],
       'Larger_by_9': [ninemore],
       'Larger_by_10': [tenmore],
       'Larger_by_more_than_10': [elevenormore]
        }
df = pd.DataFrame (wbc, columns = ['Equal_Length','Larger_by_1','Larger_by_2','Larger_by_3','Larger_by_4','Larger_by_5','Larger_by_6','Larger_by_7','Larger_by_8','Larger_by_9','Larger_by_10','Larger_by_more_than_10'])


# In[8]:


wobc = {'Equal_Length':  [equall],
        'Larger_by_1': [onemoree],
       'Larger_by_2': [twomoree],
       'Larger_by_3': [threemoree],
       'Larger_by_4': [fourmoree],
       'Larger_by_5': [fivemoree],
       'Larger_by_6': [sixmoree],
       'Larger_by_7': [sevenmoree],
       'Larger_by_8': [eightmoree],
       'Larger_by_9': [ninemoree],
       'Larger_by_10': [tenmoree],
       'Larger_by_more_than_10': [elevenormoree]
        }
df1 = pd.DataFrame (wobc, columns = ['Equal_Length','Larger_by_1','Larger_by_2','Larger_by_3','Larger_by_4','Larger_by_5','Larger_by_6','Larger_by_7','Larger_by_8','Larger_by_9','Larger_by_10','Larger_by_more_than_10'])


# In[10]:


df.to_csv('percentage-paths-back.csv',index=False)
df1.to_csv('percentage-paths-no-back.csv',index=False)


# In[ ]:




