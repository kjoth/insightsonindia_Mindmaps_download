
# coding: utf-8

# In[32]:


from bs4 import BeautifulSoup as BS
import urllib.request as urllib2
import requests
import lxml
import re
import os


# In[33]:


path_to_store_images = '/home/karthik/Desktop/CSE/InsightsonIndia/'


# In[34]:


quote_page = 'http://www.insightsonindia.com/insights-mindmaps-on-important-current-issues-for-upsc-civil-services-exam/'
urlopen = requests.get(quote_page)
html = urlopen.content
soup = BS(html, "lxml")


# In[35]:


a = soup.find_all('div',attrs={'class':'entry themeform'})[0]


# In[36]:


b = a.findAll('a', attrs={'href':re.compile(r".*jpg")})


# In[37]:


#finding href links from variable b and stor it in images
images = [a['href'] for a in b]


# In[ ]:


# here we are spliting the href(Image URL) to 2 parts.
# 1) Year and Month ==> To create folder
# 2) image name ==> TO save the image

#Catching the exception in the exception variable so that we can verify the erros if any
exception = []

directory_exists = 0

for i in images:
    
    if len(re.findall('wp-content',i)) < 1:
        #printing the href, if any content has been missed
        print(i)
        
    #else trying to save the image
    else:
        try:
            #spliting the year and month to create folder
            #Year_Month = str(i[50:57]).replace('/','_')
            
            #Slice a string after a certain phrase
            sub_str = str(i).split('uploads', 1)[1]
            Year_Month = str(sub_str[1:8]).replace('/','_')
            
            
            #spliting the image name to save the image in that name
            Image_name = str(sub_str[9:])
            
            #Directory to store the images(yearandMonth e.g. 2017_11)
            directory = path_to_store_images +str(Year_Month)
            
            #Directory path for the image file
            directory_filename = directory + '/' + str(Image_name)
            
            #Checking the folder(Year and Month) already exists
            if os.path.exists(directory):
                #checking if folder  exists, check for the file exists or not
                if os.path.isfile(directory_filename)==True:
                    
                    pass
                else:
                    #if file not exists in the fodler create the file
                    
                    urllib2.urlretrieve(i,directory_filename)
                    
            else:
                #if directory not exists, create the directory
                os.makedirs(directory)
                
                #Then save the image
                urllib2.urlretrieve(i,directory_filename)
                
        except Exception as e:
            #Save the exception araised for furture analyis
            exception.append((i,e))
            #continue if any exception occured
            continue
    
    


# In[ ]:




