# BRUTE FORCE APPROACH
# arr=[2,2,3,3,1,2,2]
# n=len(arr)
# count=0
# for i in range(n):
#     for j in range(n):
#         if(arr[i]==arr[j]):
#             count=count+1
# if(count>n//2):
#     print(arr[i])

# BETTER SOLUTION
# def majority_element(arr):
#     mpp={}
#     for num in arr:
#         mpp[num]=mpp.get(num,0)+1
#     for key,count in mpp.items():
#         if(count>len(arr)//2):
#             return key
#     return -1
# arr=[2,2,3,3,1,2,2]
# print(majority_element(arr))

# OPTIMAL SOLUTION BY USING MOORE'S VOTTING ALGORITHM
def majority_element(arr):
    cnt=0
    ele=None
    # step 1 : find the candidate for the majority element
    for num in arr:
        if cnt==0:
            cnt=1
            ele=num
        elif num ==ele:
            cnt +=1
        else:
            cnt -=1
        #  step 2 : verify if the candidate occurs more than n/2 times
        cnt1=0
        for num in arr:
            if num == ele:
                cnt1 +=1
        if cnt1 > (len(arr)//2):
            return ele 
    return -1
arr=[7,7,5,7,5,1,5,7,5,5,7,7,5,5,5,5]
print(majority_element(arr))