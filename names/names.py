import time
import collections

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

# same logic but list comprehension for time baseline:
# duplicates = [i for i in names_1 for j in names_2 if i == j] # 1.63 seconds

# Python has a built-in .difference() method on sets, so convert lists to sets and then back:
# x = set(names_1)
# y = set(names_2)
# z = x.difference(y) # returns elements in x but not in y (i.e. elements only in x)
# q = x.difference(z) # returns elements in x but not in z, e.g. elements in x and in y (duplicates)
# duplicates = [i for i in q] #.0050 seconds

# same logic as above, but list comprehension instead of variable assignment:

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

# See above -- using set comparisons, which are built-in, resulted in ~ 99.7% reduction in runtime.