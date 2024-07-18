# # 사용 전
# numbers = [1, 2, 3, 4, 5]
# squared_numbers = []

# for num in numbers:
#     squared_numbers.append(num**2)

# print(squared_numbers)


# # 사용 후

# squared_numbers2 = [num**2 for num in numbers]
# squared_numbers2 = list(num**2 for num in numbers)
# print(squared_numbers2)

# # List Comprehension 활용 예시 - "2차원 배열 생성 시 (인접행렬 생성 시)"
# data1 = [[0] * (5) for _ in range(5)]
# print(data1)
# # 또는
# data2 = [[0 for _ in range(5)] for _ in range(5)]
# print(data2)

# N x N 행렬
# 정수 N 입력
# 2차원 리스트 입력
# ---> 무조건 리스트

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'{tc} {arr}')