#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests,re
from bs4 import BeautifulSoup


# In[2]:


browser = requests.session()
url = "https://tvshows4mobile.com/search/list_all_tv_series"
user_agent = {'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'}


# In[3]:


def open_url(url):
        html = browser.get(url,headers =user_agent,allow_redirects=False).content
        return(html)


# In[4]:


def crawl_link(url,pattern="(.*?)"):
        pages = list()
        html = open_url(url)
        BS = BeautifulSoup(html, "html.parser")
        for link in BS.findAll("a",href=re.compile(pattern)):
            if "href" in link.attrs:
                try:
                    file_link = link.attrs['href']
                    pages.append(file_link)
                except Exception as e:print(str(e))
        return(pages)


# In[5]:


data = crawl_link(url)


# In[6]:


def get_info(url,pattern="(.*?)"):
        info_dict,lists = dict(),list()
        html = open_url(url)
        movie_name = None
        movie_description = None
        BS = BeautifulSoup(html, "html.parser")
        for link in BS.findAll("div", {"class": "tv_series_info"}):
            movie_name = link.findAll("div", {"class": "serial_name"})[0].text
            movie_description = link.findAll("div", {"class": "serial_desc"})[0].text
            data = link.findAll("div", {"class": "value"})
            for info in data:
                lists.append(re.sub("\n","",info.text))
        info_dict["movie_name"] = movie_name
        info_dict["movie_description"] = movie_description
        info_dict["casts"] = lists[0]
        info_dict["genres"] = lists[1]
        info_dict["run_time"] = lists[2]
        info_dict["views"] = lists[3]
        info_dict["rating"] = lists[4]
        info_dict["seasons"] = lists[5]
        return(info_dict)


# In[7]:


get_info("https://tvshows4mobile.com/Das-Boot/index.html")


# In[8]:


data


# In[9]:


import csv
list_data = []
csv_file = "Tvseries_Dataset.csv"
csv_columns = ['movie_name', 'movie_description', 'casts', 'genres', 'run_time', 'views', 'rating', 'seasons']


# In[10]:


for url in data:
    try:list_data.append(get_info(url))
    except Exception as e :print(e,url)

try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in list_data:
            writer.writerow(data)
except IOError:
    print("I/O error")


# In[ ]:




