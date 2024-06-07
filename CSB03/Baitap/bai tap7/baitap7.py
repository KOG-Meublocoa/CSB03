# cau 1
# numbers = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5,
#                'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9, 'X': 10}
# n = input('Input: '),
# if n in numbers :
#     print (numbers[n])
# else:
#     print('Not found')

# cau 2
# numbers = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5,
#                'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9, 'X': 10}
# numbers_2 = {'XI': 11, 'XII': 12, 'XIII': 13, 'XIV': 14, 'XV': 15,
#                 'XVI': 16, 'XVII': 17, 'XVIII': 18, 'XIX': 19, 'XX': 20}
# numbers.update=(numbers_2)
# n = input('Input: '),
# if n in numbers :
#     print (numbers[n])
# else:
#     print('Not found')

# cau 3
# number_list = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X',
#                  'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX']
# list= []
# dem=1
# while dem <= len(number_list):
#     list.append(dem)
# dem=+1  
# numbers=dict(zip(number_list,list))
# n = input('Input:'),
# if n in numbers:
#     print(numbers[n])
# else:
#     print('Not found')

# cau 4
# students = [{'firstName': 'Nikki', 'lastName': 'Roysden'},
#             {'firstName': 'Mervin', 'lastName': 'Friedland'},
#             {'firstName': 'Aron', 'lastName': 'Wilkins'}],
# print('List of students:')
# for i in students:
#     print(f"-{i['firstName']} {i['lastName']}")

# cau 5
# names = {
#   'students': [
#     {'firstName': 'Nikki', 'lastName': 'Roysden'},
#     {'firstName': 'Mervin', 'lastName': 'Friedland'},
#     {'firstName': 'Aron', 'lastName': 'Wilkins'}
#   ],
#   'teachers': [
#     {'firstName': 'Amberly', 'lastName': 'Calico'},
#     {'firstName': 'Regine', 'lastName': 'Agtarap'}
#   ]
# }
# print('List of students:')
# for x in names['students']:
#     print(f"-{x['firstName']} {x['lastName']}")
# print('List of teachers:')
# for y in names['teachers']:
#     print(f"-{y['firstName']} {y['lastName']}")

# cau 6
# char = {}
# chuoi = str(input('Input a text: '))
# for i in chuoi:
#     if i in char:
#         char[i]+=1
#     else:
#         char[i] = 1
# print(char)