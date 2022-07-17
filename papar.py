name=[]
marks=[]
grade=[]
roll=[]
last=[]
current=[]
N=int(input("Total Number of Students : "))
for i in range (1,N+1):
  n=input(f"Enter Name of Student {i} : ")
  ma=int(input(f"Enter Marks out of 1100 {i} : "))
  r=input(f"Enter roll no {i} : ")
  lc=input(f"Enter last class {i} : ")
  cc=input(f"Enter current {i} : ")
  name.append(n)
  marks.append(ma)
  roll.append(r)
  last.append(lc)
  current.append(cc)
  for m in marks:
   if(m>=900 and m<=1100):
        m=("A+")
   elif(m>=800 and m<900):
       m=("A")
   elif(m>=700 and m<800):
       m=("B")
   elif(m>=600 and m<700):
       m=("C")
   elif(m>=0 and m<600):
       m=("Fail")
   else:
     m=("invalid marks")
grade.append(m)
print("="*120)
print("\t\t\t*** Mix record of students***")
print("="*120)
print("\t Names\t\t Marks \t grade\t\t Roll no \tlast class \tcurrent class ")
print("="*120)
for a,b,c,d,e,f in zip(name,marks,grade,roll,last,current):
   print("\t",a,"\t  ",b,"  \t",c,"\t\t",d," \t\t",e,"\t\t",f)
print("="*120)
print()
print("**********maxmum marks of student************")
print("********* Maxmum marks is ",max(marks),"*******\n")