x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
print(x+" "+y+" "+z) #same output as 4th line

a=5
b=10
print(a+b) #output:15

num = 5
string = "John"
print(num , string) 
try:
    num = 5
    string = "John"
    print(num + string)  # This will raise a TypeError
except TypeError:
    print("Error: Cannot add a number and a string.")

