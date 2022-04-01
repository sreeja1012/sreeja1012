PI = 3.14
r = float(input("Enter the radius of a circle:"))
area = PI * r * r
print("Area of a circle = %.2f" %area)


filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))

