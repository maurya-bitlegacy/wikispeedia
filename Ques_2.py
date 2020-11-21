#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import pandas as pd
import urllib.parse


# In[2]:


tsv_file = open("categories.tsv")
categories = csv.reader(tsv_file)


# In[3]:


lis=[]
for row in categories:
    if len(row)>0 and row[0][0]!='#':
        lis.append([urllib.parse.unquote(row[0])])


# In[4]:


categories=[]
for row in lis:
    categories.append(row[0].split('\t')[1])
categories=sorted(list(set(categories)))
maxlen=0
for i in range(len(categories)):
    categories[i]=list(categories[i][8:].split('.'))
    maxlen=max(maxlen,len(categories[i]))


# In[5]:


dic={}
dic['subject']='C0001'
index=2
for i in range(maxlen):
    for j in range(len(categories)):
        if len(categories[j])>i and dic.get("subject."+".".join(categories[j][0:i+1]))==None:
            dic["subject."+".".join(categories[j][0:i+1])]="C"+str('{0:04}'.format(index))
            index+=1

    


# In[6]:


sorted_dic={}
for k,v in sorted(dic.items()):
    sorted_dic[k]=v


# In[7]:


df = pd.DataFrame(sorted_dic.items(),columns=['Category_Name','Category_ID'])
df.to_csv("category-ids.csv",index=False,encoding='utf-8')


# In[8]:


wholecategs=[]
for row in lis:
    wholecategs.append(row[0].split('\t')[1])
wholecategs=sorted(list(set(wholecategs)))


# In[9]:


dic_w={}
for categ in wholecategs:
    dic_w[categ]=sorted_dic[categ]


# In[10]:


df1 = pd.DataFrame(dic_w.items(),columns=['Category_Name','Category_ID'])
df1.to_csv("wholecategory-ids.csv",index=False,encoding='utf-8')


# In[11]:





# In[ ]:




