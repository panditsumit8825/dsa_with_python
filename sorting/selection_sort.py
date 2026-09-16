def selection_sort(list,n):
    for i in range(n-1):
        min_idx=i
        for j in range(i+1,n):
            if(list[j]<list[min_idx]):
                min_idx=j
        list[min_idx],list[i]=list[i],list[min_idx]
    return list
        

list=[]
n=int(input("Enter a number :"))
for i in range(n):
    num=int(input(f"Enter number {i+1} :"))
    list.append(num)
print(list)
print("Sorted list is :" , selection_sort(list,n))