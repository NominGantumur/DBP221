#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
x = np.arange(0,10)
y = x*2
z = x**2
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# 1 Өгөгдлийг ашиглан дараах графикийг байгуул.
plt.plot(x, 2*x + 0, linestyle = '-', color = 'blue')
plt.title('Граф1')
plt.xlabel('x')
plt.ylabel('y')
plt.show()


# In[3]:


#2 Өмнө байгуулсан графикийг дараах шиг болго.
plt.plot(x, 2*x + 0, linestyle = '-', color = 'orange')
a = plt.axes([0.25, 0.5, .2, .2])
plt.plot(x, 2*x + 0, linestyle = '-', color = 'blue')
plt.show()


# In[4]:


#3 Өгөгдлийг ашиглан дараах графикийг байгуул
plt.subplot(221)
plt.plot(x, 2*x + 0, linestyle = '--', color = 'blue')
plt.subplot(222)
plt.plot(x, x**2 + 0, linestyle = '-', color = 'red')
plt.show()


# In[5]:


# 4 Өгөгдлийг ашиглан дараах графикийг байгуул.
plt.subplot(221)
plt.plot(x, 2*x + 0, linestyle = '--', color = 'blue')
plt.subplot(222)
plt.plot(x, x**2 + 0, linestyle = '-', color = 'red')
plt.subplot(223)
plt.plot(x, 2*x + 0, linestyle = '--', color = 'blue')
plt.subplot(224)
plt.plot(x, x**2 + 0, linestyle = '-', color = 'red')
plt.show()


# In[ ]:




