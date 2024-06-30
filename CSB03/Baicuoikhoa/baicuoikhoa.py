# cau 1
# so1 = int(input("Nhập số : "))
# so2 = int(input("Nhập số : "))
# tong = so1 + so2
# print(f"Tổng của {so1} và {so2} là {tong}")

# cau 2
# a=int(input("Nhap so :"))
# b=int(input("Nhap so :"))
# c=int(input("Nhap so :"))

# cau 3
# def is_palindrome(a_string):
#     a_string = a_string.lower().replace(' ', '')
#     return a_string == a_string[::-1]

# print(is_palindrome("anna")) 

# cau 4

# danh_sach_mon_da_goi = ["pho ,bun bo"]

# def them_mon_vao_danh_sach(mon):
#     if mon not in danh_sach_mon_da_goi:
#         danh_sach_mon_da_goi.append(mon)
#         print(f"Đã thêm món {mon} vào danh sách.")
#     else:
#         print(f"Món {mon} đã có trong danh sách.")

# def main():
#     while True:
#         mon_muon_dat = input("Nhập tên món muốn đặt (hoặc 'q' để thoát): ")
#         if mon_muon_dat.lower() == 'q':
#             break
#         them_mon_vao_danh_sach(mon_muon_dat)

# if __name__ == "__main__":
#     main()

# def mon_dat_them(them_mon):
#     while True:
#     mon_dat_them = input("Nhap them mon(hoac'e'de quay lai thoat):")
#     if mon_dat_them.lower()=='e':
#         break
#     them_mon_vao_danh_sach_da_chon(mon_dat_them)
# if _name_ =="_mon_dat_them_":
#    main()

# cau 5
# name_phone={
#      "Iphone":28.000000,
#     "Samsung N10": 	16.000000 ,
#      "Oppo 93 "	:7.500000 ,
#     "Vsmart" :	7.400000 ,
#     "Vivo" :4.200000 ,
# }
# print(name_phone)

# name=input("Nhap ten dien thoai :")
# print(name_phone[name])

# cau 6
# so =input("Nhập một số nguyên: ")
# print(len(so))

# cau 7
# list =[5, 1, 8, 92, -1, 30]
# list.sort()
# print(list)


# cau 8
# def fibonacci(n):
#     fib_sequence = [0,1]
#     for i in range(2, n):
#         next_fib = fib_sequence[-1] + fib_sequence[-2]
#         fib_sequence.append(next_fib)
#     return fib_sequence

# n = int(input("Nhập số n > 0: "))
# if n <= 0:
#     print("Vui lòng nhập số n lớn hơn 0.")
# else:
#     result = fibonacci(n)
#     print(f"{n} phần tử đầu tiên của dãy Fibonacci là: {result}")
