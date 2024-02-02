#!/usr/bin/env python
# coding: utf-8

# In[26]:


# The code idea comes from: https://www.codecademy.com/resources/blog/advanced-python-code-challenges/

# Find the difference between the strings

# Write a function in Python that accepts two string parameters. 
# The first parameter will be a string of characters, and the second parameter will be the same string of characters, 
# But they’ll be in a different order and have one extra character. The function should return that extra character.
# For example, if the first parameter is “eueiieo” and the second is “iieoedue,” then the function should return “d.”

string1 = "eueiieo" # Test string 1
string2 = "iieoedue" # Test string2 

def difference(string1, string2):
    set1 = set(string1) # Making sets so all characters are unique
    set2 = set(string2)
    extra_chars = list(set1.symmetric_difference(set2)) # Symmetric difference returns characters which are not present in all sets
    return extra_chars
    
print(difference(string1, string2))

