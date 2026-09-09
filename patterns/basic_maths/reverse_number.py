# def reverse_num(n):
#     revN=0
#     while(n>0):
#         lastdigit=n%10
#         n=n//10
#         revN=(revN*10)+lastdigit
#     return revN
# num=int(input("Enter a number :"))
# print(reverse_num(num))

def reverse_num(n):
    revN=0
    while(n!=0):
        lastdigit=n%10
        n=n//10
        revN=(revN*10)+lastdigit
    return revN
num=int(input("Enter a number :"))
print(reverse_num(num))