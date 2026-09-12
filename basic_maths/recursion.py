# # # # # # arr = [1,2,3]
# # # # # # for i in arr:
# # # # # #     i=i*2
# # # # # # print(arr)
# # # # # # print(i)

# # # # # # Printing name n times by using recursion
# # # # # # def rec_name(n):
# # # # # #     if (n>0):
# # # # # #         print("Sumit")
# # # # # #         rec_name(n-1)
# # # # # # rec_name(15)

# # # # # # Printing 1 to N
# # # # # def rec_num(i,n):
# # # # #     if(i>n):
# # # # #         return 
# # # # #     else:
# # # # #         print(i)
# # # # #         # i+=1
# # # # #         rec_num(i+1,n)
# # # # # rec_num(1,5)

# # # # # Printing n to 1
# # # # def rev_num(n,i):
# # # #     if(n<i):
# # # #         return
# # # #     else:
# # # #         print(n)
# # # #         rev_num(n-1,i)
# # # # rev_num(5,1)

# # # # Print sum of first n numbers
# # # def rec_sum(i,sum):
# # #     if(i<1):
# # #         print(sum)
# # #         return
# # #     else:
# # #         rec_sum(i-1,sum+i)
# # # rec_sum(10,0)

# # # factorial of n number
# # def rec_fact(n,fact):
# #     if(n<1):
# #         print(fact)
# #         return
# #     else:
# #         rec_fact(n-1,fact*n)
# # rec_fact(0,1)
   
# # Print reverse in array by using single pointer
# def reverse_array_recursive(arr, i=0):
#     n = len(arr)
    
#     # Base Case: Stop when the pointer reaches the middle
#     if i >= n - i - 1:
#         return
    
#     # Swap elements using the single index 'i'
#     arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
    
#     # Recursive call moving the single pointer forward
#     reverse_array_recursive(arr, i + 1)

# # Example Usage:
# my_list = [1, 2, 3, 4, 5]
# reverse_array_recursive(my_list)
# print(my_list) 

# check given string is palindrome or not
def rec_palindrome(i,str):
    n=len(str)
    if(i>=n//2):
        return True
    if(str[i] != str[n-i-1]):
        return False
    else:
        return rec_palindrome(i+1,str)
str="madam"
# rec_palindrome(0,str)
print(rec_palindrome(0,str))
print(rec_palindrome(0,"kakak"))