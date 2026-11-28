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
# arr=[3,1,-2,-5,2,-4]
# n=len(arr)
# ans=[0]*n
# posIndex=0
# negIndex=1
# for i in range(n):
#     if(arr[i]<0):
#         ans[negIndex]=arr[i]
#         negIndex+=2
#     else:
#         ans[posIndex]=arr[i]
#         posIndex+=2
# print(ans)

# If number of positive or negative sign are not equal
def rearrangment_array(arr):
    pos=[]
    neg=[]
    n=len(arr)
    for i in range(n):
        if(arr[i]<0):
            neg.append(arr[i])
        else:
            pos.append(arr[i])
    # if pos==neg
    # for i in range(n//2):
    #     arr[2*i]=pos[i]
    #     arr[2*i+1]=neg[i]
    # # return arr
    # if pos>neg
    s=len(pos)
    t=len(neg)
    if(pos>neg):
        for i in range(t):
            arr[2*i]=pos[i]
            arr[2*i+1]=neg[i]
        index=2*t
        for i in range(t,s):
            arr[index]=pos[i]
            index+=1
        return arr
        # if neg>pos
    else:
        for i in range(s):
            arr[2*i]=pos[i]
            arr[2*i+1]=neg[i]
            index=2*s
            for i in range(s,t):
                arr[index]=neg[i]
                index+=1
        return arr
arr=[-1,2,3,4,-3,1]
print(rearrangment_array(arr))