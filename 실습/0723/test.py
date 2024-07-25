# items 실습
# # 미션 1. 점수가 80점 이상, 이름이 대문자인 새 딕셔너리 생성

# student_scores = {
#     'alice': 85,
#     'bob': 92,
#     'charlie': 78,
#     'david': 95,
#     'eva': 88
# }

# high_scorers = {}
# for name, score in student_scores.items():
#     if (score >= 80):
#         high_scorers[name.upper()] = score
# print(high_scorers)


# high_scorers = {name.upper() : score for name, score in student_scores.items() if score >= 80}
# print(high_scorers)


# 미션 2
# new_dict의 결과가 각 혈액형 의 인원수로 나오게
blood_types = ['A', 'B', 'O', 'AB', 'A', 'O', 'B', 'A', 'AB', 'O', 'A', 'B']


# 1. [] 표기법을 사용한 방법
def count_blood_types(blood_types):
    new_dict = {}
    for blood_type in blood_types:
        if blood_type not in new_dict:
            new_dict[blood_type] = 1
        else:
            new_dict[blood_type] += 1
    return new_dict

print(count_blood_types(blood_types))  # {'A': 4, 'B': 3, 'O': 3, 'AB': 2}


# 2. get() 메서드를 사용한 방법
def count_blood_types(blood_types):
    new_dict = {}
    for blood_type in blood_types:
        new_dict[blood_type] = new_dict.get(blood_type, 0) + 1
    return new_dict

print(count_blood_types(blood_types))  # {'A': 4, 'B': 3, 'O': 3, 'AB': 2}


# 3. setdefault() 메서드를 사용한 방법

def count_blood_types(blood_types):
    new_dict = {}
    for blood_type in blood_types:
        new_dict[blood_type] = new_dict.setdefault(blood_type, 0) + 1
    return new_dict

print(count_blood_types(blood_types))  # {'A': 4, 'B': 3, 'O': 3, 'AB': 2}


# 4. counter 메서드 사용
from collections import Counter

new_dict = Counter(blood_types)
print(type(new_dict))