# a = int(input("Nhap so "))

# if a > 0:
#     print("a la so duong")
# elif a < 0:
#     print("a la so am")
# else:
#     print("a = o") 


# a = int(input("Nhap so"))

# if a % 2 == 0:
#     print(" a la so chan")
# else: 
#      print("a la so le")
    

# i = 1
# while i < 6:
#   print(i)
#   i += 1

# i = 1
# n = 0
# while i <= 99:
#       n += i
#       i += 1
# print(i)

# a = range(1,20,1)
# for n in a:
#     print(n)

# for i in range(0,20,1):
#     i += 1
#     print(i)

# 1. Viết chương trình tìm số lớn hơn trong 3 số nhập từ người dùng
# a = float(input("Nhap so  "))
# b = float(input("Nhap so  "))
# c = float(input("Nhap so  "))
# max_numbers= a
# numbers =[a,b,c]

# for i in numbers:
#     if i > max_numbers:
#          max_numbers = i
# print(max_numbers)

# 2. Viết chương trình xác định một năm có phải năm nhuận không 
# (Năm nhuận là năm chia hết cho 4. Trong trường hợp năm chia hết cho 100 thì phải chia hết cho 400)
# a = int(input("nhap nam "))

# if a % 4 == 0:
#     print(" a La nam nhuan")
# elif  a % 100 % 400 == 0:
#     print(" a La nam nhuan")
# else:
#     print("a khong phai nam nhuan")

# 3. Dùng vòng lặp in ra các dãy số sau (mỗi dãy số là 1 vòng lặp):
    #  - 0 1 2 3 4 5 6
    #  - 100 101 102 103 104 105
    #  - 9 8 7 6 5 4 3 2


# for i in range(7):
#     print(i, end=" ")
# print("\n")

# for i in range(100, 106):
#     print(i, end=" ")
# print("\n")

# for i in range(9, 1, -1):
#     print(i, end=" ")
# print("\n")


# 4. In ra các  số chia hết cho 3 từ 0 đến 20, mỗi số một dòng

for i in range(21):
    if i % 3 == 0:
        print(i,end=" ")
print("\n")



# 5. Tính số chữ số của một số nguyên do người dùng nhập vào
        # len(str(abs(number)))