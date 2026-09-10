def pallindrome(n):
    dup=n
    rev=0
    # using this for the print negative reverse number
    # if(n<0):
    #     sign=-1
    # else:
    #     sign =1
    # n=abs(n)
    # dup=abs(n)
    while(n>0):
        digit=n%10
        n=n//10
        rev=(rev*10)+digit
        # use for the sign change from neg to postive
        # rev=rev*sign
    # return rev
    if(dup==rev):
        return "true"
    else:
        return "false"
num=int(input("Enter a number:"))
print(pallindrome(num))