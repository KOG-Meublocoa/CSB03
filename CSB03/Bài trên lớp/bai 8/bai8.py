# import example_module


# a = float(input("Nhap so thu nhat: "))
# b = float(input("Nhap so thu hai: "))

# example_module.sum(a, b)


# 1. Viết Function tìm số lớn hơn trong 2 số 
# 2. Định nghĩa hàm có thể chấp nhận input là số nguyên và in "Đây là một số chẵn" nếu nó chẵn và in "Đây là một số lẻ" nếu là số lẻ.
# 3. Viết function kiểm tra năm đó có phải năm nhuận hay không 
# 4. Viết function tính tổng một array nhập từ bàn phím. Nếu trong array tồn tại phần tử không phải là số, thì bỏ qua phần tử đó 
# 5. Viết một chương trình chấp nhận chuỗi từ do người dùng nhập vào, phân tách nhau bởi dấu phẩy và in những từ đó thành chuỗi theo thứ tự bảng chữ cái, phân tách nhau bằng dấu phẩy.


# Cau 1
# def number(a,b):
#     a,b < 0
# a = float(input("Nhap so a :"))
# b = float(input("Nhap so b :"))
# so_lon_hon = number(a,b)
# print(f"Số lớn hơn trong hai số là: {so_lon_hon}")

# cau 2
# def CheckEvenOdd(num):
#     if num % 2 == 0:
#         print(f"{num} Đây là số chẵn")
#     else:
#         print(f"{num} Đây là số lẻ")
# CheckEvenOdd (11)
# CheckEvenOdd (12)

# cau 3
# def is_leap_year(year):
 
#     if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
#         return True
#     else:
#         return False


# nam = int(input('Nhập năm: '))
# if is_leap_year(nam):
#     print('Năm nhuận')
# else:
#     print('Năm không nhuận')


# cau 5
# def sum_array():
#     elements = []
    
#     while True:
#         element = input("Nhập một phần tử (hoặc nhấn Enter để kết thúc): ")
#         if element == "":
#             break
#         elements.append(element)
    
#     valid_numbers = []
#     for element in elements:
#         try:
#             number = float(element)
#             valid_numbers.append(number)
#         except ValueError:
#             print(f"'{element}' không phải là số, bỏ qua.")
    
#     total_sum = sum(valid_numbers)
    
#     return total_sum

# print("Tổng của mảng là:", sum_array())

# cau 4
# input_string = input("Enter a string of words separated by commas: ")
# def sort_words(input_string):
#     words_list = input_string.split(',')
#     words_list = [word.strip() for word in words_list]
#     words_list.sort()
#     sorted_string = ', '.join(words_list)
#     return sorted_string

# sorted_string = sort_words(input_string)
# print(sorted_string)