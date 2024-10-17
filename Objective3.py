# Advanced Slicing Techniques

# Problem Statement: You have a list of daily temperatures for one month, and you'd like to extract specific data from it.

# Task 1

# Given the following list of temps, extract the temps between index 7 and 14.

# Expected outcome: 83, 85, 86, 87, 88, 89, 90,

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

print(temperatures[7:14]) # We can easily solve this using Indexing.

# Task 2 : Extract all the temperatures above 100. HINT: add the temperatures over 100 to a new list, or use list slicing to get the temperatures.

# I mean, the list is already in order, so this is really easy.

# We could make a MORE complicated function that iterated every index in "temperatures", checking to see if the value is over 100 or not, and then adding the result to a new list. But, why do all that when we can just slice the last 7 numbers in the list?

print(temperatures[-7:])