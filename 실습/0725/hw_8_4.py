class UserInfo:
    def __init__(self):
        self.user_list = {}
        self.name = None
        self.age = None

    def get_user_info(self):
        self.name = input('이름을 입력하세요: ')
        self.age = input('나이를 입력하세요: ')

        try:
            self.age = int(self.age)
        except ValueError:
            print('나이는 숫자로 입력해야 합니다.')
            self.name = None
            self.age = None
        else:
            self.user_list[self.name] = self.age

    def display_user_info(self):
        if self.name is None or self.age is None:
            print('사용자 정보가 입력되지 않았습니다.')
        else:
            print('사용자 정보:')
            print(f'이름: {self.name}')
            print(f'나이: {self.age}')

user = UserInfo()
user.get_user_info()
user.display_user_info()
