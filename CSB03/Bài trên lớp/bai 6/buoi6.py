# # ngoac vuong thi khong can chu "list"
# student = list(("huy","ngoc","lam","tai","khoi","bach","hieu")) 

# print(student[1])

# student[1] = "hieu"

# print(student[1])

# student.append("ngoc")

# print(student)

# student.insert(3,"khoa")

# print(student)

# myNumber = [1, 2 ,4 ,9]

# student.extend(myNumber)

# print(student)

# xoa bang value:
# student.remove("huy")

# print(student)

# xoa bang index:
# student.pop(0)

# print(student)

# del student[9]

# print(student)

# del student

# student.clear()

# print(student)

# for i in student:
#     print(i)

# x = 0
# while x < len(student):
#       print(student(x))
#       x += 1

# newList = student +myNumber
# print(newList) 

# myTuples = ("hieu","lam","ngoc","khoa")

# myNumberTuples = tuple((1 , 5, 3, 9, 0))

# myList = List(myTuples)



# Bài 1:
    # - Hỏi người dùng món ăn mà người dùng muốn. Cho món ăn vào list. In ra các món ăn trong list, mỗi món một dòng
    # - Hỏi người dùng muốn bỏ món ăn nào, in món đó ra và loại bỏ món khỏi list
# Bài 2: Tính tổng các số trong một list (List nhập từ bàn phím)
# Bài 3: Tìm số lớn nhất trong một list (List nhập từ bàn phím)
# Bài 4: Sắp xếp các số trong list theo thứ tự tăng dần (không dùng hàm sort, sorted, List nhập từ bàn phím))


# bai 1
# A = str(input("Hỏi người dùng món ăn mà người dùng muốn?"))
# B =  list(("Pho","Mi xao","Com tam","Banh mi","Mien","Chao","Banh mi bo kho","Hu tieu","Nui"))
# B.append(A)
# x=0
# while x<len(B):
#     print(B[x])
#     x+=1
# while True:
#     remove_food = input("Chọn món ăn để loại bỏ (hoặc chọn 'quit' để dừng): ")
#     if remove_food.lower() == 'quit':
#         break
#     if remove_food in B:
#         print(f"Loại bỏ {remove_food} khỏi danh sách...")
#        B.remove(remove_food)
#     else:
#         print(f"{remove_food} không ở trong danh sách.")
# print("Danh sách món ăn yêu thích sau khi cập nhật:")
# for food in B:
#     print(food)

# bai 2
# nums = [1, 2, 3, 4, 5, 6]
# def totalNums(x):
#     sum = 0
#     for i in x:
#         sum += i
#     return sum
# print(totalNums(nums))

# bai 3

# bai 4
