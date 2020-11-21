#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import pandas as pd
import urllib.parse


# In[2]:


csv_file = open("paths_unfinished.tsv",encoding='utf-8')
paths = csv.reader(csv_file)
lis=[]
for row in paths:
    if len(row)>0 and row[0][0]!='#':
        lis.append(row)


# In[3]:


source_dest=[]
for row in lis:
    row=row[0].split('\t')
    source=urllib.parse.unquote(row[3].split(';')[0])
    dest=urllib.parse.unquote(row[4])
    source_dest.append([source,dest])


# In[4]:


df=pd.read_csv('article-subcategories.csv',header=None,encoding='utf8')


# In[5]:


csv_file = open("article-ids.csv",encoding='utf-8')
categories = csv.reader(csv_file)
dic={}
for row in categories:
    dic[row[1]]=row[0]


# In[6]:


categs={}
for index,row in df.iterrows():
    categs[dic[row[0]]]=row[1]


# In[7]:


categs['Test']="C0001"
categs['Netbook']="C0001"
categs['Podcast']="C0001"
categs['Christmas']="C0001"
categs['Sportacus']="C0001"
categs['Black_ops_2']="C0001"
categs['Western_Australia']="C0001"
categs['The_Rock']="C0001"
categs['Great']="C0001"
categs['Fats']="C0001"
categs['Bogota']="C0001"
categs['The']="C0001"
categs['Rat']="C0001"


# In[8]:


uncat_pairs={}
for entry in source_dest:
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
        if uncat_pairs.get(pair)==None:
            uncat_pairs[pair]=1
        else:
            uncat_pairs[pair]+=1


# In[9]:


csv_file = open("paths_finished.tsv",encoding='utf-8')
paths = csv.reader(csv_file)
lis=[]
for row in paths:
    if len(row)>0 and row[0][0]!='#':
        lis.append(row)


# In[10]:


source_des=[]
for row in lis:
    row=row[0].split('\t')[3].split(';')
    source=urllib.parse.unquote(row[0])
    dest=urllib.parse.unquote(row[-1])
    source_des.append([source,dest])


# In[11]:


fincat_pairs={}
for entry in source_des:
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
        if fincat_pairs.get(pair)==None:
            fincat_pairs[pair]=1
        else:
            fincat_pairs[pair]+=1


# In[12]:


percentage_fin={}
percentage_unfin={}
for k,v in uncat_pairs.items():
    percentage_unfin[str(k[0])+" "+str(k[1])]=(v/(v+fincat_pairs.get(k,0)))*100
for k,v in fincat_pairs.items():
    percentage_fin[str(k[0])+" "+str(k[1])]=(v/(v+uncat_pairs.get(k,0)))*100
for k,v in percentage_unfin.items():
    if percentage_fin.get(k)==None:
        percentage_fin[k]=0
for k,v in percentage_fin.items():
    if percentage_unfin.get(k)==None:
        percentage_unfin[k]=0


# In[13]:


df1=pd.DataFrame(percentage_fin.items(),columns=['Category','Percentage_of_finished_paths'])
df2=pd.DataFrame(percentage_unfin.items(),columns=['Category','Percentage_of_unfinished_paths'])
df3=pd.merge(df1,df2,on='Category')
df3=df3.sort_values(by=['Category'])


# In[14]:


df4=pd.DataFrame()
df4[['From_Category','To_Category']]=df3.Category.str.split(expand=True)
df3=df3.drop(['Category'],axis=1)
df5=pd.concat([df4,df3],axis=1)


# In[15]:


df5.to_csv('category-pairs.csv',index=False,encoding='utf8')


# In[ ]:




