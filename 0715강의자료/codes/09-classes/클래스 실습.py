
# class Person:
#     # 클래스 변수
#     name = 'Kai'

# # 클래스 변수 호출
# print(Person.name)

# # 1. 객체(인스턴스) 생성
# # 객체(인스턴스) = 클래스명()
# kai = Person()
# print(kai.name)


# class Person:
#     def say(self):
#         print('Welcome.')

# # 1. 객체 생성
# kai = Person()
# # 2. 메서드 호출
# kai.say()

# class Person:
#     # 생성자 메서드 : 객체 초기화 작업을 수행
#     # 객체가 생성될 때 필요한 모두 초기 설정 수행
#     # 즉, 객체가 사용가능한 상태로 만들어줌
#     def __init__(self, name): #name -> 매개변수
#         # 인스턴스 변수
#         self.name = name
    
#     def say(self):
#         print(f'welcome. {self.name}')

# kai = Person("kai") # "kai" --> 인자
# kai.say()

# class Singer:
#     def __init__(self, name, birth, nation):
#         self.name = name
#         self.job = 'singer'
#         self.birth = birth
#         self.nation = nation
    
#     def rap(self):
#         print('rap')
    
#     def dance(self):
#         print('dance')

#     def cowmori(self):
#         print('cowcow')

# iu = Singer('iu','1993년 5월 16일','Korea')
# print(iu.job)
# print(iu.birth)
# print(iu.job)


# class Singer:
#     def __init__(self):
#         self.occ = "가수"
#         self.birth = '1993년 5월 16일'
#         self.nat = '대한민국'

#     def rap(self):
#         print('rap')
    
#     def dance(self):
#         print('dance')

#     def cowmori(self):
#         print('cowcow')


# # 객체 생성하기
# singer = Singer()
# # 인스턴스 속성 출력
# print(singer.occ)
# print(singer.birth)
# print(singer.nat)
# # 인스턴스 메서드 출력
# singer.rap()
# singer.dance()
# singer.cowmori()



# 클래스 메서드 실습

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
    
    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)
    
# 사용예시
circle1 = Circle(5)
circle2 = Circle.from_diameter(10)

print(f'{circle1.area():.2f}')
print(f'{circle2.area():.2f}')


# 스태틱 메서드 실습

class MathUtils:

    @staticmethod
    def add(x, y):
        return x + y # 8
    
    @staticmethod
    def is_even(num):
        return num% 2 ==0 # True
    
print(MathUtils.add(5, 3))
print(MathUtils.is_even(4))


# 상속 실습

class Keyboard:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def info(self):
        print(f'Model : {self.model}, Color : {self.color}')


class ActuationPoint(Keyboard):
    def acpoint(self, point) :
        self.point = point
        print(f'actuationpoint : {self.point}')


hansung = ActuationPoint('hansung', 'white')
# info() 메서드 호출
hansung.info() # Model : hansung, Color : white
# acpoint 메서드 호출
hansung.acpoint(1.2) # actuationpoint : 1.2


# 다중 상속, .super()

class Parent:
    def greet(self):
        print('Hello from parent')

class Child(Parent):
    def greet(self):
        super().greet()  # Hello from parent
        print('Hello from child')

child = Child()
child.greet()

'''
Hello from parent
Hello from child
'''


class A : pass
class B(A) : pass
class C(A) : pass
class D(B, C) : pass

print(D.mro())
# <class '__main__.D'>, 
# <class '__main__.B'>, 
# <class '__main__.C'>, 
# <class '__main__.A'>
# <class 'object'>

# 어떤 순서로 MRO 출력?

# D - B - C - A - object


# overridding?
# 오버라이딩 == 재정의
# 부모클래스에서 정의한 메서드를 자식 클래스에서 재정의
# 같은 이름의 메서드를 자식클래스에서 변경

class Animal:
    def speak(self):
        print('동물소리')

class Dog(Animal):
    def speak(self):
        print('멍멍')

class Cat(Animal):
    def speak(self):
        print('야옹')

dog = Dog()
dog.speak() # 멍멍

seongwook = Cat()
seongwook.speak() # 야옹


# 스마트폰 다중상속
class Tool :
    def __init__(self, name):
        self.name = name # 도구의 이름 저장

    def use(self):
        print(f'{self.name} 사용') #도구 사용 메시지 출력

class ElectronicDevice:
    def __init__(self,power):
        self.power = power # 전자기기 전원 정보 저장

    def turn_on(self):
        print(f'{self.power}volt 전원 켜기')

class Smartphone(Tool, ElectronicDevice):
    def __init__(self, name, power, os):
        Tool.__init__(self, name) # Tool 클래스의 생성자 메서드 호출
        # super().__init__() : 틀린 표현은 아님, 유지 보수성을 해칠 수도 있음
        ElectronicDevice.__init__(self, power) # ElectronicDevice 클래스의 생성자 메서드 호출
        self.os = os

    def run_app(self):
        print(f'{self.os}에서 앱 실행')

# 스마트폰 인스턴스 생성
my_phone = Smartphone('Galaxy', 220, "Android")

# 메서드 호출
my_phone.use()
my_phone.turn_on()
my_phone.run_app()




# 상속받은 클래스에서 생성자 메서드를 호출할 때, 필요한 인자만 가지고 오려면
class Parent:
    def __init__(self, age, name, address):
        self.age = age
        self.name = name
        self.address = address

class Child(Parent):
    def __init__(self, age):
        Parent.__init__(self, age, None, None)



# 다중 상속에서 super 사용하지 않는 이유 -> 유지보수성