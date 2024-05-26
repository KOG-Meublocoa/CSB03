# phan 1
# cau 1
# number = int(input("Nhap so : "))
# float= (number % 2 == 0) 
# if float: print(number, "la so chan.") 
# else: print(number, "la so le")

# cau 2
# import math

# def cal_area(radius):
#     area = math.pi * radius ** 2
#     return area


# radius_input = float(input("Nhap ban kinh hinh tron :"))
# dien_tich = cal_area(radius_input)
# print(f"Dien tich hinh tron la : {dien_tich}")

# cau 3
# text = "MIndX"
# reversed_text = text[::-1]
# print(reversed_text)

# cau 4
# def is_palindromed(str):

#    return str ==str[::-1]
# str = ("Nhap chu :")
# instr = is_palindromed(str)

# if instr:
# 	print("Yes")
# else:
# 	print("No")


# Phan 2
# cau 1
# def tinh_giai_thua(n):
#     giai_thua = 1
#     if n == 0 or n == 1:
#         return giai_thua
#     else:
#         for i in range(2, n + 1):
#             giai_thua *= i
#         return giai_thua

# n = int(input("Nhập số nguyên dương n = "))
# print(f"Giai thừa của {n} là {tinh_giai_thua(n)}")


# cau 2
# def sap_xep_tang_dan (list):
#     for i in range (len(list)):
#         for a in range( i + 1,len (list)):
#             if list[i] > list[a]:
#                 list[i],list[a] =list[a],list[i]
# lst = [12,56,90,-39,30]
# print(lst)
# sap_xep_tang_dan(lst)
# print(lst)

# cau 3
# def fibonacci(n):
#     f0 = 0
#     f1 = 1
#     fn = 1
#     if n < 0:
#         return -1
#     elif n == 0 or n == 1:
#         return n
#     else:
#         for i in range(2, n):
#             f0 = f1
#             f1 = fn
#             fn = f0 + f1
#         return fn

# print("Nhap so n: ")
# n = int(input())
# print(f"{n} so dau tien cau day  Fibonacci: ")
# a= ""
# for i in range(n):
#     a += str(fibonacci(i)) + ", "
# print(a)

# Phan 3
# cau 1
# def tinh_hieu_va_17(so):
#     hieu = so - 17
#     if hieu > 0:
#        return hieu * 2
#     else :
#         return abs(hieu)
# so_da_chon = 10
# ket_qua = tinh_hieu_va_17(so_da_chon)
# print(f"Hiệu của {so_da_chon} và 17 là: {ket_qua}")

# cau 2
# date = dt1 = (2024,12,5) 
# date = dt2 = (2024,12,28)
# A1 = 2024
# B1 = 12 
# d1 = 5
# d2 = 28

# cau 3
# def count_number_4(lst):
#     return lst.count(4)
# my_list = [1, 2, 3, 4, 4, 5, 4, 9, 10, 4, 6, 7]
# result = count_number_4(my_list)
# print(f"So luong so 4 trong danh anch la : {result}")

# cau 4
# def number(so):
#     return 

# cau 5
# def create_histogram(so):
#     return so.matplotlib
# character:()
# number = [2,4,6,1]