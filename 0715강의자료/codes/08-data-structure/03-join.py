my_list = ['my', 'name', 'is', 'jonghwa']

print(' '.join(my_list))
print(*my_list)


queue = [1, 2, 3, 4, 5]
first_element = queue.pop(0)
print(first_element) # 1 
## pop(x) 는 알고리즘 문제 풀 때 사용X
## 시간복잡도의 문제 --> 첫 x+1 번째 요소를 제거하고 나머지 요소를 한 칸씩 인덱스를 앞으로 당김
## 시간복잡도가 O(n) --> 시간 초과 발생



#해결시 덱 모듈 사용
from collections import deque
queue = deque([1, 2, 3, 4, 5])
first_element = queue.popleft()
print(first_element) # 1
# 시간복잡도가 O(1)


numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()
print(numbers) # [1, 1, 2, 3, 4, 5, 9]
numbers.sort(reverse= True)
print(numbers) # [9, 5, 4, 3, 2, 1, 1]

numbers = [3, 1, 4, 1, 5, 9, 2]
sorted_numbers1 = sorted(numbers)
print(sorted_numbers1) # [1, 1, 2, 3, 4, 5, 9]
sorted_numbers2 = sorted(numbers, reverse=True)
print(sorted_numbers2) # [9, 5, 4, 3, 2, 1, 1]


# 차이 : sort는 원본 변경 O, sorted는 원본 변경x
# 차이 : sort는 반환값 X, sorted는 반환값 O