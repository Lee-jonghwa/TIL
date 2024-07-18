# items = ['apple', 'banana', 'coconut']

# for item in items:
#     print(item)

# '''
# apple
# banana
# coconut
# '''


# country = 'Korea'

# for char in country:
#     print(char)

# for i in range(5):
#     print(i)


# my_dict = {
#     'x': 10,
#     'y': 20,
#     'z': 30,
# }

# for key in my_dict :
#     print(key)
#     print(my_dict[key])

# numbers = [4, 6, 10, -8, 5]

# for i in range(len(numbers)):
#     numbers[i] = numbers[i] * 2

# print(numbers)


# outers = ['A', 'B']
# inners = ['c', 'd']

# for outer in outers:
#     for inner in inners:
#         print(outer, inner)


# elements = [['A', 'B'],
#             ['c', 'd']
# ]

# for elem in elements:
#     for item in elem:
#         print(item)




# 중첩 for문 예제
# 정수 n을 입력받아 n단의 왼쪽 직각 이등변 삼각형을 그려보세요
n = int(input())

for i in range(1,n+1):
    print("*"*((2*i)+1))


n = int(input('n : '))
for i in range(n):
    for j in range(i + 1):
        print('*', end = '')
    print()
