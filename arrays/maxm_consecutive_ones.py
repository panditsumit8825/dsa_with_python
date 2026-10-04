# list=[1,1,0,1,1,1,1,1,1,1,0,1,1]
# maxi=0
# count=0
# n=len(list)
# for i in range(n):
#     if(list[i]==1):
#         count +=1
#         maxi=max(maxi,count)
#     else:
#         count=0
# print(maxi)

#  By using function
def max_cons_ones(list,n):
    count=0
    maxi=0
    for i in range(n):
        if(list[i]==1):
            count +=1
            maxi=max(maxi,count)
        else:
            count=0
    return maxi

list=[1,1,0,1,1,1,1,0,1,1,1,1,1,1]
n=len(list)
print(max_cons_ones(list,n))