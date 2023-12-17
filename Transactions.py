#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Bank:

    def __init__(self):
        self.bal=0
        
    def display(self,bal):
        print('Your current Balance: ',self.bal)
        
    def deposit(self,dep):
        self.bal+=dep
        print('Your current balance: ',self.bal)
    
    def withdraw(self,wd):
        self.bal-=wd
        print('Your current balance: ',self.bal)
        
        






