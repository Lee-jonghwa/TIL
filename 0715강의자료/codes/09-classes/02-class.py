# 클래스 정의
class Person:
    blood_color = 'red'  # attribute

    def __init__(self, name):  # method
        self.name = name

    def singing(self):  # method
        return f'{self.name}가 노래합니다.'


# 실제로 행동하는 건 class가 아닌 인스턴스(클래스는 blueprint!)

# 인스턴스 생성
singer1 = Person('iu')
# 생성될 때부터 person으로 클래스 정의

# (인스턴스) 메서드 호출
print(singer1.singing()) # iu가 노래합니다.

# 속성(변수) 접근
print(singer1.blood_color) # red

# 인스턴스 변수
print(singer1.name) # iu