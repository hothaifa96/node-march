import flask as flask


class Dog:
    def __init__(self,name,color,speed,favfood,price):
        self.speed= speed
        self.color= color
        self.name= name
        self.__favfood= favfood
        self.__price=price

    def get_price(self):
        return self.__price*1.17
    def set_price(self,new_price):
        self.__price= new_price if new_price > self.__price else self.__price
    def get_favfood(self):
        if self.__favfood is not None:
            return self.__favfood
    def bark(self):
        print(f'barking {self.name}')
    def eat(self):
        print(f'eating {self.__favfood}')
    def __str__(self):
        return f'{self.name} in this color {self.color}'
class Cat:
    def __init__(self,name,age,lives,color='white'):
        self.name = name
        self.age= age
        self.lives=lives
        self.color=color
    # func
    def meow(self):
        if self.color != 'white':
            print(f'meeeeowwww {self.name}')
        else:
            print(f'mooowoowo {self.name}')
    def jump(self,m):
        print(f'jumping {m}m')
    def __str__(self):
        return f'{self.name} {self.age}'

# c1 = Cat('petsi',12,7,'black')
# c2 = Cat('gibour',22,2)
#
# # print(petsi)
# # petsi.meow()
# # petsi.meow()
# # petsi.jump(20)
# #
# # gibour.meow()
#
# print(c1)
# print(c2)
# c1.meow()

# d1 = Dog('kay','brown','20','bonzo')
# print(d1)
# d1.bark()
# print(d1.get_favfood('owNr'))
#
# d1.color='yellow'

