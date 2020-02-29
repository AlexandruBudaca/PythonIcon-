
#1. WAP in python to input 4 numbers and find the largest
#2. WAP in python to input 5 numbers and find the largest
#3. WAP to enter a name of a person and his/her age and check if the age is below 18, then print you are not allowed in Pub.
#4.WAP to enter 3 float numbers and print its products.
#5.WAp to enter a number and divisor and check wheater the number is divisible by the divisor or not.



'''
1.
a = list(map(int, input("Enter 4 numbers, (no comma): ").split())) 
print("The largest number is: ", max(a))
index = a.index(max(a))
print("The index of the largest number is:", index)
'''

'''
2.
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
d = int(input("Enter a number: "))
e = int(input("Enter a number: "))
f = [a,b,c,d,e]
for x in f:
  if x == max(f):
    print("The largest number is: ", x)
'''

'''
3.
from termcolor import colored

a = input("Enter your name: ")
b = int(input("Enter your age: "))
if b > 18:
  print(colored("You are not allowed in Pub!!!" ,"red"))
'''


'''
4.
a = float(input("Enter a number: "))
a = "1. " + "£" + str('%.2f' %a) + " Nike Af1"
print(a)
b = float(input("Enter a number: "))
b = "2. " + "£" + str('%.2f' %b) + " AirMax90"
print(b)
c = float(input("Enter a number: "))
c = "3. " + "£" + str('%.2f' %c) + " AsicsGel 150"
print(c)
'''


'''
5.
a = int(input("Enter a number: "))
b= int(input("Enter a divisor: "))
c = a / b;
if a % b:
  print(c)
else:
  print("Your number is an exact multiple with your divider")
'''

