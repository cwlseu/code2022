#!/usr/bin/env python
# coding: utf-8

# dropout: 随机对某些元素进行置为零，然后对于所有元素进行归一化。

# In[2]:


import torch
import torch.nn as nn

m = nn.Dropout(p=0.2)
input = torch.randn(10, 5)
output = m(input)
print(input)
print(output)
diff = (input - output) > 0
print(diff)


# In[ ]:




