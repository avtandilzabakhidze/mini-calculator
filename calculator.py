"""
enter first number
enter + - / * 
enter second number

"""
x = int(input("Enter first number : "))
z = input("Enter + - / * : ^ ")
y = int(input("Enter second number : "))

if z == "+":
    print(x+y) 
elif z=="-":
    print(x-y) 
elif z=="*":
    print(x*y) 
elif z=="/":
    if y!=0:
        print(x/y) 

    
elif z=="^":
    print(x**y) 
else:
    print("this is false")    