def make_sum(pram1, pram2):
    """이것은 두 수를 받아
    두 수의 합을 반환하는 함수입니다.
    >>> make_sum(1, 2)
    3
    """
    return pram1 + pram2


result = make_sum(100, 30)
print(result) # 130

return_value = print(result)
print(return_value) # None
# Print는 Return이 None임
# -> print는 출력을 하는 거지 값을 반환을 하는 게 아님
# Return과 출력은 다름

def my_func() :
    print('hello')

result = my_func()
print(result)