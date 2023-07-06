#
# def greet():
#     print('hello')
# def greet_with_name(age=0,name='user'):
#     print(f'hello {name} {age}')
#
# def greet_group(*args):
#     print(args)
#     for st in args:
#         print(f'hello {st}')
#
# def greet_with_salary(**kwargs):
#     print(kwargs.items())
#     for k,v in kwargs.items():
#         if k == 'salary':
#             print(v)
#
#
# # greet_group('hodi','lior','ofek','gitam')
# greet_with_salary(name='suzi',salary=15000,happy=False)
#
# print('hodi',"gmail",sep='@',end='.com\n')
# print('hello')
#
#
# def functionname():
#     pass

# write a python code to print triangle using a user input

# n = int(input('please enter a number '))
#
# def draw(start,end,jump):
#     for i in range(start, end,jump):
#         print(' ' * (n - i), f'{i} ' * i)
#
# draw(0,n,1)
# draw(n,0,-1)



# -> func ->
# - func ->
# - func -
# -> func -

# def multi(*args):
#     s = 1
#     for x in args:
#         s*=x
#     return s
#
# def generate_jwt():
#     return 'hgfbjkadbgviladsbgk;ad'
# print(multi(111,66))
# g=generate_jwt()
# print(g)


import datetime
import time

print(datetime.datetime.now())
time.sleep(3)
print('hello')
