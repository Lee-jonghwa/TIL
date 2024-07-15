

''' # 데이터 타입 출력 실습

a1 = 1
a2 = 2.3
a3 = 2 + 3j
a4 = 'hello'
a5 = True
a6 = [1, 2, 3]
a7 = (1, 2, 3)
a8 = range(1, 4)
a9 = {1, 2, 3}
a10 = {'apple' : 2, 'banana' : 3}
a11 = None
a12 = lambda x, y : x + y

b = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11]

print(type(a1))
print(type(a2))
print(type(a3))
print(type(a4))
print(type(a5))
print(type(a6))
print(type(a7))
print(type(a8))
print(type(a9))
print(type(a10))
print(type(a11))

for i in b :
    print(type(i))

for i in range(1, 13):
    var = f'a{i}'
    var = eval(var)
    print(type(var))


for i in range(1, 13):
    var = f'a{i}'
    var = eval(var)
    # eval global에서 해당되는 타입에 맞게 출력
    print(type(var))


# 메모리 주소 확인하는 방법

degree = 36.5
print(id(degree))
#메모리 주소는 실행할 때마다 바뀜

degree = 36.5
degree2 = 36.5
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(id(degree))
print(id(degree2))
print(id(list1))
print(id(list2))
#할당되는 값이 같다고 해서 주소가 같은 것은 아님
#Numeric, string과 같은 불변 객체는 같은 값을 가지면 대부분 같은 메모리 주소 공유
#list와 같은 가변 객체는 같은 값을 가져도 다른 메모리 주소를 가질 수 있다.

#재할당 시 메모리 주소

degree1 = 36.5
degree2 = 36.7
print(id(degree1))
print(id(degree2))


#파이썬 매서드들은 변수로 사용할 수 없음
#내장 함수를 변수로 할당하면 에러
a = [1, 2, 3]
sum = 8
print(sum(a))

'''

# 부동소수점 오류

# 거의 같다는 것에 대한 정의

a = 3.2 - 3.1
b = 1.2 - 1.1

print(abs(a-b) <= 1e-10)

import math
#isclose : 두 숫자가 거의 같은지를 확인
print(math.isclose(a,b))

num_a = f'{a:.1f}'
num_b = f'{b:.1f}'

print(num_a)
print(num_b)

'''
from decimal import Decimal

a = Decimal('3.2') - Decimal('3.1')
b = Decimal('3.3') - Decimal('3.2')

print(3.2 - 3.1)
print(3.3 - 3.2)

print(a)
print(b)
print(a == b)

print(f'{a:.3f}')
# 소수 셋째 자리까지 출력

# ctrl + 매서드 클릭하면 해당 매서드의 설명 볼 수 있음

'''
'''

str1 = [1, 2, 3]
str1[0] = 'a'

print(str1)



# 포맷팅 3가지 방법

name = input()
age = int(input())
height = float(input())

# %연산자
print('저의 이름은 %s이고, 나이는 %d세, 키는 %.2fcm 입니다' %(name, age, height))
# .format() 매서드
print('저의 이름은 {}이고, 나이는 {}세, 키는 {:.2f}cm 입니다'.format(name,age,height))
# f-string : 가장 많이 사용하는 방법
print(f'저의 이름은 {name}이고, 나이는 {age}세, 키는{height:.2f}cm 입니다')
#.nf : 소수점 n자리까지 표시


# 미션 2. 문자열 parsing

greeting = "hello world"

#greeting[start:end:step]

#1. step > 0 : start부터 end - 1까지, step 만큼 증가
#2. step < 0 : start부터 end + 1까지, step 만큼 감소

# step이 생략되면 기본값은 1
# start가 생략되면 기본값은 0
# end가 생략되면 기본값은 len()


# 1. 인덱싱 -> 알파벳 w 출력
print(greeting[6])
print(greeting[greeting.find('w')])

# 2-1. 슬라이싱 -> hello를 출력해 보세요.
print(greeting[:5])

# 2-2. 슬라이싱 -> world를 출력해 보세요.
print(greeting[6:])
# 공백도 값으로 취급

# 2-3. 슬라이싱 -> 거꾸로 출력해 보세요.
print(greeting[::-1])

# 3. 메서드를 사용하여 문자열의 길이를 출력
print(len(greeting))






'''