# 1. Positional Arguments
# def greet(name, age):
#     print(f'안녕하세요, {name}님! {age}살이시군요.')

# greet('Alice', 25) #안녕하세요, Alice님! 25살이시군요.
# greet(25, 'Alice') #안녕하세요, 25님! Alice살이시군요.
# greet('Alice') #TypeError: greet() missing 1 required positional argument: 'age'

# 2. Default Argument Values
# def greet(name, age = 30):
#     print(f'안녕하세요, {name}님! {age}살이시군요')

# greet('Bob') #안녕하세요, Bob님! 30살이시군요
# greet('Charlie', 40) #안녕하세요, Charlie님! 40살이시군요

# 3. Keyword Arguments
def greet(name, age):
    print(f'안녕하세요, {name}님! {age}살이시군요')

greet(name = 'Dave', age = 35) #안녕하세요, Dave님! 35살이시군요
greet(age = 35, name = 'Dave') #안녕하세요, Dave님! 35살이시군요
greet('Dave', age = 35 ) # positional argument follows keyword argument

# 4. Arbitrary Argument Lists
# def calculate_sum(*args): #임의의 인자 사용시 args(arguments) 관습적 사용
#     print(args)
#     print(type(args)) # <class 'tuple'>

# calculate_sum(1, 100, 5000, 30) #(1, 100, 5000, 30)

# def calculate_sum(prams,*args): #임의의 인자 사용시 args(arguments) 관습적 사용
#     print(args)
#     print(type(args)) # <class 'tuple'>
# ## 위치 인자는 임의 인자 뒤에 올 수 없음.
# ## 앞에 위치인자가 오면 그 개수만큼 인자를 들고 감
# 
# calculate_sum(1, 100, 5000, 30) #(100, 5000, 30)
# 5. Arbitrary Keyword Argument Lists
def print_info(**kwargs):
    print(kwargs)

print_info(name = 'Eve', age = 30) # {'name': 'Eve', 'age': 30}

# 인자의 모든 종류를 적용한 예시
def func(pos1, pos2, default_arg='default', *args, **kwargs):
    print('pos1:', pos1)
    print('pos2:', pos2)
    print('default_arg:', default_arg)
    print('args:', args)
    print('kwargs:', kwargs)


func(1, 2, 3, 4, 5, 6, key1='value1', key2='value2')
#{'name': 'Eve', 'age': 30}
#pos1: 1
#pos2: 2
#default_arg: 3
#args: (4, 5, 6)
#kwargs: {'key1': 'value1', 'key2': 'value2'}