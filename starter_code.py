#!/usr/bin/env python
# coding: utf-8

# ## Python Control Structures Assignment
# 
# # Instructions
# Welcome to the Python Control Structures Assignment! In this assignment, you will work through a series of exercises to test your understanding of Python control structures like `while`, `for`, and `if` statements, including the use of `break` and `continue` statements. Your task is to implement the provided starter code and ensure your solutions meet the requirements.
# 
# ### Part 1: Looping Constructs
# 
# #### Task 1: `while` loop
# - Write a `while` loop that prints all the even numbers from 0 to 20.
# - If the number reaches 16, break out of the loop.

# In[2]:


# Task 1: while loop
def while_loop():
    number = 0
    while number <= 20:
        if number % 2 == 0:
            print(number)
        if number == 16:
            break
        number += 1


# #### Task 2: `for` loop with `continue`
# - Write a `for` loop that iterates through numbers from 1 to 15.
# - If the number is divisible by 3, skip printing it using the `continue` statement.
# 

# In[2]:


# Task 2: for loop with continue
def for_loop_continue():
    for num in range(1, 16):
        if num % 3 == 0:
            continue
        print(num)

# #### Task 3: `if-else` statement
# - Write an `if-else` statement that checks if a given number is positive, negative, or zero.
# - Print an appropriate message for each case.

# In[3]:


# Task 3: if-else statement
def number_classification():
    number = int(input("Enter a number: "))
    if number > 0:
        print("positive")
    elif number < 0:
        print("negative")
    else:
        print("zero")


# #### Task 4: Nested loops
# - Write a program that uses nested loops to print a multiplication table for numbers 1 through 5.
# 

# In[1]:


# Task 4: Nested loops
def multiplication_table():
    for i in range(1, 6):
        for j in range(1, 6):
            print(f"{i} x {j} = {i * j}")


# 
