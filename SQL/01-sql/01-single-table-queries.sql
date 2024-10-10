-- SQLBook: Code
-- 01. Querying data
SELECT
  LastName
FROM
  employees;

SELECT
  LastName, FirstName
FROM
  employees;

SELECT
  *
FROM
  employees

SELECT
  FirstName As '이름'
FROM
  employees

SELECT
  Name,
  Milliseconds / 60000 AS '재생 시간(분)'
FROM
  tracks;

-- 02. Sorting data

SELECT
  FirstName
From
  employees
ORDER BY
  FirstName;

SELECT
  FirstName
From
  employees
ORDER BY
  FirstName DESC;


SELECT
  Country, City
FROM
  customers
ORDER BY
  Country DESC,
  City;

SELECT
  Name,
  Milliseconds / 60000 AS '재생 시간(분)'
FROM
  tracks
ORDER BY
  Milliseconds DESC

-- NULL 정렬 예시
SELECT
  ReportsTo
FROM
  employees
ORDER BY
  ReportsTo;



-- 03. Filtering data
SELECT
  Country
FROM
  customers
ORDER BY
  Country;


SELECT DISTINCT
  Country
FROM
  customers
ORDER BY
  Country;


SELECT
  LastName, FirstName, City
FROM
  customers
WHERE
  City = 'Prague';

SELECT
  LastName, FirstName, City
FROM
  customers
WHERE
  City != 'Prague';

SELECT
  LastName, FirstName, Company, Country
FROM
  customers
WHERE
  Company IS NULL
  AND country = 'USA';

SELECT
  LastName, FirstName, Company, Country
FROM
  customers
WHERE
  Company IS NULL
  OR country = 'USA';

SELECT
  Name, Bytes
FROM
  tracks
WHERE
  Bytes BETWEEN 10000 and 500000


SELECT
  Name, Bytes
FROM
  tracks
WHERE
  Bytes BETWEEN 10000 and 500000
ORDER BY
  Bytes


SELECT
  LastName, FirstName, Country
FROM
  customers
WHERE
  Country IN ('Canada', 'Germany', 'France')


SELECT
  LastName, FirstName, Country
FROM
  customers
WHERE
  Country NOT IN ('Canada', 'Germany', 'France')

SELECT
  LastName, FirstName
FROM
  customers
WHERE
  LastName LIKE '%son'

SELECT
  LastName, FirstName
FROM
  customers
WHERE
  FirstName LIKE '___a'

SELECT
  TrackId, Name, Bytes
FROM
  tracks
ORDER BY
  Bytes DESC
LIMIT 7;

SELECT
  TrackId, Name, Bytes
FROM
  tracks
ORDER BY
  Bytes DESC
LIMIT 3, 4;
-- LIMIT 4 OFFSET 3;

-- 04. Grouping data

SELECT
  Country, COUNT(*)
FROM
  customers
GROUP BY
  Country



-- employees 테이블에서 LastName 필드만 선택해라
SELECT
  LastName
FROM
  employees;

-- employees 테이블에서 LastName, FirstName 필드만 선택해라
SELECT
  LastName, FirstName
FROM
  employees;


SELECT
  *
FROM
  employees;


SELECT
  FirstName AS '이름'
FROM
  employees;


SELECT
  Name,
  Milliseconds / 60000 AS '재생 시간(분)'
FROM
  tracks;

-- 오름차순 정렬
SELECT
  FirstName
FROM
  employees
ORDER BY
  FirstName;
  -- FirstName ASC;

-- 내림차순 정렬
SELECT
  FirstName
FROM
  employees
ORDER BY
  FirstName DESC;


SELECT
  Country, City
FROM
  customers
ORDER BY
  Country DESC,
  City;


SELECT
  Milliseconds / 60000 AS '재생 시간(분)'
FROM
  tracks
ORDER BY
-- 계산된 값을 기준으로 정렬
  Milliseconds DESC;

-- NULL은 None 과 같음
SELECT
  postalCode
FROM
  customers
ORDER BY
  PostalCode;

SELECT DISTINCT
  Country
FROM
  customers
ORDER BY
  Country;


SELECT
  LastName, FirstName, City
FROM
  customers
WHERE
  City = 'Prague';

SELECT
  LastName, FirstName, City
FROM
  customers
WHERE
  City != 'Prague';


SELECT
  LastName, FirstName, Company, Country
FROM
  customers
WHERE
  Company IS NULL
  AND Country = 'USA';

SELECT
  LastName, FirstName, Company, Country
FROM
  customers
WHERE
  Company IS NULL
  OR Country = 'USA';


SELECT
  Name, Bytes
FROM
  tracks
WHERE
  Bytes BETWEEN 10000 AND 500000;

SELECT
  Name, Bytes
FROM
  tracks
WHERE
  Bytes BETWEEN 10000 AND 500000
ORDER BY
  Bytes;


SELECT
  LastName, FirstName, Country
FROM
  customers
WHERE
  Country IN ('Canada', 'Germany', 'France')


SELECT
  LastName, FirstName, Country
FROM
  customers
WHERE
  Country NOT IN ('Canada', 'Germany', 'France')


-- 패턴 매칭

SELECT
  LastName, FirstName, Country
FROM
  customers
WHERE
  LastName LIKE '%son'

SELECT
  TrackID, Name, Bytes
FROM
  tracks
ORDER BY
  Bytes DESC
LIMIT
  3, 4;


SELECT
  Country, COUNT(*)
FROM
  customers
GROUP BY
  Country;

SELECT
  Composer

CREATE TABLE examples (
  ExamId INTEGER PRIMARY KEY AUTOINCREMENT,
  LastName VARCHAR(50) NOT NULL,
  FirstName VARCHAR(50) NOT NULL
);

ALTER TABLE
  examples
ADD COLUMN
  Country VARCHAR(100) NOT NULL DEFAULT 'default value';

ALTER TABLE
  examples
ADD COLUMN
  Age INTEGER NOT NULL DEFAULT 0;

ALTER TABLE
  examples
ADD COLUMN
  Address VARCHAR(100) NOT NULL DEFAULT 'default value';

ALTER TABLE examples
RENAME TO new_examples;

ALTER TABLE new_examples
RENAME COLUMN Address TO PostCode;

ALTER TABLE new_examples
DROP COLUMN PostCode;

DROP TABLE new_examples;

DROP TABLE examples;