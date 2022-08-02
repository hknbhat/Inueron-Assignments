#!/usr/bin/env python
# coding: utf-8
#1. In the below elements which of them are values or an expression? eg:- values can be integer or string and expressions will be mathematical operators.
* ,'hello',-87.8,- ,/ ,+	,6 

Ans:
Values:-87.8,6,'hello'
Expression's:*,+,/,-

#2What is the difference between string and variable?
Ans:
String: it is set of information or a set of characters that you want to store, either it might be numeric or character or a value. 
Variable: Variable is the key where you can store a srting, by entering the value of variable we shoud be able to fetch the string.Always Variable has to be a alphabetic. 
#3Describe three different data types.
Ans: 
Different types of data tytpes are:
1)INT: which is used to represent the data of whole number.
2)Float; its a type of data type which is used to  the floating point no or the decimal's.
3)Complex:its the data type where we have complex number#4What is an expression made up of? What do all expressions do?
Ans:
An expression is made up of different requisite, by which we can yeild certian values in return.
Expression are made up of values, operators. Interpreter evaluates the expression and yeild the results.
#5. This assignment statements, like spam = 10. What is the difference between an expression and a statement?
Ans:
Expression: Expression  is the set of values and functions which will be interpreted into an new value as result.
Ex: a=4*4
Statements: In case of statements its just an line by which we will not yeild any result 
Ex: b="this is the first line"
#6. After running the following code, what does the variable bacon contain?
bacon = 22
bacon + 1
Ans: Variable bacon contains the value as 23

# In[6]:


bacon = 22
bacon + 1

7. What should the values of the following two terms be?
'spam' + 'spamspam'
'spam' * 3
Ans: 'spamspamspam'

# In[7]:


'spam' + 'spamspam'
'spam' * 3


# In[8]:


'spam' + 'spamspam'


# In[9]:


'spam' * 3

8. Why is eggs a valid variable name while 100 is invalid?
Ans:
Always the variable we are providing it should be in Alphabetic, any integer value will not be accepted.
# In[ ]:


get_ipython().set_next_input('9. What three functions can be used to get the integer, floating-point number, or string version of a value');get_ipython().run_line_magic('pinfo', 'value')
Ans:
int()
float()
str()

10. Why does this expression cause an error? How can you fix it?
'I have eaten ' + 99 + ' burritos.'
Ans:
Since the  statement contains the both alpha and num we cannot merge both. we need to typecast the int vale to string and we are able to fix the issue
# In[11]:


'I have eaten ' + str(99) + ' burritos.'


# In[ ]:




