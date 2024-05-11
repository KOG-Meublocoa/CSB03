# phan 1
# Câu 1. Liệt kê các đặc điểm giống nhau giữa list và tuple.
# -là danh sách lưu trữ dữ liệu một cách tuần tự, có các địa chỉ được gán cho các thành phần của danh sách ( được gọi là index )
# -Vị trí bắt đầu từ [0]

# Câu 2. Cho biến employee = ('Jane', 22, 'Engineer'). Làm thế nào để thay đổi giá trị của employee[1] thành 23?
# -employee[1]=23

# Câu 3. Cho biến cars = ['Mercedes', 'Rolls Royce', 'Lamborghini', 'Range Rover']. Biểu thức nào sau đây trả về ['Lamborghini', 'Range Rover']?
# -cars[2:]

# # Câu 4. Câu lệnh nào sau đây khởi tạo list có giá trị [(1, 1), (2, 4), (3, 9), (4, 16)]?
# -arr = [(x, x**2) for x in range(1, 5)]

# Câu 5. Cho đoạn code sau.
#     arr = [1, 2, 3, 4]
#     arr.append(5)
#     arr_2 = arr.copy()
#     arr = []
    
# Chọn giá trị đúng của arr_2 sau khi thực thi đoạn code trên.
# -[1, 2, 3, 4, 5]


# phan 2
# cau 1
# arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 90]
# arradd = []
# multi = []
# shift = []
# for i in range(len(arr)):
#     arradd.append(arr[i]+2)
#     multi.append(arr[i]*2)
#     shift.append(arr[(i + 2) % len(arr)])
# print('Original list :',arr)
# print('Add 2: ',arradd)
# print('Multiply by 2 :',multi)
# print('Shift 2 ',shift)

# cau 2
# arr = ['l', 'o', 'o', 'h', 'c', 'S', ' ', 'y', 'g', 'o', 'l',
#             'o', 'n', 'h', 'c', 'e', 'T', ' ', 'X', 'd', 'n', 'i', 'M']

# arr.reverse()
# for i in arr:
#     print(i, end='')

# cau 3
# n = int(input("Input a positive number: "))
# fib = [0]*(n + 1)
# fib[1] = 1
# for i in range(2, n + 1):
#     fib[i] = fib[i - 1] + fib[i - 2]
# print("First",n,"Fibonacci number(s):", *fib[1:])

# cau 4
# n = int(input("Number of items: "))
# menu = []
# pr = []
# for i in range(n):
#     item = input(f"Item {i+1}: ")
#     price = float(input(f"Price of item {i+1}: "))
#     menu.append((item, price))
#     pr.append(price)
# print(item)
# average_price = sum(pr)/n
# print(f"Average price: {average_price}")

# above_average_items = [a for a in menu if a[1] > average_price]
# print("Item(s) above average price:", *above_average_items)

# cau 5
# text = set(input('Write: ').split()) 
# x = len(text)
# print(x)
#split chia chuoi theo space
#set khong tinh gia tri lap lai