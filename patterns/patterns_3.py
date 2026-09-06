# def patterns3(n):
#     for i in range(1,n):
#         for j in range(1,i+1):
#             print(j,end=" ")
#         print()
# patterns3(6)

# def patterns5(n):
#     for i in range(n,0,-1):
#         for j in range(i):
#             print("*",end="")
#         print()
# patterns5(6)

# def patterns6(n):
#     for i in range(n,0,-1):
#         for j in range(1,i+1):
#             print(j,end="")
#         print()
# patterns6(6)

# def pattern(n):
#     for i in range(n+1):
#         print(" "*(n-i)+"*"*(2*i+1)+" "*(n-i))
# pattern(4)

def pattern(n):
    for i in range(n,0,-1):
        print(" "*(n-i),"*"*(i-1)," "*(n-i))
pattern(5)