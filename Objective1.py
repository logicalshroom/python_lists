# 1. Python List Transformation
# Objective: The aim of this assignment is to practice list operations and transformations.
# 
# Problem Statement: You've been given a list of grades from an exam. You need to process and analyze these grades.

# Task 1: Given the list of grades below, sort the grades in descending order, and print the sorted list.

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

print(grades.sort())

# Task 2: Calculate Average

grades_avg = sum(grades)/len(grades) #Add up all the grades, divide by the number of grades

print(grades_avg)