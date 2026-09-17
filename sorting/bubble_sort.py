def bubble_sort(list,n):
    for i in range(n-1,0,-1):
        did_swap=0
        for j in range(i):
            if(list[j]>list[j+1]):
                list[j],list[j+1]=list[j+1],list[j]
                did_swap=1
                if(did_swap==0):
                    break
                # print("How many time loops runs")
    return list
list=[]
n=int(input("Enter a number:"))
for i in range(n):
    nums=int(input(f"Enter number {i+1}:"))
    list.append(nums)
print(list)
print(bubble_sort(list,n))