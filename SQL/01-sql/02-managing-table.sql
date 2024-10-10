-- SQLBook: Code
-- Table 구조 확인
PRAGMA table_info('examples');

-- 1. Create a table

CREATE TABLE articles(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(100) NOT NULL,
  content VARCHAR(200) NOT NULL,
  createdAt DATE NOT NULL
);

INSERT INTO
  articles (title, content, createdAt)
VALUES
  ('hello', 'world', '2000-01-01');


INSERT INTO
  articles (title, content, createdAt)
VALUES
  ('title1', 'content1', '1900-01-01'),
  ('title2', 'content2', '1800-01-01'),
  ('title3', 'content3', '1700-01-01');


INSERT INTO
  articles (title, content, createdAt)
VALUES
  ('title4', 'content4', DATE());

-- 2. Modifying table fields
-- 2.1 ADD COLUMN

-- sqlite는 단일 문을 사용하여 한번에 여러 열을 추가하는 것을 지원하지 않음

-- 2.2 RENAME COLUMN

-- 2.3 RENAME TO

-- 3. Delete a table


-- sqlite는 컬럼 수정 불가
-- 대신 테이블의 이름을 바꾸고, 새 테이블을 만들고 데이터를 새 테이블에 복사하는 방식을 사용
