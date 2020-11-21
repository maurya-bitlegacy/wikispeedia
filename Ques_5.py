#!/usr/bin/env python
# coding: utf-8

# In[1]:


#pip install networkx


# In[1]:


import csv
import json
import pandas as pd
import urllib.parse
import itertools


# In[4]:


csv_file = open("edges.csv",encoding='utf-8')
edges = csv.reader(csv_file)
lis=[]
for row in edges:
    if row[0]!='From_ArticleID':
        lis.append(row)


# In[5]:


import networkx as nx
g=nx.Graph()
for edge in lis:
    g.add_edge(edge[0],edge[1])


# In[6]:


con = nx.connected_components(g)
comps=[]
for index,component in enumerate(con):
    comps.append(component)


# In[7]:


df1=pd.read_csv('article-ids.csv')
articles = df1['Article_ID'].to_list()
articles=set(articles)


# In[8]:


isolated = articles-comps[0]-comps[1]


# In[9]:


dicedges={}
dicdia={}
for comp in comps:
    sub = g.subgraph(comp).copy()
    dicedges[sub.number_of_nodes()]=sub.number_of_edges()
    dicdia[sub.number_of_nodes()]=nx.diameter(sub)


# In[ ]:


df1=pd.DataFrame(dicedges.items(),columns=['Nodes','Edges'])
df2=pd.DataFrame(dicdia.items(),columns=['Nodes','Diameter'])
df3=pd.merge(df1,df2,on='Nodes')


# In[ ]:


for vertex in isolated:
    df3.loc[len(df3.index)] = [1, 0, 0] 


# In[22]:


df3.to_csv('graph-components.csv',index=False,encoding='utf8')


# In[ ]:




