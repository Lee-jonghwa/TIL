packed_values = 1, 2, 3, 4, 5
print(packed_values)  # (1, 2, 3, 4, 5)


numbers = [1, 2, 3, 4, 5]
a, *b, c = numbers
print(a)  # 1
print(b)  # [2, 3, 4]
print(c)  # 5


def my_func(*objects):
    print(objects)  # (1, 2, 3, 4, 5)
    print(type(objects))  # <class 'tuple'>


my_func(1, 2, 3, 4, 5)
# (1, 2, 3, 4, 5)
# <class 'tuple'>


numbers = [1, 2, 3, 4, 5]
a, b, *c, d, e = numbers

print(a)  # 1
print(b)  # [2, 3, 4]
# 남은 요소들을 리스트로 패킹하여 할당
print(c)  # 5
print(d)
print(e)