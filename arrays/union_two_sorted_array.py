# for using in built union function first we need to declare in a set 
# because set contain a unique element
# union of two sorted array bu using union function
# set_a={1,1,2,3,4,5}
# set_b={2,3,4,4,5}
# array_union=set_a.union(set_b)
# print(array_union)

# ---------------M-2----------------
# by using brute force approach using set function
arr1=[1,1,2,3,4,5]
arr2=[2,3,4,4,5]
n1=len(arr1)
n2=len(arr2)
# this is way to declare empty set or set in python 
new_set=set()
for i in range(n1):
    new_set.add(arr1[i])
for i in range(n2):
    new_set.add(arr2[i])
union=[]
for item in new_set:
    union.append(item)
print(union)