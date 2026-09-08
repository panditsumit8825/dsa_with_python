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

# def pattern7(n):
#     for i in range(n+1):
#         print(" "*(n-i)+"*"*(2*i+1)+" "*(n-i))
# pattern7(4)

# def pattern8(n):
#     for i in range(n):
#         print(" "*i,end="")
#         print("*"*(9-2*i))
# pattern8(5)

# def pattern9(n):
#     for i in range(n):
#         print(" "*(n-(i+1))+"*"*(2*i+1))
#     for j in range(n):
#         print(" "*j+"*"*(n-2*j+2)+" "*j)
# pattern9(3)

# def patterns10(n):
#     dooo
# def patterns11(n)
#     dooo
# def pattern12(n):
#     for i in range(1,n+1):
#         for j in range(1,i):
#             print(j,end="")
#         for k in range(2*(n-i)):
#             print(" ",end="")
#         for p in range(i-1,0,-1):
#             print(p,end="")
#         print()
# pattern12(5)

def pattern13(n):
    for i in range(n):
        print(i)
pattern13(5)