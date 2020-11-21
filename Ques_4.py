#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import json
import pandas as pd
import urllib.parse


# In[2]:


f = open("shortest-path-distance-matrix.txt", "r")
lis=[]
for i in range(4621):
    lis.append(f.readline())


# In[3]:


tsv_file = open("articles.tsv")
articles = csv.reader(tsv_file)
lis_art=[]
for row in articles:
    if len(row)>0 and row[0][0]!='#':
        lis_art.append([urllib.parse.unquote(row[0])])


# In[4]:


dic={}
csv_file = open("article-ids.csv",encoding='utf-8')
categories = csv.reader(csv_file)
for row in categories:
    dic[row[0]]=row[1]


# In[5]:


edge_list={}
for i in range(17,4621):
    j=i-17
    curstr = lis[i]
    for k in range(len(curstr)):
        if curstr[k]=='1':
            if edge_list.get(lis_art[j][0])==None:
                edge_list[lis_art[j][0]]=[lis_art[k][0]]
            else:
                edge_list[lis_art[j][0]]+=[lis_art[k][0]]
with open("edges.json","w",encoding='utf-8') as temp:
    json.dump(edge_list,temp)


# In[6]:


article=[]
neighbors=[]
for (key1,val1) in edge_list.items():
    for neighbor in val1:
        article.append(dic[key1])
        neighbors.append(dic[neighbor])
edges = pd.DataFrame(list(zip(article,neighbors)), columns =['From_ArticleID','To_ArticleID'])
    


# In[7]:


edges.to_csv("edges.csv",index=False)


# In[ ]:





# In[ ]:




