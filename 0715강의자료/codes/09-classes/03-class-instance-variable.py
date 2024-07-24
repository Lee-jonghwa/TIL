class Person:
    # 클래스 변수 count
    count = 0

    def __init__(self, name):
        # 인스턴스 변수 name
        self.name = name
        Person.count += 1

person1 = Person('iu')
person2 = Person('BTS')

print(Person.count)  # 2

##########################

class Circle:
    pi = 3.14

    def __init__(self, r):
        self.r = r

c1 = Circle(5)
c2 = Circle(10)

print(c1.r) # 5
print(c2.r) # 10

# c1.pi -> c1에서 pi변수가 있는지 확인
# -> 찾으러 클래스로 들어감 -> 클래스 변수 출력

print(Circle.pi) # 3.14
print(c1.pi) # 3.14
print(c2.pi) # 3.14


# c2의 인스턴스 변수 pi를 생성
# 인스턴스 변수 할당을 먼저 -> 없으면 클래스로
c2.pi = 5
print(Circle.pi) # 3.14
print(c1.pi) # 3.14
print(c2.pi) # 5

Circle.pi = 5
print(Circle.pi) # 5
print(c1.pi) # 5
print(c2.pi) # 5


