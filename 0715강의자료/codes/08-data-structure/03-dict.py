# # clear
# person = {'name': 'Alice', 'age': 25}
# person.clear()
# print(person)


# get
# person = {'name': 'Alice', 'age': 25}

# print(person.get('name')) # Alice
# print(person.get('country')) # None
# print(person.get('country','unknown')) # unknown
# print(person['contry']) # KeyError: 'contry'
# print(person) # {'name': 'Alice', 'age': 25}
# person['country'] = 'unknown'
# print(person) # {'name': 'Alice', 'age': 25, 'country': 'unknown'}
## get을 한다고 해서 추가 되는 것은 아님

# # keys
# person = {'name': 'Alice', 'age': 25}
# print(person.keys()) # dict_keys(['name', 'age'])
# ## 리스트 형태 유사 -> 시퀀스 데이터 --> iterable
# print(type(person.keys())) # <class 'dict_keys'>

# for item in person.keys():
#     print(item)
# '''
# name
# age
# '''

# # values
# person = {'name': 'Alice', 'age': 25}
# print(person.values()) # dict_values(['Alice', 25])

# for item in person.values():
#     print(item)
# '''
# Alice
# 25   
# '''

# # items
# person = {'name': 'Alice', 'age': 25}
# print(person.items()) #dict_items([('name', 'Alice'), ('age', 25)])

# for item in person.items():
#     print(item)
# '''
# ('name', 'Alice')
# ('age', 25)
# '''
# # 튜플 형태

# for key, value in person.items():
#     print(key, value)
# '''
# name Alice
# age 25
# '''
# # unpacking 활용

# # pop
# person = {'name': 'Alice', 'age': 25}

# print(person.pop('age')) # 25
# print(person) # {'name': 'Alice'}
# print(person.pop('country', None)) # None
# # 순회하는 딕셔너리에서 팝 사용할 때 유용할 듯
# print(person.pop('country')) # KeyError: 'country'


# setdefault
# person = {'name': 'Alice', 'age': 25}

# print(person.setdefault('country', 'KOREA')) # KOREA
# print(person) # {'name': 'Alice', 'age': 25, 'country': 'KOREA'}

# # update
# person = {'name': 'Alice', 'age': 25}
# other_person = {'name': 'Jane', 'gender': 'Female'}

# person.update(other_person)
# print(person) # {'name': 'Jane', 'age': 25, 'gender': 'Female'}

# person.update(age=50, country='KOREA')
# print(person) #{'name': 'Jane', 'age': 50, 'gender': 'Female', 'country': 'KOREA'} 

# # 키워드 인자로 넣을 때 키 인자는 문자열로 하지 않음 주의!

a = {}
b = {'name' : 'Alice', 'age' : 25}

a.update(b)
print(a) # {'name': 'Alice', 'age': 25}
b['name'] = 'Harry'
print(a) # {'name': 'Alice', 'age': 25}