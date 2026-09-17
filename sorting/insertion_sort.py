def insertion_sort(list,n):
    for i in range(n):
        j=i
        while(j>0 and list[j-1]>list[j]):
            list[j-1],list[j]=list[j],list[j-1]
            j -=1
    return list
list=[]
n=int(input("Enter a number:"))
for i in range(n):
    nums=int(input(f"Enter number {i+1}:"))
    list.append(nums)
print(list)
print(insertion_sort(list,n))