

print("\n")
#-------<list: it is in order ,change able,and it has duplicate memenbers, use square braces>-------
list1=["apple","banana","mango","apple","orange"]
list1[0]="good"
print(list1)
print(type(list1))
print("\n")


#-------<tuple: it is in order ,unchange able,and it has duplicate memenbers, use small breces>-------
tuple1=("apple","banana","mango","apple","orange")
#tuple1[0]="good"  it is error
print(tuple1)
print(type(tuple1))
print("\n")


#-------<set: it is in unorder ,unchange able,and it has no duplicate memenbers, use carly breces>-------
set1={"apple","banana","mango","apple","orange"}
#set1[0]="good"  it is error
print(set1)
print(type(set1))
print("\n")


#-------<diction: it is in order ,change able,and it has no duplicate memenbers, use carly breces>-------
diction1 = {'Name':'sultan', 'Age':17, 'Height':'5.7 ft', 'Hobby':'coding'}
diction1["Name"]="mohsin"
print(diction1)
print(type(diction1))
print("\n")