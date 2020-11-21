#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import re
import json
import pandas as pd
import urllib.parse


# In[2]:


tsv_file = open("paths_finished.tsv")
articles = csv.reader(tsv_file)


# In[3]:


with open("paths_finished.tsv", 'r',encoding='utf-8') as myfile:
    with open("paths_finished.csv", 'w',encoding='utf-8') as csv_file:
        for line in myfile:
            fileContent = re.sub("\t", ",", line)
            csv_file.write(fileContent)


# In[4]:


csv_file = open("paths_finished.csv",encoding='utf-8')
paths = csv.reader(csv_file)
lis=[]
for row in paths:
    if len(row)>0 and row[0][0]!='#':
        lis.append(row)


# In[5]:


reader = csv.reader(open('article-ids.csv', 'r',encoding='utf-8'))
d = {}
for row in reader:
    if row[1]=='Article_ID':
        continue
    k=int(row[1].split('A')[1])-1
    v=row[0]
    d[v]=k


# In[6]:


f = open("shortest-path-distance-matrix.txt", "r")
liss=[]
for i in range(4621):
    liss.append(f.readline())
pruned_lis=[]
for list in liss:
    if list[0]!='#' and list[0]!='\n':
        pruned_lis+=[list]


# In[8]:


paths=[]
human_wbc=[]
human_wobc=[]
shortest=[]
ratio_wbc=[]
ratio_wobc=[]
for path in lis:
    pathlis=path[3].split(';')
    curpath=urllib.parse.unquote(pathlis[0])+'->'+urllib.parse.unquote(pathlis[-1])
    lenpath_wbc=len(pathlis)-1
    if '<' in pathlis:
        lenpath_wobc=lenpath_wbc-2*pathlis.count('<')
    else:
        lenpath_wobc=lenpath_wbc
    shorpath=pruned_lis[d[urllib.parse.unquote(pathlis[0])]][d[urllib.parse.unquote(pathlis[-1])]]
    if shorpath=='_' or shorpath=='0':
        continue
    else:
        curratio_wbc=lenpath_wbc/int(shorpath)
        curratio_wobc=lenpath_wobc/int(shorpath)
    if(lenpath_wbc>0):
        paths.append(curpath)
        human_wbc.append(lenpath_wbc)
        ratio_wbc.append(curratio_wbc)
        human_wobc.append(lenpath_wobc)
        shortest.append(shorpath)
        ratio_wobc.append(curratio_wobc)
    

wbc = pd.DataFrame(
    {'path': paths,
     'Human_Path_Length': human_wbc,
     'Shortest_Path_Length': shortest,
     'Ratio': ratio_wbc
    })
wobc = pd.DataFrame(
    {'path': paths,
     'Human_Path_Length': human_wobc,
     'Shortest_Path_Length': shortest,
     'Ratio': ratio_wobc
    })    


# In[9]:


wbc=wbc.drop(['path'],axis=1)


# In[10]:


wobc=wobc.drop(['path'],axis=1)


# In[11]:


wbc.to_csv("finished-paths-back.csv",index=False,encoding='utf-8')
wobc.to_csv("finished-paths-no-back.csv",index=False,encoding='utf-8')


# In[ ]:




