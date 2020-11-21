#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import pandas as pd
import urllib.parse
import copy


# In[2]:


csv_file = open("paths_finished.csv",encoding='utf-8')
paths = csv.reader(csv_file)
lis=[]
for row in paths:
    if len(row)>0 and row[0][0]!='#':
        lis.append(row)


# In[3]:


df1=pd.read_csv('category-pairs.csv')
fromcat=df1['From_Category'].tolist()
tocat=df1['To_Category'].tolist()


# In[4]:


df1=pd.read_csv("finished-paths-no-back.csv")


# In[5]:


csv_file = open("paths_finished.tsv",encoding='utf-8')
paths = csv.reader(csv_file)
lis=[]
for row in paths:
    if len(row)>0 and row[0][0]!='#':
        lis.append(row)
source_des=[]
for row in lis:
    row=row[0].split('\t')[3].split(';')
    source=urllib.parse.unquote(row[0])
    dest=urllib.parse.unquote(row[-1])
    source_des.append([source,dest])


# In[6]:


df=pd.read_csv('article-subcategories.csv',header=None,encoding='utf8')
csv_file = open("article-ids.csv",encoding='utf-8')
categories = csv.reader(csv_file)
dic={}
for row in categories:
    dic[row[1]]=row[0]
categs={}
for index,row in df.iterrows():
    categs[dic[row[0]]]=row[1]


# In[7]:


dicratio={}
diccnt={}
for index,row in df1.iterrows():
    ratio= row['Ratio']
    entry=source_des[index]
    source_art=entry[0]
    dest_art=entry[1]   
    source_cats=categs[source_art].split(',')
    dest_cats=categs[dest_art].split(',')
    pairs=[]
    for cat in source_cats:
        for catt in dest_cats:
            pair=cat,catt
            pairs.append(pair)
    pairs=list(set(pairs))
    for pair in pairs:
        if dicratio.get(pair)==None:
            dicratio[pair]=ratio
            diccnt[pair]=1
        else:
            dicratio[pair]+=ratio
            diccnt[pair]+=1
avgratio={}
for k,v in dicratio.items():
    avgratio[str(k[0])+" "+str(k[1])]=dicratio[k]/diccnt[k]


# In[8]:


df2=pd.DataFrame(avgratio.items(),columns=['Category','Ratio_of_human_to_shortest'])
df2=df2.sort_values(by=['Category'])
df4=pd.DataFrame()
df4[['From_Category','To_Category']]=df2.Category.str.split(expand=True)
df2=df2.drop(['Category'],axis=1)
df5=pd.concat([df4,df2],axis=1)


# In[9]:


df5.to_csv('category-ratios.csv',index=False,encoding='utf8')


# In[ ]:




