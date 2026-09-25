def Slargest(arr,n):
    largest=arr[0]
    Slargest=-1
    for i in range(n):
        if(arr[i]>largest and arr[i]>Slargest):
            Slargest=largest
            largest=arr[i]
        elif(arr[i]<largest and arr[i]>Slargest):
            Slargest=arr[i]
    return Slargest

def Smallest(arr,n):
    Smallest=arr[0]
    Ssmallest=float('inf')
    for i in range(n):
        if(arr[i]<Smallest):
            Smallest=arr[i]
            Ssmallest=Smallest
        elif(arr[i]!=Smallest and arr[i]<Ssmallest):
            Ssmallest=arr[i]
    return Ssmallest


arr=[1,2,4,7,7,5]
n=len(arr)
print([Slargest(arr,n),Smallest(arr,n)])