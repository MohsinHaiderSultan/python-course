from pickletools import int4


num=int(input("Enter num of rows: "))
for i in range(num):
   for j in range(i+1):
       print("",end=" ")
   for j in range(i+1,num+1):
       print("*",end=" ")
   print()
for i in range(num):
   for j in range(i):
       print("",end=" ")
   for j in range(i-8
                91,num+1):
       print("*",end=" ")
   print()