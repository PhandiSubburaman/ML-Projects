#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import json
import pandas as pd
import numpy as np
import string
import re
from fuzzywuzzy import fuzz


# In[2]:


df = pd.read_csv("WYOMING.csv")


# In[3]:


count=1


# In[4]:


lst1=[]
for i in df.itertuples():
    print(count)
    count+=1
    nmls = i.NMLSID
    officer_name_old = i.OfficerName
    b = requests.get("http://10.0.10.30:7070/nmls/api/v1/companyandbranch/indiudial/"+str(nmls)).json()
    try:
        branch = b[0]['branch']
        company = b[0]['company']
        web = b[0]['company']['companyWebsites']
        if branch != None:
            cmpy_nmls = b[0]['company']['companyNMLSID']
            branch_nmls = b[0]['branch']['branchNMLSID']
            first_name = b[0]['individual']['firstName']
            last_name = b[0]['individual']['lastName']
            name = first_name+' '+last_name
            if len(web) == 0:
                website = "NA"
            else:
                website = web[0]['website']
            lst1.append({"Officer_NMLS":nmls, "Company_nmls":cmpy_nmls, "Branch_nmls":branch_nmls, "Officer_name":name, "Company_website":website, "officer_name_old": officer_name_old})
        elif branch == None and company != None:
            cmpy_nmls = b[0]['company']['companyNMLSID']
            branch_nmls = "NA"
            first_name = b[0]['individual']['firstName']
            last_name = b[0]['individual']['lastName']
            name = first_name+' '+last_name
            if len(web) == 0:
                website = "NA"
            else:
                website = web[0]['website']
            lst1.append({"Officer_NMLS":nmls, "Company_nmls":cmpy_nmls, "Branch_nmls":branch_nmls, "Officer_name":name, "Company_website":website, "officer_name_old": officer_name_old})
    except:
        pass
            
            


# In[ ]:


lstt1 = pd.DataFrame(lst1)
lstt1.to_csv("WYOMING_website.csv", index=False)


# In[ ]:




