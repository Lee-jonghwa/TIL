my_dict_1 = {}
my_dict_2 = {'key': 'value'}
my_dict_3 = {
    'apple': 12,
    'list': [1, 2, 3]
}
print(my_dict_1)  # {}
print(my_dict_2)  # {'key': 'value'}
print(my_dict_3)  # {'apple': 12, 'list': [1, 2, 3]}


my_dict = {
    'apple': 12,
    'list': [1, 2, 3],
}

# key를 통해 value 접근
print(my_dict['apple'])

# 추가
my_dict['banana'] = 50
print(my_dict)

# 변경
# key가 추가가 되는 것이 아닌 변경이 되는 것
my_dict['banana'] = 60
print(my_dict)

#인덱스 불가 -> 키로 접근하여 key error가 뜸
print(my_dict[1])


# int는 변경 불가 --> 재할당 방법 밖에 없음
a = 100
a = 99