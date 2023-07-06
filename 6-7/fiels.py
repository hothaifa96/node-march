file = open('name.txt','r')


# while True:
#     user_input =input('enter a sen (q to exit)')
#     if user_input == 'q':
#         break
#     file.write(user_input+'\n')

print( file.read(6))
file.readline()
print( file.read(4))