# leetcode 350 problem by brute force approach
nums1=[4,9,5]
nums2=[9,4,9,8,4]
n1=len(nums1)
n2=len(nums2)
visit=[0]*n2
ans=[]
for i in range(n1):
    for j in range(n2):
        if(nums1[i]==nums2[j] and visit[j]==0):
            ans.append(nums2[j])
            visit[j]=1
            break
        if(i>n1 and j>n2):
            break
print(ans)