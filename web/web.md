# WEB
- WWW(World Wide Web): 인터넷으로 연결된 컴퓨터들이 정보를 공유하는 거대한 정보공간
- Web 기술: Web site, Web application을 통해 사용자들이 정보를 검색하고 상호작용하는 기술
- Web site: 여러 개의 Web page가 모인 것으로, 사용자들에게 정보나 서비스를 제공하는 공간
- Web page: HTML, CSS 등의 웹 기술을 이용하여 만들어진 Web Site를 구성하는 하나의 요소

![alt text](image.png)

# 웹 구조화(HTML)

- HTML(HyperText Markup Language): 웹페이지의 "의미"와 "구조"를 정의하는 단어
- HyperText: 웹 페이지를 다른 페이지로 연결하는 링크, 참조를 통해 다른 문서로 즉시 접근
  - Hypertext의 특징: 비선형성, 상호연결성, 사용자 주도 탐색
- Markup Language: 태그 등을 이용하여 "문서나 데이터"의 "구조"를 명시하는 언어
  - 예: HTML, Markdown

## HTML의 구조

***"! + tab" 하면 기본 뼈대를 작성해줌***

1) !DOCTYPE html: 해당 문서가 html임을 나타냄

2) html /html: 전체 페이지의 콘텐츠 포함 --> 웹 페이지를 구성하는 모든 내용

3) title /title: 브라우저 탭 및 즐겨찾기 시 표시되는 제목

4) head /head
   - HTML 문서에 관련된 설명, 설정 등 컴퓨터가 식별하는 메타데이터
   - ***사용자에게 보이지 않음***

5) body /body

    - HTML 문서의 내용을 나타냄
    - 페이지에 표시되는 모든 콘텐츠 작성
    - 한 문서에 ***하나의 body 요소***만 존재

### HTML Element
- 하나의 요소는 여는 태그와 닫는 태그, 그 안의 내용으로 구성됨
- 닫는 태그는 태그 이름 앞에 슬래시가 포함됨 -> meta와 같이 닫는 태그가 없는 경우도 존재

### HTML Attribute
- 사용자가 원하는 기준에 맞도록 요소를 설정하고나 다양한 방식으로 요소의 동작을 조절하기 위한 값
- 목적
  - 나타내고 싶지 않지만 추가적인 기능과 내용 담고 싶을 때 사용
  - CSS에서 스타일 적용을 위해 해당 요소를 선택하기 위한 값으로 활용
- ""를 사용
- href --> a(anchor)의 필수 속성
- img --> 닫는 태그는 없음(텍스트가 필요 없기 때문), src(source) 필수 요구 / alt -> 시각장애인의 스크린 리더 사용할 때


### HTML Structure
- h1~6: 단순히 텍스트 크기만 큰 것이 아닌, 문서의 최상위 제목이라는 의미 부여 ==> 의미가 문법적인 기능을 가지진 않음 but 암묵적인 rule을 정할 수 있음
- p
- list: ol(순서가 있는 부모태그), ul(순서가 없는 부모태그), li(내부 리스트)
- Emphasis & Importance: em, strong


# 웹 스타일링(CSS)
- CSS(Cascading Style Sheet): 웹페이의 디자인과 레이아웃을 구성하는 언어 
![alt text](image-1.png)

## CSS 적용방법
1. Inline 스타일: HTML 요소 안에 style 속성 값으로 작성
2. Internal 스타일: head 태그 안에 style 태그에 작성
3. External 스타일: 별도 CSS 파일 생성 후 HTML link 태그 사용

## CSS Selectors
- HTML 요소를 선택하여 스타일을 적용할 수 있도록 하는 선택자

### 선택자의 종류
1) 기본 선택자
   - 전체(*) 선택자: HTML 모든 요소 선택
   - 요소(tag) 선택자: 지정한 모든 태그 선택
   - 클래스(class) 선택자: '.' 사용, 클래스 속성을 가진 모든 요소 선택
   - 아이디(id) 선택자: '#', 주어진 아이디 속성을 가진 요소, 문서에는 주어진 아이디를 가진 요소가 하나만 있어야 함
   - 속성(attr) 선택자 등

2) 결합자(Combinators)
   - 자손 결함자(" "(space))
      - 첫 번째 요소의 자손 요소들 선택
      - 예: p span 은 p 안에 있는 모든 span 선택
   - 자식 결합자(">")
      - 첫 번째 요소의 직계 자식만 선택
      - 예: ul > li은 ul안에 있는 li를 모두 선택
  

### 명시도
- 결과적으로 요소에 적용할 CSS 선언을 결정하기 위한 알고리즘
- CSS Selector에 내재되어 있는 가중치에 맞게 계산하여 결정
  - 동일한 요소를 가리키는 2개 이상의 규칙이 있는 경우 -> 가장 높은 명시도를 가진 Selector가 승리
- 명시도의 순서
  Importance(!important) - Inline style - 선택자(id - class - 요소) - 소스 코드 선언 순서

### Cascade(계단식)
- 한 요소에 동일한 가중치를 가진 선택자가 적용될 때, CSS에서 마지막에 나오는 선언이 사용


### CSS 속성 2가지 분류
- 상속되는 속성: Text 관련
- 상속되지 않는 속성: 배치 관련

**상속하지 않을 때 -> .outerbox > :not(.inner_box)**와 같이 작성


## CSS Box Model
- HTML 요소를 감싸는 사각형 상자 모델

### 박스 배치 타입
* 좌측 상단부터 시작 -> 오른쪽 또는 아래로 진행
- Block box: 외부 / 아래로 표기, 새로운 태그를 만들 때 새 줄에서 시작
    - div, p, h1, h2
- Inline box: 내부 / 오른쪽으로 표기, 태그의 줄이 바뀌지 않음
    - span, a, strong


"""
nav>ul>li*5>a

style nav {background-color: gray; padding: 10px 0}

padding은 요소 안의 여백
margin은 요소 밖의 여백
"""