#!/usr/bin/env python
# coding: utf-8
#1.What are the two values of the Boolean data type? How do you write them?
# In[ ]:


Ans:Basic two Boolean data type are, True and False


# In[1]:


a=True
b=False
print(a,type(a))
print(b,type(b))


# #2 What are the three different types of Boolean operators?

# In[ ]:


Three Different types of Boolean operators are,
and
or
not


# #3 Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean values for the operator and what it evaluate ).

# Table for and:
# True and True- True
# True and False- False
# False and True- False
# False and False- False
# 
# Table for or:
# True or True -True
# True or False - True
# False or True -True
# False or False -False
# 
# Truth table for not:
# True-False
# False-True
# 
# 
# 

# 4. What are the values of the following expressions?
# (5 > 4) and (3 == 5)
# not (5 > 4)
# (5 > 4) or (3 == 5)
# not ((5 > 4) or (3 == 5))
# (True and True) and (True == False)
# (not False) or (not True)
# 

# In[18]:


print((5>4)and(3==5))
print(not(5>4))
print((5>4)or(3==5))
print(not((5>4)or(3==5)))
print((True and True) and (True == False))
print((not False) or (not True))


# 5.What are the six comparison operators?

# In[ ]:


==,!=,>,<,>=,=<


# 6.How do you tell the difference between the equal to and assignment operators?Describe a condition and when you would use one.

# In[26]:


#= is the operator which is used to assign a value for a variable,== is a operator which is used to compare the value. 
a=7
if a==7:
    print(a==3)


# In[29]:


#7. Identify the three blocks in this code:
spam = 0
if spam == 10:
    print('eggs')
if spam > 5:
    print('bacon')
else:
    print('ham')
print('spam')
print('spam')


# 8.Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.

# In[47]:


def spam(a):
    if a ==1:
        print("Hello")
    elif a ==2:
        print("Howdy")
    else:
        print("Greetings!")
spam(1)
spam(2)
spam(7)


# 9.If your programme is stuck in an endless loop, what keys you’ll press?

# In[ ]:


CTRL+C


# 10.How can you tell the difference between break and continue?

# break: function break is used to move out of the loop.
# continue: Function continue is used to move to the  start of the loop.

# 11.In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?

# In[ ]:


range(10)-  tells the loop to Provides the value till 10 except 10
range(0, 10)-  tells the loop to provides the value starting from 0 till 9
range(0,10,1)- tells the loop to provide the value starting from 0 till 9 wit an increment of 1


# 12.Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

# In[62]:


for i in range(0,11):
    print(i)


# In[67]:


i = 0
while(i<=10):
    print(i)
    i += 1


# 13.If you had a function named bacon() inside a module named spam, how would you call it after importing spam?

# In[ ]:


spam.bacon()


# In[ ]:




