# # # # arr = [1,2,3]
# # # # for i in arr:
# # # #     i=i*2
# # # # print(arr)
# # # # print(i)

# # # # Printing name n times by using recursion
# # # # def rec_name(n):
# # # #     if (n>0):
# # # #         print("Sumit")
# # # #         rec_name(n-1)
# # # # rec_name(15)

# # # # Printing 1 to N
# # # def rec_num(i,n):
# # #     if(i>n):
# # #         return 
# # #     else:
# # #         print(i)
# # #         # i+=1
# # #         rec_num(i+1,n)
# # # rec_num(1,5)

# # # Printing n to 1
# # def rev_num(n,i):
# #     if(n<i):
# #         return
# #     else:
# #         print(n)
# #         rev_num(n-1,i)
# # rev_num(5,1)

# # Print sum of first n numbers
# def rec_sum(i,sum):
#     if(i<1):
#         print(sum)
#         return
#     else:
#         rec_sum(i-1,sum+i)
# rec_sum(10,0)

# factorial of n number
def rec_fact(n,fact):
    if(n<1):
        print(fact)
        return
    else:
        rec_fact(n-1,fact*n)
rec_fact(0,1)
   

