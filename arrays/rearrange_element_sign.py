# Brute Force Approach to rearrange array element by sign value 

# arr=[3,1,-2,-5,2,-4]
# pos=[]
# neg=[]
# n=len(arr)
# for i in range(n):
#     if(arr[i]>0):
#         pos.append(arr[i])
#     else:
#         neg.append(arr[i])
# # print(pos)
# # print(neg)
# for i in range(n//2):
#     arr[2*i]=pos[i]
#     arr[2*i+1]=neg[i]
# print(arr)


# Optimal solution 
arr=[3,1,-2,-5,2,-4]
n=len(arr)
ans=[0]*n
posIndex=0
negIndex=1
for i in range(n):
    if(arr[i]<0):
        ans[negIndex]=arr[i]
        negIndex+=2
    else:
        ans[posIndex]=arr[i]
        posIndex+=2
print(ans)