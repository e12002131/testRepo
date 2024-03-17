#!/usr/bin/env python
# coding: utf-8

# In[6]:


import time
from datetime import datetime
import sys

while True:
    print(datetime.now(), flush=True, end="")
    print('\r', flush=True, end="")
    time.sleep(0.015)


# In[ ]:




