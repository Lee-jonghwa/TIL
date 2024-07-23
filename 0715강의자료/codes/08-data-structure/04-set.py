# # add
# my_set = {'a', 'b', 'c', 1, 2, 3}

# my_set.add(4)
# print(my_set)
# # 여러 번 시행 시 순서 바뀜
# # {1, 'c', 3, 2, 'a', 'b', 4}
# # {1, 2, 3, 'a', 4, 'c', 'b'}

# my_set.add(4)
# print(my_set) # {1, 2, 3, 'a', 4, 'c', 'b'}
# # 두 번 add한다고 해서 같은 값이 두 번 들어가는 것은 아님
# # (중복값제거)

# # clear
# my_set = {'a', 'b', 'c', 1, 2, 3}
# my_set.clear()
# print(my_set) # set()
 

# # remove
# my_set = {'a', 'b', 'c', 1, 2, 3}

# my_set.remove(2)
# print(my_set) # {1, 3, 'b', 'a', 'c'}

# my_set.remove(10)
# print(my_set) # KeyError: 10


# # pop
# my_set = {'a', 'b', 'c', 1, 2, 3}
# element = my_set.pop()
# print(element)
# # 규칙성 없이 빠짐
# # 1
# # a
# # c

# # discard
# my_set = {'a', 'b', 'c', 1, 2, 3}

# my_set.discard(2)
# print(my_set) # {1, 3, 'b', 'a', 'c'}

# my_set.discard(10)
# print(my_set.discard(10)) # None

# # update
# my_set = {'a', 'b', 'c', 1, 2, 3}

# my_set.update([1, 4, 5])
# print(my_set) # {1, 2, 3, 'c', 4, 5, 'b', 'a'}

# 집합 메서드
set1 = {0, 1, 2, 3, 4}
set2 = {1, 3, 5, 7, 9}
set3 = {0, 1}

print(set1.difference(set2)) # {0, 2, 4}
print(set1.intersection(set2)) # {1, 3}
print(set1.issubset(set2)) # False
print(set3.issubset(set1)) # True
print(set1.issuperset(set2)) # False
print(set1.issuperset(set3)) # True
print(set1.union(set2)) # {0, 1, 2, 3, 4, 5, 7, 9}