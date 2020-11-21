#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import pandas as pd
import urllib.parse


# In[2]:


df=pd.read_csv("article-ids.csv",encoding="utf8")


# In[4]:


tsv_file = open("categories.tsv")
categories = csv.reader(tsv_file)
lis=[]
for row in categories:
    if len(row)>0 and row[0][0]!='#':
        lis.append([urllib.parse.unquote(row[0])])


# In[5]:


csv_file = open("category-ids.csv")
categories = csv.reader(csv_file)
diccategories={}
for row in categories:
    diccategories[row[0]]=row[1]


# In[6]:


dic={}
for row in lis:
    article=row[0].split('\t')[0]
    category=row[0].split('\t')[1]
    
    if dic.get(article)==None:
        dic[article]=[diccategories[category]]
    else:
        dic[article]+=[diccategories[category]]
        
    


# In[7]:


for k,v in dic.items():
    v=list(set(v))
    dic[k]=','.join(sorted(v))


# In[8]:


article_list=list(df['Article_Name'])
for article in article_list:
    if dic.get(article)==None:
        dic[article]='C0001'
df1 = pd.DataFrame(dic.items(),columns=['Article_Name','Category_ID'])


# In[9]:


df2=pd.merge(df,df1,on='Article_Name')
df2=df2.drop(["Article_Name"], axis=1)
df2=df2.sort_values(by=['Article_ID'])


# In[10]:


df2.to_csv('article-categories.csv',index=False,encoding='utf8')


# In[11]:


dicsub={}
for row in lis:
    article=row[0].split('\t')[0]
    category=row[0].split('\t')[1].split('.')[1:]
    categs=['subject']
    for i in range(len(category)):
        categs.append(categs[-1]+'.'+category[i])
    for c in categs:
        if dicsub.get(article)==None:
            dicsub[article]=[diccategories[c]]
        else:
            dicsub[article]+=[diccategories[c]]
for k,v in dicsub.items():
    dicsub[k]=sorted(list(set(dicsub[k])))


# In[13]:


for k,v in dicsub.items():
    v=list(set(v))
    dicsub[k]=','.join(sorted(v))


# In[14]:


for article in article_list:
    if dicsub.get(article)==None:
        dicsub[article]='C0001'
df3 = pd.DataFrame(dicsub.items(),columns=['Article_Name','Category_ID'])


# In[15]:


df4=pd.merge(df,df3,on='Article_Name')
df4=df4.drop(["Article_Name"], axis=1)
df4=df4.sort_values(by=['Article_ID'])


# In[16]:


df4.to_csv('article-subcategories.csv',index=False,header=False,encoding='utf8')


# In[ ]:




