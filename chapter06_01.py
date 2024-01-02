#파이썬 클래스
#OOP(객체 지향 프로그래밍), Self, 인스턴스 메소드, 인스턴스 변수

#클래스와 인스턴스의 차이 이해

#예제 1

class Dog(object):
    species = "firstdog"

    def __init__(self, name, age):
        self.name = name
        self.age = age

print(Dog)

#인스턴스화
a = Dog("Harry", 2)
b = Dog("Ron", 2)

print(a == b, id(a), id(b))

#네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
print("dog1", a.__dict__)
print("dog2", b.__dict__)

#클래스 변수 : 직접 접근 가능
#인스턴스 변수 : 객체마다 별도 존재

#인스턴스 속성 확인
print("{} is {} and {} is {}".format(a.name, a.age, b.name, b.age))

if a.species == "firstdog":
    print("{0} is {1}".format(a.name, a.species))

print(Dog.species)
print(a.species)
print(b.species)

#예제 2
#self의 이해

class SelfTest:
    def func1():
        print("Func1 called")
    def func2(self):
        print("Func2 called")

f = SelfTest()

# print(dir(f))
# print(id(f))
#  f.func1()
f.func2()
SelfTest.func1() 
#SelfTest.func2() #예외 발생
SelfTest.func2(f)

#예제 3
#클래스 변수, 인스턴스 변수

class Warehouse:
    stock_num = 0

    def __init__(self, name):
        self.name = name
        Warehouse.stock_num += 1

    def __del__(self):
        Warehouse.stock_num -= 1

user1 = Warehouse("Lee")
user2 = Warehouse("Cho")

print(Warehouse.stock_num)

print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print("before : ", Warehouse.__dict__)
print(user1.stock_num)

del user1
print("after : ", Warehouse.__dict__)

#예제 4
class Dog(object):
    species = "firstdog"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return '{} is {} years old'.format(self.name, self.age)
    
    def speak(self, sound):
        return "{} says {}!".format(self.name, sound)
    
c = Dog('Jenny', 4)
d = Dog('Lisa', 5)

print(c.info())
print(d.info())

print(c.speak("bow wow"))