# thisdict = {
#     "class_name": "CSB03",
#     "year": 2024,
#     "student_count":10
# }

# access items
# print(thisdict["class_name"])

# change items
# thisdict["student_count"] = 9
# print(thisdict["student_count"])

# # add items 
# thisdict["new_student"]="Quynh Anh"
# print(thisdict)

# remove items

# remove theo key
# thisdict.pop("new_student")
# print(thisdict)

# remove phần tử cuối
# thisdict.popitem()
# print(thisdict)

# loop dictionaries
# for y in thisdict:
#     print(y)

# for x in thisdict:
#     print(thisdict[x])

# for a,b in thisdict.items():
#     print(a,b)

# copy
# new_dict = thisdict.copy()
# print(new_dict)

# nested
# my_class = {
#     "student1":{
#         "name":"Tai",
#         "age":18
#     },
#     "student2":{
#         "name":"Lam",
#         "age":17
#     },
#      "student3":{
#         "name":"Huy",
#         "age":16
#     },
# }

# for i in my_class.values():
#     print(i["name"])
    
# for x,y in my_class.items():
#     print(y["name"])


# cau 1.1
# name_computer ={
#     "HP" : 20,
#     "DELL" : 50,
#     "MACBOOK" : 12,
#     "ASUS" :30,
# }
# print(name_computer)

# # 1.2
# print(name_computer["MACBOOK"])
# # 1.3
# a=input("Nhap thiet bi :")
# print(name_computer[a])

# cau 2
# character = {
#     "Name": "Light",
#     "Age": 17,
#     "Strength": 8,
#     "Defense": 10,
#     "HP": 100,
#     "Backpack": ["Shield", "Bread Loaf"],
#     "Gold": 100,
#     "Level": 2
# }
# #1
# character["Gold"] += 50
# #2
# character["Backpack"].append("FlintStone")
# #3
# character["Pocket"] = ["MonsterDex", "Flashlight"]
# print(character)

students_details = {
    "Alice": {"age": 20, "score": 85},
    "Bob": {"age": 22, "score": 92},
    "Charlie": {"age": 21, "score": 78},
}
if "David" in students_details:
   print(students_details["David"])
else:
   print("David khong co trong danh sach")

