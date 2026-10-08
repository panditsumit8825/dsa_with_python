list=[1,2,4,5]
n=5
# flag=0
for i in range(1,n):
    for j in range(1,n-1):
        if list[j]==i:
            flag=1
            break
    if(flag==0):
        print(i)


# def missing_num(list,n):
#     flag=0
#     for i in range(1,n):
#         for j in range(1,n-1):
#             if(list[j]==i):
#                 flag=1
#                 break
#     if(flag==0):
#         return i

# list=[1,2,4,5]
# n=5
# # flag=0
# print(missing_num(list,n))