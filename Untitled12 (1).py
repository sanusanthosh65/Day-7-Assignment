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


# # Assignment 3

# In[1]:


list1=[(1,2,3),[1,2],['a','hit','less']]
list2=[]
list2=[i for each in list1 for i in each]
print ("The expected list is:",list2)

