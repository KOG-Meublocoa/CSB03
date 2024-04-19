# bai 1
# i = int(input("Nhap so: "))

# print("Input: "+"", i,-"")
# if i % 2 == 0:
#     print("so chan")
# else: 
#     print("so le")


# bai 2
# try:
#     a = float(input("Enter your type of data: "))
#     b = int(a)
#     if b / a == 1:                                
#         print(a, "is an integer")                 
#     else: print(a, "is not an integer")            
# except ValueError:                                 
#     print(a, "is not an integer")


# bai 3
# a = input("Enter your type of data: ")
# try:
#     int(a)                           
#     print("'",a,"'", "is a digit")
# except ValueError:                    
#     print("'",a,"'", "is not a digit")

# bai 4
# try:
#     a = int(input("Enter an integer: "))
#     if a % 3 == 0 and a % 5 == 0:
#         print(a, "is divisible by 3 and 5")
#     elif a % 3 == 0 and a % 5 != 0: 
#         print(a, "is divisible by 3")
#     elif a % 3 != 0 and a % 5 == 0: 
#         print(a, "is divisible by 5")
#     else: print(a, "is not divisible by 3 or 5")
# except ValueError: print("Enter an integer, please.")

# bai 5
# print("Welcome to The Ultimate Sercurity System")
# name = input("Please enter your username: ")
# pw = input("Please enter your password: ")
# if name == "admin" and pw == "12345":
#     print("Welcome to The Ultimate Sercurity System")
#     print("Username: ", name)
#     print("Password: ", pw)
#     print("You are logged in, admin.")
# else: 
#     print("Welcome to The Ultimate Sercurity System")
#     print("Username: ", name)
#     print("Password: ", pw)
#     print("Wrong username or password.")

# bai 6
# try:
#     a = float(input("Enter triangle side 1: "))
#     b = float(input("Enter triangle side 2: "))
#     c = float(input("Enter triangle side 3: "))
#     if a + b > c: 
#         print("The 3 sides can form a triangle")
#     else: print("The 3 sides cannot form a triangle")
# except ValueError: print("Fuk you, enter all 3 sides with numbers, dipsht.")

# bai 7
# from turtle import *

# try:
#     a = float(input("Enter triangle side 1: "))
#     b = float(input("Enter triangle side 2: "))
#     c = float(input("Enter triangle side 3: "))
#     max_num = a
#     sides = [a, b, c]
#     if a + b > c: print("The 3 sides can form a triangle")   
#     else:                                                    
#         print("The 3 sides cannot form a triangle.")         
#         exit()                                               
#     for i in sides:                                      
#         if i > max_num: max_num = i                       
#     if pow(a, 2) + pow(b, 2) + pow(c, 2) - pow(max_num, 2) == pow(max_num, 2):
#         print("This is a Right Triangle!")                                
#     elif a == b == c:
#         print("This is an Equilateral Triangle!")
#         pen()
#         forward(a)
#         left(120)
#         forward(b)
#         left(120)
#         forward(c)
#         left(120)
#         mainloop()
#     else: print("This is just a normal triangle.")
# except ValueError: 
#     print("Please enter all numbers.")

# bai 8
# numbers = range(0, 21, 1)
# for i in numbers:
#     if i % 3 == 0: print(i)

# bai 9
# var = int(input("Enter your number: "))
# digits = len(str(var))

# print("So chu so cua so la: ",digits)