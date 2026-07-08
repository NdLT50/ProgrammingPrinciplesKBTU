 #Strings in python are surrounded by either single quotation marks, or double quotation marks.
print("Hello")
print('Hello')

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

a = "Hello"
print(a)


a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

a = "Hello, World!"
print(a[1])

for x in "banana":
    print(x,end=' ')
print('\n')


#The len() function returns the length of a string:
a = "Hello, World!"
print(len(a))

txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")


#SLICING
b = "Hello, World!"
print(b[2:5])


b = "Hello, World!"
print(b[:5])


b = "Hello, World!"
print(b[2:])


b = "Hello, World!"
print(b[-5:-2])


#modify strings 
a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())


#The strip() method removes any whitespace from the beginning or the end:
a = "    Hello, World!    "
print(a.strip()) # returns "Hello, World!"

a = "Hello, World!"
print(a.replace("H", "J"))

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']