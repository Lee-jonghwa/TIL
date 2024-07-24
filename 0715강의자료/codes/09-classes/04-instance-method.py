class Person:
    
    def __init__(self, name):
        self.name = name
        # 왼쪽 name = instance 변수
        # 오른쪽 name : 생성자 메서드의 매개변수 이름
        print('인스턴스가 생성되었습니다.')

    def greeting(self): # 인자가 필요하면 self를 먼저 쓰고 씀
        print(f'안녕하세요. {self.name}입니다.')
        # 그냥 name으로 하면 존재하지 않는다고 뜸.

person1 = Person('지민') # 인스턴스가 생성되었습니다.
person1.greeting() # 안녕하세요. 지민입니다. # 객체지향
# Person.greeting(person1) # 절차지향