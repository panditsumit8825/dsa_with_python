n=int(input("Enter a number:"))
str1="FizzBuzz"
str2="Fizz"
str3="Buzz"
ans=[]
for i in range(1,n+1):
    if(i%3==0 and i%5==0):
        ans.append(str1)
    elif(i%3==0):
        ans.append(str2)
    elif(i%5==0):
        ans.append(str3)
    else:
        ans.append(str(i))
print(ans)
