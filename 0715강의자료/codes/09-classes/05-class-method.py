class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1
    
    @classmethod
    def number_of_population(cls):
        print(f'인구수는 {cls.count}입니다.')
        # 호출하기 전까지는 cls가 무엇인지 모름
        # 호출하는 그 클래스
        # print(f'인구수는 {Person.count}입니다.')
        # 위가 될 수 없는 이유 : 클래스의 상속 때문
        # 하위 클래스가 사용할 수 없게됨


person1 = Person('iu')
person2 = Person('BTS')

 
Person.number_of_population() # 인구수는 2입니다.
# cls가 Person으로 결정