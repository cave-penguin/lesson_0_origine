"""DROP TABLE IF EXISTS Songs;
CREATE TABLE Songs
(
    id        INT PRIMARY KEY AUTO_INCREMENT,
    place     INT,
    trackname VARCHAR(30),
    artist    VARCHAR(30),
    streams   INT
);

INSERT INTO Songs (place, trackname, artist, streams)
VALUES (4, 'Crazy On You', 'Heart', 76338),
       (3, 'My Lover', 'The Sounds', 99488),
       (2, 'Running up That Hill', 'Kate Bush', 121495),
       (5, 'Thrill', 'The Sounds', 49345),
       (1, 'Spent the Day in Bed', 'Morrissey', 174994);
SELECT trackname
FROM Songs
LIMIT 3
OFFSET 2;"""


"""
    запрос ниже извлекает из таблицы Songs все записи, которые в качестве значения поля streams имеют целочисленное значение, превышающее 100000:

SELECT *
FROM Songs
WHERE streams > 100000;

Чтобы извлечь только уникальные записи, необходимо воспользоваться ключевым словом DISTINCT, которое указывается непосредственно перед именами полей.
Например:

SELECT DISTINCT artist
FROM Songs;

Иногда при извлечении данных из таблицы может потребоваться получить лишь первую запись или некоторое определенное количество записей. Сделать это можно с помощью ключевого слова LIMIT.

Результатом приведенного ниже запроса:

SELECT trackname
FROM Songs
LIMIT 3;

Запрос выше извлекает поле trackname, а выражение LIMIT 3 говорит о том, что должно быть извлечено не более трех записей. Если необходимо получить следующие три записи, можно задать начальную точку извлечения с помощью ключевого слова OFFSET.

SELECT trackname
FROM Songs
LIMIT 3
OFFSET 2;

Выражение LIMIT 3 OFFSET 2 говорит о том, что должно быть извлечено три записи, начиная с записи с индексом два. Таким образом, первое число — это количество строк для извлечения, а второе — начальная точка.

Записи при использовании ключевого слова OFFSET индексируются с нуля, поэтому, например, выражение LIMIT 1 OFFSET 1 вернет вторую запись, а не первую.

Псевдонимы:

Даются с помощью ключевого слова AS, которое располагается между исходным именем поля и новым:

SELECT trackname AS 'Song name',
       artist AS Artist
FROM Songs;

Однострочные комментарии обозначаются двумя дефисами (--):

SELECT trackname    -- это комментарий
FROM Songs;

Многострочные комментарии обрамляются сочетанием символов /*:

/* это
многострочный
комментарий */

SELECT trackname
FROM Songs;
"""

"""
Агрегатные функции
 1 Функция AVG()
 2 Функция COUNT()
 3 Функции MIN() и MAX()
 4 Функция SUM()
 5 Функция GROUP_CONCAT()
 """


"""
Скрипт для создания таблицы Songs

DROP TABLE IF EXISTS Songs;
CREATE TABLE Songs
(
    id           INT PRIMARY KEY AUTO_INCREMENT,
    place        INT,
    trackname    VARCHAR(40),
    artist       VARCHAR(40),
    streams      INT,
    release_year INT,
    length       INT
);

INSERT INTO Songs (place, trackname, artist, streams, release_year, length)
VALUES (4, 'Crazy on You', 'Heart', 303885, 1976, 254),
       (7, 'My Lover', 'The Sounds', 211133, 2009, 266),
       (3, 'Running up That Hill', 'Kate Bush', 339583, NULL, 296),
       (5, 'Thrill', 'The Sounds', 294264, 2016, 228),
       (9, 'Spent the Day in Bed', 'Morrissey', 174994, 2017, 259),
       (2, 'Bigmouth Strikes Again', 'The Smiths', 379112, 1986, 195),
       (6, 'Painted By Numbers', 'The Sounds', 265121, 2006, 200),
       (8, 'Let Me Kiss You', 'Morrissey', 197426, 2004, 210),
       (1, 'Keep Yourself Alive', 'Queen', 385991, NULL, 235),
       (10, 'Everyday is Like Sunday', 'Morrissey', 160404, 1988, 216);
       """


"""SELECT AVG(streams) AS avg_streams
FROM Songs;

SELECT COUNT(*) AS num_of_songs
FROM Songs;

SELECT COUNT(*) AS num_of_songs
FROM Songs
WHERE artist = 'Morrissey';

SELECT COUNT(trackname) AS num_of_tracknames
FROM Songs;

SELECT COUNT(*) AS num_of_songs,
       COUNT(release_year) AS num_of_years
FROM Songs;

SELECT MIN(length) AS min_length
FROM Songs;

SELECT SUM(streams) AS sum_streams
FROM Songs;

SELECT GROUP_CONCAT(trackname) AS songs
FROM Songs
WHERE id <= 5;

SELECT GROUP_CONCAT(trackname ORDER BY trackname SEPARATOR '; ') AS songs
FROM Songs
WHERE id <= 5;

Примечание 1:
Внутри функций AVG(), COUNT(), SUM() и GROUP_CONCAT() можно использовать ключевое слово DISTINCT, чтобы в итоговых вычислениях участвовали лишь уникальные значения поля:

... AVG(DISTINCT <название поля>)
... COUNT(DISTINCT <название поля>)
... SUM(DISTINCT <название поля>)
... GROUP_CONCAT(DISTINCT <название поля>)

Примечание 2: 
Помимо обычных полей, в качестве аргумента агрегатным функциям можно передавать и вычисляемые поля.

SELECT MAX(length DIV 60) AS max_length_in_mins
FROM Songs;"""


"""Группировки

Давайте рассмотрим еще одну базу данных game_events и попробуем решить следующую задачу: посчитать сумму внутриигровых покупок каждого пользователя.

Скрипт для создания таблицы game_events

CREATE TABLE game_events (
    user_id VARCHAR(32),
    event_name VARCHAR(128),
    level_name VARCHAR(64),
    level_success INT,
    event_date DATE,
    revenue FLOAT
);
INSERT INTO game_events 
(user_id, event_name, level_name, level_success, event_date, revenue) values
('7f0344f8','in_app_purchase',NULL,NULL,'2021-01-10','0.99'),
('7f0344f8','daily_game_events',NULL,NULL,'2021-01-10',NULL),
('7f0344f8','daily_battle_victories',NULL,NULL,'2021-01-10',NULL),
('00aa49ac','level_end','level_01','1','2021-01-13',NULL),
('00aa49ac','level_end','level_02','1','2021-01-13',NULL),
('00aa49ac','level_start','level_01',NULL,'2021-01-13',NULL),
('00aa49ac','level_start','level_03',NULL,'2021-01-14',NULL),
('00aa49ac','level_start','level_02',NULL,'2021-01-13',NULL),
('00aa49ac','in_app_purchase',NULL,NULL,'2021-01-13','2.49'),
('00aa49ac','in_app_purchase',NULL,NULL,'2021-01-14','9.49'),
('00aa49ac','in_app_purchase',NULL,NULL,'2021-01-13','7.49'),
('00aa49ac','in_app_purchase',NULL,NULL,'2021-01-13','9.49'),
('00aa49ac','daily_game_events',NULL,NULL,'2021-01-13',NULL),
('00aa49ac','daily_game_events',NULL,NULL,'2021-01-14',NULL),
('00aa49ac','daily_battle_victories',NULL,NULL,'2021-01-14',NULL),
('00aa49ac','daily_battle_victories',NULL,NULL,'2021-01-13',NULL),
('f5ef9841','level_end','level_02','1','2021-01-16',NULL),
('f5ef9841','level_end','level_03','1','2021-01-16',NULL),
('f5ef9841','level_end','level_04','1','2021-01-16',NULL),
('f5ef9841','level_end','level_01','1','2021-01-15',NULL),
('f5ef9841','level_start','level_03',NULL,'2021-01-16',NULL),
('f5ef9841','level_start','level_04',NULL,'2021-01-16',NULL),
('f5ef9841','level_start','level_01',NULL,'2021-01-15',NULL),
('f5ef9841','level_start','level_02',NULL,'2021-01-16',NULL),
('f5ef9841','level_start','level_02',NULL,'2021-01-15',NULL),
('f5ef9841','app_first_launch',NULL,NULL,'2021-01-15',NULL),
('f5ef9841','in_app_purchase',NULL,NULL,'2021-01-15','7.49'),
('f5ef9841','in_app_purchase',NULL,NULL,'2021-01-15','2.49'),
('f5ef9841','in_app_purchase',NULL,NULL,'2021-01-16','9.49'),
('f5ef9841','daily_game_events',NULL,NULL,'2021-01-16',NULL),
('f5ef9841','daily_game_events',NULL,NULL,'2021-01-15',NULL),
('f5ef9841','daily_battle_victories',NULL,NULL,'2021-01-16',NULL),
('f5ef9841','daily_battle_victories',NULL,NULL,'2021-01-15',NULL),
('13d17d67','level_end','level_05','1','2021-01-13',NULL),
('13d17d67','level_start','level_05',NULL,'2021-01-13',NULL),
('13d17d67','in_app_purchase',NULL,NULL,'2021-01-13','9.476738'),
('13d17d67','in_app_purchase',NULL,NULL,'2021-01-15','7.07912'),
('13d17d67','in_app_purchase',NULL,NULL,'2021-01-13','2.360289'),
('13d17d67','daily_game_events',NULL,NULL,'2021-01-15',NULL),
('13d17d67','daily_game_events',NULL,NULL,'2021-01-17',NULL),
('13d17d67','daily_game_events',NULL,NULL,'2021-01-13',NULL),
('13d17d67','daily_battle_victories',NULL,NULL,'2021-01-17',NULL),
('13d17d67','daily_battle_victories',NULL,NULL,'2021-01-15',NULL),
('13d17d67','daily_battle_victories',NULL,NULL,'2021-01-13',NULL)
;


Если мы напишем запрос SELECT SUM(revenue) FROM game_events, то посчитаем сумму, которая поступила к нам от всех пользователей за все время. Очевидно, это не то, что нам нужно.

Для решения нам необходимо просуммировать покупки каждого пользователя по отдельности. Для этого существует GROUP BY. Выглядит такой запрос следующим образом: 

SELECT user_id, SUM(revenue)
FROM game_events
GROUP BY user_id"""
