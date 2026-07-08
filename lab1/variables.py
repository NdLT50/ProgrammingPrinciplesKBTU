x = 5
y = "John"
print(x)
print(y)
x = "Sally" # x is now of type str
print(x)

a, b, c = "Orange", "Banana", "Cherry"
print(a)
print(b)
print(c)

a = b="Orange" #now a and b are storing value "Orange"
print(a)
print(b)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc()


x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)


def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)


x = "awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)