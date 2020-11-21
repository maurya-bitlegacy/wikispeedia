#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import pandas as pd
import urllib.parse


# In[2]:


tsv_file = open("articles.tsv")
articles = csv.reader(tsv_file)


# In[ ]:





# In[3]:


lis=[]
for row in articles:
    if len(row)>0 and row[0][0]!='#':
        lis.append([urllib.parse.unquote(row[0])])


# In[4]:


dic={}
index=1
for article in lis:
    dic[article[0]]="A"+str('{0:04}'.format(index))
    index+=1


# In[5]:


df = pd.DataFrame(dic.items(),columns=['Article_Name','Article_ID'])


# In[6]:


df.to_csv("article-ids.csv",index=False,encoding='utf-8')


# In[ ]:




