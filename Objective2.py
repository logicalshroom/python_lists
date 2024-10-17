# Advanced List Methods 

# Given the two lists of student names, find out if Alice submitted their assignment AND attended class

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

if "Alice" in submitted and "Alice" in attended:
    print(f"Alice went to class and completed their assignment!")
else:
    print(f"Alice either didn't go to class or didn't submit their assignment.")