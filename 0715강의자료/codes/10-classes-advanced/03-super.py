# super 사용 전
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email


class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        self.name = name
        self.age = age
        self.number = number
        self.email = email
        self.student_id = student_id



# super 사용 예시 - 단일 상속
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email

class Student(Person):
    def __init__(self, name, age, number, email,student_id, gpa):
        super().__init__(name, age, number, email)
        # self 쓸 필요 없음
        self.student_id = student_id
        self.gpa = gpa

# super 사용 예시 - 다중 상속
class ParentA:
    def __init__(self):
        self.value_a = 'ParentA'

    def show_value(self):
        print(f'Value from ParentA: {self.value_a}')


class ParentB:
    def __init__(self):
        self.value_b = 'ParentB'

    def show_value(self):
        print(f'Value from ParentB: {self.value_b}')
        ## 해당 상황에서 ParentB의 메서드를 사용하려면
        ## ParentB.show_value()를 사용해야 함.


class Child(ParentA, ParentB):
    def __init__(self):
        super().__init__()
        ## self를 안 넣어도 됨
        self.value_c = 'Child'
    # 상속순으로가지만, 호출하는 클래스에 메서드가 없으면 다음으로 넘어감

child1 = Child()
print(child1.value_a) # ParentA
print(child1.value_c) # Child
# print(child1.value_b) # AttributeError: 'Child' object has no attribute 'value_b'
# value_b가 있으려면 Child 클래스에 ParentB.__init__()필요