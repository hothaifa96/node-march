# 2
# for condition:
#     true block
# else:
#     false block

# 3

# number = [1,5,7,8,100]

# for i in range(len(number)//2):
#     print(number[i])

# for i in number[:len(number)//2 +1]:
#     print(i)

# print(number[:len(number)//2])

# 4 and 5
# words = ['static','hello','pen','boker miftsaaae']
#
# for word in words:
#     if len(word) <4 :
#         break
#     print(word.upper())

# 6

# name='ofnek segal'
#
# #a
# print(name[-5:])
# #b
# print(name[:len(name)//3])
# #c
# print(name.count('a'))
# #d
# print('b' in name)
# # e
# name_list=name.split()
# print(name_list)
# # f
# name_list.reverse()
# print(name_list)
# #g
# f_name =name_list[1]
# h= len(f_name)//2
#
# f_name= f_name[:h]+f_name[h+1:]
# name_list[1]=f_name
# print(name_list[1])
#
# # name= f'{name_list[0]} {name_list[1]}'
# name= ' '.join(name_list)
# print(name)

# numbers = [[12, 87, 5], [-1, 3000, 4], [-200, 8, 4]]
# temp = numbers[0][0]
#
# for list in numbers:
#     for number in list:
#         if number < temp:
#             temp = number
# print(temp)

# l1= [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
# l2 = [x for x in l1 if x%3==0  ]
#
# # l2=[]
# # for x in l1:
# #     if x%3==0:
# #         l2.append(x)
#
# print(l2)


import random

score_com = 0
score_user = 0
while score_user <4 and score_com <4:
    com = random.randrange(1, 4)
    user = int(input('enter a number 1-3:'))
    print(f'user{user}   <>   computer {com}')
    if com == user:
        print('tie')
    elif user - com in [-1,2]:
        score_com += 1
        print('computer')
    else:
        score_user += 1
        print('user')

