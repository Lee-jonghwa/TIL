def get_num(num1, num2):
    return num1 + num2

num1 = 5
num2 = 3

result = get_num(num1, num2)
print(result)


# Return이 없게 수정
def get_num(num1, num2):
    result = num1 + num2
    print(result)

num1 = 5
num2 = 3

get_num(num1, num2)