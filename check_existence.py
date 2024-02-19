#!/usr/bin/env python
# coding: utf-8

# Write a function that checks whether a given key exists in a dictionary.

students_id = {
    "Smith": 123,
    "Johnson": 456,
    "Williams": 789,
    "Jones": 987,
    "Brown": 654,
    "Davis": 321,
    "Miller": 852,
    "Wilson": 159,
    "Moore": 753,
    "Taylor": 246,
    "Anderson": 468,
    "Thomas": 975,
    "Jackson": 321,
    "White": 654,
    "Harris": 987,
    "Martin": 852,
    "Thompson": 369,
    "Garcia": 741,
    "Martinez": 258,
    "Robinson": 147,
    "Clark": 963,
    "Rodriguez": 654,
    "Lewis": 321,
    "Lee": 987
}

check_surname = input("Type a surname you want to check: ")

def checking(my_dict, surname):
    if surname in my_dict.keys():
        print("The surname already exists!")
    else: 
        print("There's no such surname in the dictionary.")
              
checking(students_id, check_surname)


