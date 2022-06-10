
#USING IF CONDATION

name=input("\nEnter your Name : ")
roll=input("Enter Roll no : ")
uni=input("Enter Universty Name : ")
city=input("Enter City Name : ")

sub1 = input("\nEnter subject 1 name: ")
m1= float(input("Enter marks 0ut of 100 : "))
print()

sub2 = input("Enter subject 2 name: ")
m2 = float(input("Enter marks 0ut of 100 : "))
print()

sub3 = input("Enter subject 3 name: ")
m3 = float(input("Enter marks 0ut of 100 : "))
print()

sub4 = input("Enter subject 4 name: ")
m4 = float(input("Enter marks 0ut of 100 : "))
print()

sub5 = input("Enter subject 5 name: ")
m5 = float(input("Enter marks 0ut of 100 : "))

print("-"*70)
print("\t\t*** Grades card of student ***")
print("-"*70)
print(" Name : ",name,"\t\t\t Roll No : ",roll,"\n Universty Name: ",uni,"  \t City : ",city)

print("="*70)
print(" subjects \t\t Marks \t\t Grades")
print("="*70)

def grade(marks, sub, m) :
    if (marks >=90 and marks <=100):
       print(" ",sub +"\t\t\t" ,float(m) , " \t\t A+")
    if (marks>=80 and marks <90):
        print(" ",sub +"\t\t\t" ,float(m) , " \t\t A")
    if (marks>=70 and marks <80):
        print(" ",sub +"\t\t\t" ,float(m) , " \t\t B+")
    if (marks >=60 and marks <70):
        print(" ",sub +"\t\t\t" ,float(m) , " \t\t B")
    if (marks >=50 and marks <60):
        print(" ",sub +"\t\t\t" ,float(m) , " \t\t C")
    if (marks <50 and marks >=0):
        print (" ",sub +"\t\t\t" ,float(m) ,"\t\tYou are FAILED!")
grade(m1, sub1, m1)
grade(m2, sub2, m2)
grade(m3, sub3, m3 )
grade(m4, sub4, m4 )
grade(m5, sub5, m5 )
print("="*70)

#====================================================================================================#


#USING IF ELSE CONDATION FOR GRADING

name=input("\nEnter your Name : ")
roll=input("Enter Roll no : ")
uni=input("Enter University  Name : ")
city=input("Enter City Name : ")

sub1 = input("\nEnter subject 1 name: ")
m1= float(input("Enter marks 0ut of 100 : "))
print()

sub2 = input("Enter subject 2 name: ")
m2 = float(input("Enter marks 0ut of 100 : "))
print()

sub3 = input("Enter subject 3 name: ")
m3 = float(input("Enter marks 0ut of 100 : "))
print()

sub4 = input("Enter subject 4 name: ")
m4 = float(input("Enter marks 0ut of 100 : "))
print()

sub5 = input("Enter subject 5 name: ")
m5 = float(input("Enter marks 0ut of 100 : "))
print("\n","-"*70)
print("\t\t*** Grades card of student ***")
print("-"*70)
print(" Name : ",name,"\t\t Roll No : ",roll,"\n University  Name :",uni,"  \t City : ",city)

print("="*70)
print(" subjects \t\t Marks \t\t Grades")
print("="*70)

def grade(marks, sub, m) :
    if 100>=float(marks) >=90:
        print(" ",sub + "\t\t\t",float(m) ," \t\t A+")
    else :
        if 80<= float(marks) <90 :
           print(" ",sub +"\t\t\t" ,float(m) ," \t\t A")
        else :
            if  70<= float(marks) <80 :
               print(" ",sub +"\t\t\t" ,float(m) ,"\t\t B+")
            else :
                if 60<= float(marks) <70 :
                  print(" ",sub +"\t\t\t" ,float(m) , "\t\t B")
                else :
                    if 50<= float(marks) <60 :
                       print(" ",sub +"\t\t\t" ,float(m) , "\t\t C")
                    else :
                        if 50> float(marks) >=0:
                          print(" ",sub +"\t\t\t",float(m) , " \t\tsorry! you are Fail in this subject")
                        else :
                         print("invalid Marks")

grade(m1, sub1, m1)
grade(m2, sub2, m2)
grade(m3, sub3, m3 )
grade(m4, sub4, m4 )
grade(m5, sub5, m5 )
print("="*70)

#==============================================================================================#
#using if else if control structure

name=input("\nEnter your Name : ")
roll=input("Enter Roll no : ")
uni=input("Enter Universty Name : ")
city=input("Enter City Name : ")

sub1 = input("\nEnter subject 1 name: ")
m1= float(input("Enter marks 0ut of 100 : "))
print()

sub2 = input("Enter subject 2 name: ")
m2 = float(input("Enter marks 0ut of 100 : "))
print()

sub3 = input("Enter subject 3 name: ")
m3 = float(input("Enter marks 0ut of 100 : "))
print()

sub4 = input("Enter subject 4 name: ")
m4 = float(input("Enter marks 0ut of 100 : "))
print()

sub5 = input("Enter subject 5 name: ")
m5 = float(input("Enter marks 0ut of 100 : "))
print("\n","-"*70)
print("\t\t *** Grades card of student ***\n")
print("-"*70)

print(" Name : ",name,"\t\t Roll No : ",roll,"\n Universty Name: ",uni,"  \t City : ",city)

print("="*70)
print(" subjects \t\t Marks \t\t Grades")
print("="*70)

def grade(marks, sub, m) :
    if 100>=float(marks) >=90:
        print(" ",sub + "\t\t\t",float(m) ,"  \t\t A+")
    elif 80<= float(marks) <90 :
        print(" ",sub +"\t\t\t" ,float(m) ,"  \t\t A")
    elif 70<= float(marks) <80 :
        print(" ",sub +"\t\t\t" ,float(m) ,"  \t\t B+")
    elif 60<= float(marks) <70 :
        print(" ",sub +"\t\t\t" ,float(m) , "  \t\t B")
    elif 50<= float(marks) <60 :
        print(" ",sub +"\t\t\t" ,float(m) , "  \t\t C")
    elif 50> float(marks) >=0:
        print(" ",sub +"\t\t\t",float(m) , " \t\tsorry! you are Fail in this subject")
    else :
        print("invalid Marks")

grade(m1, sub1, m1)
grade(m2, sub2, m2)
grade(m3, sub3, m3 )
grade(m4, sub4, m4 )
grade(m5, sub5, m5 )
print("="*70)

#-----------------------------------**** THANKS A LOT ***--------------------------------------------#
