
# coding: utf-8

# # Date 11th Aug 2018: Session 1 - Assignment 1

# In[8]:


# Question 1 - My First Program
print("This is my first Program")


# In[21]:


#Question 2
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). 
# The numbers obtained should be printed in a comma-separated sequence on a single line

list1=list(range(2000,3201))
list2=[]
#print(list1)
for val in list1:
    if val%7==0 and val%5!=0:
        list2.append(val)
print("list2=", list2)
        


# In[6]:


#Question 3
#Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order 
#with a space between first name and last name

FLname=str(input("Enter your First Name and Last Name:"))
print("The reverse order of FLname is:", FLname[::-1])


# In[7]:


#Qustion 4
#Write a Python program to find the volume of a sphere with diameter 12 cm.
# Formula: V=4/3 * π * r 3
import math
d=int(input("Enter the value of diameter:"))
r=(d/2)
print("The radius of the sphere is=",r,"cm")
print("The volume of the sphere is=", ((4/3)*math.pi*(r**3)),"cm3")

