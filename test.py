# question no 2 part (a)
num =int(input("Enter num to check whater even or not : "))
def even(a):
    if a%2==0: 
     print("even number")
    else:
        print("no is not even")
even(num)
print()


# question no 2 part (a)
for i in range(1,6):
    print("*"*i)
print()


# question no 2 part (c)
num1 =int(input("enter 1st num : "))
num2 =int(input("enter 2nd num : "))
def even(a,b):
         print("addation = ",a+b)
         print("subtraction = ",a-b)
         print("muntilplaction = ",a*b)
         print("division = ",a/b)
         print("exponentiation= ",a**b)
         print("floor/ quotiont= ",a//b)
even(num1,num2)