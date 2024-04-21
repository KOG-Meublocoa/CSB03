# Phần 1
# bài 1
# Firstname = input("Firstname :")
# Lastname = input("Lastname :")
# print("Your registered name is : ", Firstname, Lastname,".")

# bài 2
# print("mindX".upper())

# bài 3
# number = float(input("Nhập một số: "))
# square = number ** 2
# print(f"Bình phương của {number} là {square}")

# bài 4
# from turtle import *
# cricle(100)
# mainloop()


# Phần 2
# bài 1
# for i in range(3 , 13):
#     print (i)

# bài 2
# n = int(input("Nhập số n : "))
# for i in range (n + 1):
#     print(i ,end = "")

# bài 3
# def print_odd_numbers(n):
#     for i in range(n + 1):
#         if i % 2 != 0:
#             print(i)


# n = int(input("Nhập số  n: "))
# print("Các số lẻ từ 0 đến", n, "là:")
# print_odd_numbers(n)

# bài 4
# from turtle import *
# forward(50)
# left(40)
# forward(50)
# left(50)
# forward(50)
# left(40)
# forward(50)
# left(50)
# forward(50)
# left(40)
# forward(50)
# left(50)
# forward(50)
# left(40)
# forward(50)
# pencolor("green")
# mainloop()

# Phần 3
# bài 1
# i = int(input("Nhập số :"))
# if i > 13:
#     print(f"Số {i} lớn hơn 13.")
# else:
#     print(f"Số {i} không lớn hơn 13.")

# bài 2
# i  = int(input("Nhập số :"))
# if i % 2:
#     print(f"số {i} là số lẻ")
# else:
#     print(f"số {i} là số chẵn")

# bài 3
# def main():
#     try:
#        thang = int(input("Nhập tháng :"))
#        nam = int(input("Nhập năm"))
#        if thang in [1,3,5,78,10,12]:    
#          print(" {thang}/{nam} là tháng có 31 ngày.")
#        elif thang in [4,6,9,11]:
#          print(" {thang}/{nam} là tháng có 30 ngày.")
#        else:
#         if (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0):
#                     print(f"Tháng {thang}/{nam} có 29 ngày (năm nhuận).")
#         else:
#                     print(f"Tháng {thang}/{nam} có 28 ngày.")
   

#     except ValueError:
#         print("Vui lòng nhập số nguyên cho tháng và năm.")

# if __name__ == "__main__":
#     main()

# phần 4
# bài 1,2,3

username = input("username :")
email = input("Eamil :")
password = input('Mật khẩu :')
password2 =input('Nhập lại mật khẩu :')
def password(password, password2):
    if password == password2:
        print("Mật khẩu hợp lệ.")
    else:
        print("Mật khẩu không khớp. Vui lòng nhập lại.")
