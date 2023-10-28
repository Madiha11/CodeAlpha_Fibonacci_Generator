#!/usr/bin/env python
# coding: utf-8

# In[9]:


def fibonacci_generator(range):
    fibonacci_list = [0,1]
    while len(fibonacci_list)<range:
        next_number = fibonacci_list[-1] + fibonacci_list[-2]
        fibonacci_list.append(next_number)
    return fibonacci_list
range = int(input())
print(fibonacci_generator(range))


# In[ ]:




