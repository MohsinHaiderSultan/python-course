num=int(input("enter a number: "))
if num >1:
  for i in range(2,int(num/2)+1):
   if num % i == 0:
         print(num ,"is not prime ")
         break
  else:
         print(num,"is prime")
         
else:
    print(num,"not prime")
   
#fectriol
num=int(input("enter a number: "))
fac=1
for i in range(1,num+1):
    fac=fac*i
print("the fectrioal of number ",num,"! =",fac)