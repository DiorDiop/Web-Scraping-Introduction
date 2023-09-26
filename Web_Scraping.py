#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import the libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError


# In[ ]:


# get the url
html = urlopen('https://www.projectpro.io/article/etl-projects-ideas-for-practice/563')


# In[ ]:


# print the code
print(html.read())


# In[ ]:


# get the title
def getTitle(url):
    try:
        html = urlopen(url)
    except HTTOError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "lxml")
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title


# In[ ]:


title = getTitle("https://www.projectpro.io/article/etl-projects-ideas-for-practice/563")
if title == None:
    print("Title Not Found")
else:
    print(title)


# In[ ]:




