#!/usr/bin/env python
# coding: utf-8

# # Assignment 1

# In[38]:


port1={21: "FTP", 22:"SSH", 23: "telnet", 80: "http"}
print(port1)

port1 = {value:key for key, value in port1.items()}
print(port1)


# # Assignment 2

# In[41]:


Input =[(1,2), (3,4), (5,6),(4,5)] 
   
Output = [(x + y) for x, y in Input] 
  
print("The list of Input tuple is ") 
print(Input) 
  
print("\nOutput") 
print(Output)

