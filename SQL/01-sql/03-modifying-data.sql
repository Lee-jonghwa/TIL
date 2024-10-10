-- 공통
SELECT * FROM articles;
DROP TABLE articles;
PRAGMA table_info('articles');


-- 1. Insert data into table
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

-- 2. Update data in table

-- 단일 행 수정
UPDATE
  articles
SET
  title = 'update Title'
WHERE
  id = 1; -- id가 1인 행만 title열의 값을 update Title로 변경

-- 여러 열 값 수정
UPDATE
  articles
SET
  title = 'update Title',
  content = 'update Content'
WHERE
  id = 2;


-- 3. Delete data from table
DELETE FROM
  articles
WHERE
  id = 1;


DELETE FROM
  articles
WHERE id IN(
SELECT id FROM articles
ORDER BY createdAt
LIMIT 2
);

-- 먼저 삭제할 ID를 찾음-> 찾은 ID 사용해서 삭제
