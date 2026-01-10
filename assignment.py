#print message
print("python programming")  
# sum of digits
 a=input("enter first number:")
b=input("enter second number:")
total=int(a)+int(b)
print("total=",total)
#number is odd or even
x=input("enter one value")
if x%2==0:
 print("no. is even")
else:
 print("no. is odd")
 #leap year or not
 
 year=2025
 if year%4==0:
  if year %100==400:
  print(year,"is leap year")
  else
  print(year,"not leap year")

 #pi value
pi=3.1416
print(pi)
#constant value
PI = 3.14159
print("The constant value is:", PI)

#square of number
num = int(input("Enter a number: "))

square = num ** 2

print(f"The square of {num} is {square}")

#area of circle
radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2
print(f"The area of the circle is {area:.2f}")

#check datatype
a = 10
b = 3.14
c = "Hello"
d = True
e = [1, 2, 3]

# Check and print data types
print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'str'>
print(type(d))  # <class 'bool'>
print(type(e))  # <class 'list'>

#math function
result=math.pow(2,3)
print(result)

#positive or negative no.
num = float(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")



