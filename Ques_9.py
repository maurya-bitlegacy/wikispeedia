#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import re
import json
import math
import pandas as pd
import urllib.parse


# In[2]:


csv_file = open("paths_finished.csv",encoding='utf-8')
paths = csv.reader(csv_file)
lis=[]
for row in paths:
    if len(row)>0 and row[0][0]!='#':
        lis.append(row)


# In[3]:


df=pd.read_csv('article-categories.csv')
df9=pd.read_csv('article-subcategories.csv',header=None)


# In[4]:


dic_id={}
dic_idrev={}
csv_file = open("article-ids.csv",encoding='utf-8')
ids = csv.reader(csv_file)
for row in ids:
    if row[0]=='Article_Name':
        continue
    dic_id[row[0]]=row[1]
    dic_idrev[row[1]]=row[0]


# In[5]:


article_categories={}
for index,row in df.iterrows():
    article_categories[row['Article_ID']]=row['Category_ID']
article_categories
article_subcategories={}
for index,row in df9.iterrows():
    article_subcategories[row[0]]=row[1]


# In[6]:


dic={}
revdic={}
csv_file = open("category-ids.csv",encoding='utf-8')
categories = csv.reader(csv_file)
for row in categories:
    if row[1]=='Category_ID':
        continue
    dic[row[1]]=row[0]
    revdic[row[0]]=row[1]


# In[ ]:





# In[7]:


graph=[]
csv_file = open("edges.csv",encoding='utf-8')
edges = csv.reader(csv_file)
for row in edges:
    if row[0]!='From_ArticleID':
        graph.append([dic_idrev[row[0]],dic_idrev[row[1]]])
    


# In[8]:


import networkx as nx
g = nx.DiGraph()
g.add_edges_from(graph)


# In[9]:


numberoftimes={}
numberofpaths={}
numberoftimesShort={}
numberofpathsShort={}
for row in lis:
    paths=row[3].split(';')
    subcategories=[]
    for i in range (len(paths)):
        if paths[i]=='<':
            while(paths[i-1]=="" or paths[i-1]=="<"):
                i=i-1
            paths[i-1]=""    
    for article in paths:
        if article!='<' and article!="":
            subcategories+=(article_subcategories[dic_id[urllib.parse.unquote(article)]]).split(',')
    uniquecategories=list(set(subcategories))
    for category in subcategories:
        if numberoftimes.get(category)==None:
            numberoftimes[category]=1
        else:
            numberoftimes[category]+=1
    for category in uniquecategories:
        if numberofpaths.get(category)==None:
            numberofpaths[category]=1
        else:
            numberofpaths[category]+=1
    startnode=urllib.parse.unquote(paths[0])
    endnode=urllib.parse.unquote(paths[-1])
    subcategories=[]        
    shortestpath=nx.shortest_path(g, startnode, endnode)
    for article in shortestpath:
        subcategories+=(article_subcategories[dic_id[urllib.parse.unquote(article)]]).split(',')   
    uniquecategories=list(set(subcategories))
    for category in subcategories:
        if numberoftimesShort.get(category)==None:
            numberoftimesShort[category]=1
        else:
            numberoftimesShort[category]+=1
    for category in uniquecategories:
        if numberofpathsShort.get(category)==None:
            numberofpathsShort[category]=1
        else:
            numberofpathsShort[category]+=1


# In[10]:


for k in dic.keys():
    if numberoftimes.get(k)==None:
        numberoftimes[k]=0
        numberofpaths[k]=0
for k in dic.keys():
    if numberoftimesShort.get(k)==None:
        numberoftimesShort[k]=0
        numberofpathsShort[k]=0


# In[11]:


df1=pd.DataFrame(numberoftimes.items(),columns=['Category_ID','Number_of_human_times_traversed'])


# In[12]:


df2=pd.DataFrame(numberofpaths.items(),columns=['Category_ID','Number_of_human_paths_traversed'])


# In[13]:


df3=pd.DataFrame(numberofpathsShort.items(),columns=['Category_ID','Number_of_shortest_paths_traversed'])


# In[14]:


df4=pd.DataFrame(numberoftimesShort.items(),columns=['Category_ID','Number_of_shortest_times_traversed'])


# In[15]:


df5=pd.merge(df2,df1,on='Category_ID')
df6=pd.merge(df5,df3,on='Category_ID')
df7=pd.merge(df6,df4,on='Category_ID')


# In[16]:


df7=df7.sort_values(by=['Category_ID'])


# In[17]:


df7.to_csv('category-subtree-paths.csv',index=False,encoding='utf8')


# In[ ]:




