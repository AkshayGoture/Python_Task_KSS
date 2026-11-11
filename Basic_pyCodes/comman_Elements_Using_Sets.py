#Common Elements Using Sets: Given two lists:
 #Find:* Common elements.
      #* Elements present only in the first list.
      #* All unique elements from both lists.
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
set1 = set(list1)
set2 = set(list2)
common = set1 & set2
only_first = set1 - set2
unique = set1 | set2
print("Common elements:", common)
print("Elements only in first list:", only_first)
print("All unique elements:", unique)
