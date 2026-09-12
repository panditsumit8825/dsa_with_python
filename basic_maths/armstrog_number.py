def armstrong(n):
    dup=n
    sum=0
    while(n>0):
        digit=n%10
        sum=sum+(digit*digit*digit)
        n=n//10
    if(dup==sum):
        return "The number is Armstrong number"
    else:
        return "The number is Not a Armstrong number"
num=int(input("Enter a number:"))
print(armstrong(num))
