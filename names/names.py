import time
import collections

import sys
sys.path.append('C:\\Users\\mgroe\\Desktop\\lambdaGit\\DS\\week 2\\Sprint-Challenge--Data-Structures-Python\\names')

from sorting_tree import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1) 
# Baseline time: 4.0 seconds

# same logic but list comprehension:
# duplicates = [i for i in names_1 for j in names_2 if i == j] # 1.63 seconds

# remove if/if syntax, but still in logic:
# for name in names_1:
#     if name in names_2:
#         duplicates.append(name)

# Use a binary search tree
# Checks to see if each name is already in.

# name_tree = BSTNode()

# for n in names_1:
#     if not name_tree.contains(n):
#         name_tree.insert(n)

# for m in names_2:
#     if name_tree.contains(m):
#         if m not in duplicates:
#             duplicates.append(m)
#     else:
#         name_tree.insert(m)
# # 0.76 seconds, O(log n) time average

# # Stretch version:
x = set(names_1)
y = set(names_2)
z = x.difference(y) # returns elements in x but not in y (i.e. elements only in x)
q = x.difference(z) # returns elements in x but not in z, e.g. elements in x and in y (duplicates)
duplicates = [i for i in q] #.0050 seconds
duplicates = [i for i in set(names_1).difference(set(names_1).difference(set(names_2)))] #.0050 seconds

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

# See above -- using set comparisons, which are built-in, resulted in ~ 99.7% reduction in runtime.