#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import libraries
from bs4 import BeautifulSoup
import requests


# In[2]:


# get url
url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"
page = requests.get(url)
page


# In[3]:


# get the html code
soup = BeautifulSoup(page.text, 'html')
soup


# In[4]:


# find the table method 1
table_1 = soup.find_all('table')[1]


# In[5]:


# find the table method 2
soup.find('table', class_ = "wikitable sortable")


# In[6]:


table_1


# In[9]:


# find columns names
columns = table_1.find_all('th')


# In[10]:


columns


# In[11]:


columns_titles =[title.text.strip() for title in columns]


# In[12]:


columns_titles


# In[ ]:




