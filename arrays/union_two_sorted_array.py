# # ---------------M-1----------------

# # for using in built union function first we need to declare in a set 
# # because set contain a unique element
# # union of two sorted array bu using union function
# # set_a={1,1,2,3,4,5}
# # set_b={2,3,4,4,5}
# # array_union=set_a.union(set_b)
# # print(array_union)

# # ---------------M-2----------------
# # by using brute force approach using set function
# # arr1=[1,1,2,3,4,5]
# # arr2=[2,3,4,4,5]
# # n1=len(arr1)
# # n2=len(arr2)
# # # this is way to declare empty set or set in python 
# # new_set=set()
# # for i in range(n1):
# #     new_set.add(arr1[i])
# # for i in range(n2):
# #     new_set.add(arr2[i])
# # union=[]
# # for item in new_set:
# #     union.append(item)
# # print(union)


# # ---------------M-3----------------
# # Optimal approach by using two pointer concept
arr1 = [1, 1, 2, 3, 4, 5, 6, 7, 9]
arr2 = [2, 3, 4, 4, 5, 6, 7]

n1 = len(arr1)
n2 = len(arr2)

i = 0
j = 0
union_array = []

while i < n1 and j < n2:
    if arr1[i] <= arr2[j]:
        if len(union_array) == 0 or union_array[-1] != arr1[i]:
            union_array.append(arr1[i])
        i += 1
    else:
        if len(union_array) == 0 or union_array[-1] != arr2[j]:
            union_array.append(arr2[j])
        j += 1
while i < n1:
    if len(union_array) == 0 or union_array[-1] != arr1[i]:
        union_array.append(arr1[i])
    i += 1
while j < n2:
    if len(union_array) == 0 or union_array[-1] != arr2[j]:
        union_array.append(arr2[j])
    j += 1

print("the sorted array :" , union_array)


