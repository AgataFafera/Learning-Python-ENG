#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Declare a function taking a dictionary as an argument
def remove_duplicates(input_dict):
    unique_dict = {}  # Create an empty dictionary to store unique key-value pairs
    seen_values = set()  # Create an empty set to track seen values

    for key, value in input_dict.items():  # Iterate through key-value pairs in the input dictionary
        if value not in seen_values:  # Check if the value has not been seen before
            unique_dict[key] = value  # If not seen, add the key-value pair to the unique dictionary
            seen_values.add(value)  # Add the value to the set of seen values

    return unique_dict  # Return the new dictionary with unique key-value pairs

# Test data
employee_dict = {
    'John Doe': 'EMP001',
    'Alice Smith': 'EMP002',
    'Bob Johnson': 'EMP003',
    'Eva Davis': 'EMP004',
    'Michael Brown': 'EMP005',
    'Samantha White': 'EMP006',
    'David Miller': 'EMP007',
    'Olivia Wilson': 'EMP008',
    'Richard Lee': 'EMP009',
    'Emma Taylor': 'EMP010',
    'Michael Brown': 'EMP005',
    'John Doe': 'EMP001'
}

print(remove_duplicates(employee_dict))  # Call the function with the provided dictionary and print the result





