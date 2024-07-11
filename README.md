# GIT

## 기본 개념

### git을 쓰는 이유
1. git(로컬저장소) --- github, gitlab(원격저장소) 

2. bash를 쓰려고
    왜 개발자들은 bash를 더 많이 쓸까?
    bash는 위, 아래 방향키로 전에 입력했던 명령어들 재사용
    bash는 tab키를 이용해서 자동완성
    즉, **간편한 명령어**와 **편리한 개발환경** 보유

### Interface(리모컨과 유사)

1. GUI(graphic user interface)

2. TUI(Text User Interface)
    **Command Line Interface --- CLI**

### 깃의 영역
- local : working directory ->(add) staging area -> (commit) repository
    (push & pull/clone)
- github : remote repository

## 사용 방법

### 실행 방법
    git을 작동할 폴더에 들어가서 우클릭 -> open with bash

### 기본 문법
- git 시작 : git init
- git 종료 : rm -rf .git 또는 폴더에서 .git 폴더 삭제

- 파일 생성 : touch a.txt
- 파일 삭제 : rm a.txt
- 현재 디렉토리의 파일 목록 확인 : ls
- 폴더 생성 : mkdir new_folder
- 폴더 삭제 : rm -r new_folder

### cd 활용
- "~" : Home directory
- cd : 작업중인 디렉토리 변경
- cd ~ : 홈 디렉토리로 가기
- cd - : 뒤로 가기
- cd .. : 상위 디렉토리로 가기 
- cd ./~ => 상대 경로 (.이 현재 디렉토리를 의미)
    절대경로 : 전체 주소 작성
    상대경로 : 현재 디렉토리를 기준으로 상대적 위치
- start a.txt : 특정 문서 열기

### push 방법
- git config --global user.name "깃 사용자 이름"
- git config --global user.email "깃 메일 주소"
- git add . : 해당 디렉토리 모든 파일 add
- git status : commit할 준비 되었는지 확인(add 되었는지 확인)
- get remote add origin URL : origin이라는 이름으로 remote 연결
- get remote -v : remote 상태 확인
- git commit -m "" : 메시지와 함께 commit
- git push origin +master

### clone/pull 방법
- git clone URL : 클론
- git pull origin master : pull

# mark down 활용하기 

## 헤더 형식 알아보기

헤더 : #갯수에 따라 글씨 크기 다름
# 헤더적기 1
## 헤더적기 2
### 헤더적기 3
#### 헤더적기 4

---

## ordered / unordered 리스트

### ordered 리스트 적기
--> 순서가 있는 리스트

1. 엔터를 눌러보세요.
2. 엔터를 누르고 탭을 눌러보세요.
   1. 탭을 누르면 2-1
3. 두 번 엔터 누르면 3 

### unordered 리스트 적기
--> 순서가 없는 리스크

* -기호 또는 +기호 또는 *기호 모두 상관 없음
- 엔터를 여러번
+ *(애스터리스크 / asterisk)

마크다운에 한계가 있으므로, 깔끔하게만 작성한다고 생각

## 작성 기능

### 굵게 표현하기
- __굵은 글씨__
- **굵은 글씨**

    글 중간에 넣으려면 무조건 **로 사용

    글 중간에 **굵은 글씨** 넣기

### 기울기
- _기울기 글씨*
- *기울기 글씨*

    글 중간에 *기울기 글씨*를 넣기

### 굵게 및 기울임
- ___둘 다 하려면 이렇게___
_ 세 번 or * 세 번

### 취소선
- ~~물결물결~~

### 수평선
"-" 세 번
---

## 기타 작성 기능

### 체크리스크 만들기
- [X] 토스트
- [ ] 당근
- [ ] 양파
- [ ] 라면

### 코드블럭(중요!) --> 백틱 3번
- 프로그래밍 언어마다 다른 가독성으로 표시해줌.
- 다른 데서도 사용 많이함

```python
print('hello world')
```

```C
#include<studio.h>
int mail()
{

}
```

### 링크 URL 걸기
[네이버](https://www.naver.com)

markdown 공식 문서를 참고하여 추후 사용하면 댐

### 이미지 걸기
![고양이](https://postfiles.pstatic.net/MjAxOTEwMjhfMTM5/MDAxNTcyMjU1MjcxMTgy.KQlNPKpAtHC3dK2F6Vw4n8rK3y3XPTS4wLVpmAWy0a0g.D2U5-vKB_GCl2QRNUMjYZNmdit7gDa25FBXLvYwrE5Ig.PNG.charmed__/image.png?type=w966)