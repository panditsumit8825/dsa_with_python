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

# def pattern13(n):
#     num=1
#     for i in range(1,n+1):
#         # print(i)
#         for j in range(1,i+1):
#             print(num,end=" ")
#             num = num + 1
#         print()
# pattern13(5)
 
# def pattern14(n):
#        for i in range(1,n+1):
#         for j in range(i):
#             print(chr(65+j),end=" ")
#         print()
# pattern14(5)

# def pattern15(n):
#     for i in range(n,0,-1):
#         for j in range(i):
#             print(chr(65+j),end=" ")
#         print()
# pattern15(5)

# def pattern16(n):
#     for i in range(n):
#         for j in range(i+1):
#             print(chr(65+i),end=" ")
#         print()
# pattern16(5)

# def pattern17(n):
#     for i in range(1,n):
#         print(" "*(n-i),end="")
#         for j in range(i):
#             print(chr(65+j),end="")
#         for j in range(i-2,-1,-1):
#             print(chr(65+j),end="")
#         print()
# pattern17(5)

# def pattern18(n):
#     for i in range(n):
#         start_ascii=ord('A') + n-1-i
#         for j in range(i+1):
#             print(chr(start_ascii+j),end=" ")
#         print()
# pattern18(5)

# def pattern19(n):
#     for i in range(1,n+1):
#         for j in range(n):
#             print("*"*(n-j)+" "*2*j+"*"*(n-j))
#         for j in range(1,i+1):
#             print("*"*j+" "*(2*n-2*j)+"*"*j)
#         print()
# pattern19(5)

# def pattern20(n):
#     for i in range(1,n+1):
#         print("*"*i+" "*(2*n-2*i)+"*"*i)
#     # lower half reverse of upper logic
#     for j in range(n,0,-1):
#             print("*"*j+" "*(2*n-2*j)+"*"*j)
#     print()
        
# pattern20(5)

# def pattern21(n):
#     for i in range(n):
#         for j in range(n):
#             if(i==0 or i==n-1 or j==0 or j==n-1):
#                 print("*",end="")
#             else:
#                 print(" ",end="")
#         print()
# pattern21(5)

def pattern22(n):
    size=2*n-1
    for i in range(size):
        for j in range(size):
            val=n-min(i,j,size-i-1,size-j-1)
            print(val,end=" ")
        print()
pattern22(4)


