# def counts(n):
#     if(n==0):
#         return 1
#     cnt=0
#     while(n>0):
#        digit=n%10
#        cnt=cnt+1
#        n=n//10
#     return(cnt)
# num=int(input("Enter the digit: "))
# print(counts(num))
# Second method
import math
def count(n):
    if(n==0):
        return 1
    return int(math.log10(abs(n))) +1
print(count(15010000))
