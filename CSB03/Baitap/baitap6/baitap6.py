# cau 1
# def is_int(x):
#   if x==int(x):
#     return True
#   else:
#     return False

# num =float(input("Input number: "))
# if is_int(num):
#   print(f'{num} is an integer')
# else: 
#   print(f'{num} is not an integer')

# cau 2
# import snt
# number = int(input('Print a number: '))
# if snt.snt(number):
#     print('la so nguyen to')
# else:
#     print('khong phai so nguyen to')

# cau 3
# import snt             
# def demsnt(n):
#     i = 2  #do so nguyen to bat dau tu 2
#     count = 0 #tao bien dem
#     while count < n:  #n la du lieu lay tu 'number'
#         if snt.snt(i):  #su dung ham ktra snt neu True thi print va tang dem
#             print(f"{i} ",end='')
#             count+=1
#         i+=1
# number = int(input('Print a number: '))
# demsnt(number)

# cau 4
# number = int(input('print a number: '))  
# def gthua(x):       #Tinh giai thừa
#     gt = 1
#     for i in range(1,x+1):
#         gt*=i
#     return gt
# def bieuthuc(n):
#     tong = 0
#     for i in range(1,n+1):
#         tong += gthua(i) / i
#     return tong
# print(bieuthuc(number))

# cau 5
# from datetime import datetime


# curr = datetime.now()
# print(curr)

# print(curr.strftime('Today is %d/%m/%y'))
# print(curr.strftime('Time right now: %H:%M:%S'))