-- 5 студентів із найбільшим середнім балом з усіх предметів.
SELECT s.name_student as top_5_students, round(avg(g.grade), 2) AS avg_grade
FROM gradebook as g
LEFT JOIN students as s ON s.id = g.student_id
GROUP BY s.name_student, s.id
ORDER BY avg_grade DESC
LIMIT 5;


-- 1 студент із найвищим середнім балом з одного предмета. (враховуючі всі предмети)
SELECT  s.name_student as top_1_student, l.name_lessons, round(avg(g.grade), 2) AS avg_grade
FROM gradebook as g
LEFT JOIN students as s ON s.id = g.student_id
LEFT JOIN lessons as l ON l.id = g.lesson_id
--WHERE l.id = 202 -- Якщо розкоментувати, то можна виводити по ID предмету(дисципліни) (201-205) 
GROUP BY s.name_student, l.name_lessons
ORDER BY avg_grade DESC
LIMIT 1;


-- Середній бал в кожній групі по кожному предмету.
SELECT gr.name_group , l.name_lessons, round(avg(g.grade), 2) AS avg_grade_by_subject
FROM gradebook as g
LEFT JOIN students as s ON s.id = g.student_id
LEFT JOIN lessons as l ON l.id = g.lesson_id
LEFT JOIN kgroupsss as gr ON gr.id = s.id_group
--WHERE l.id = 202 -- Якщо розкоментувати, то можна виводити по ID предмету(дисципліни) (201-205) 
GROUP BY gr.name_group, l.name_lessons
ORDER BY gr.name_group ASC
LIMIT 12;


-- Середній бал у потоці.
SELECT round(avg(g.grade), 2) AS avg_grade_potok
FROM gradebook as g;


-- Які курси читає викладач.
SELECT t.id as id_teacher, t.name_teacher, l.name_lessons
FROM teachers as t 
LEFT JOIN lessons as l ON l.teacher_id = t.id
--WHERE t.id = 302 -- Якщо розкоментувати, то можна виводити по ID вчителя(301-305) 
GROUP BY t.id, t.name_teacher, l.name_lessons
ORDER BY l.name_lessons  ASC;


-- Список студентів у (кожній) групі.
SELECT k.name_group, s.name_student 
FROM kgroupsss as k
LEFT JOIN students as s ON s.id_group = k.id
--WHERE k.id = 102 -- Якщо розкоментувати, то можна виводити по ID групи(101-103) 
ORDER BY k.name_group  ASC;


-- Оцінки студентів у групі з предмета. (Сгрупована по групам таблиця зі всіма оцінками всіх учнів.)
SELECT k.id as id_group, k.name_group, s.name_student, l.name_lessons, g.grade, g.date_of_grade
FROM gradebook as g 
LEFT JOIN students as s ON s.id = g.student_id
LEFT JOIN lessons as l ON  l.id = g.lesson_id
LEFT JOIN kgroupsss as k ON k.id = s.id_group
--WHERE k.id  = 102 -- Якщо розкоментувати - можна виводити по ID групи(101-103) 
GROUP BY k.id, k.name_group, s.name_student, l.name_lessons, g.grade, g.date_of_grade
ORDER BY k.name_group ASC;


-- Оцінки студентів у групі з предмета на останньому занятті.
SELECT k.id as id_group, k.name_group, s.name_student, l.name_lessons, g.grade, g.date_of_grade
FROM gradebook as g 
LEFT JOIN students as s ON g.student_id = s.id
LEFT JOIN lessons as l ON g.lesson_id = l.id 
LEFT JOIN kgroupsss as k ON k.id = s.id_group
WHERE g.date_of_grade = (SELECT g2.date_of_grade
    FROM gradebook as g2
    ORDER BY g2.date_of_grade DESC
    LIMIT 1) -- AND k.id  = 102 -- <- Якщо розкоментувати - можна виводити по ID групи(101-103) 
GROUP BY k.id, k.name_group, s.name_student, l.name_lessons, g.grade, g.date_of_grade;


-- Список курсів, які відвідує (кожен) студент. Виводить список по кожному студенту список предметів.
SELECT s.id as id_student, s.name_student , l.name_lessons 
FROM students as s 
LEFT JOIN gradebook as g ON g.student_id = s.id 
LEFT JOIN lessons as l ON g.lesson_id = l.id 
--WHERE s.id = 4005 -- Якщо розкоментувати - можна виводити по ID студента (4001 і більше)
GROUP BY s.id, s.name_student , l.name_lessons 
ORDER BY s.id  ASC;


-- Список курсів, які студенту читає викладач.
SELECT s.id as id_student, s.name_student, t.id as teacher_id, t.name_teacher, l.name_lessons 
FROM gradebook as g
LEFT JOIN students as s ON g.student_id = s.id
LEFT JOIN lessons as l ON g.lesson_id = l.id
LEFT JOIN teachers as t ON t.id = l.teacher_id  
WHERE s.id = 4005 AND t.id = 301 -- можна вводити ID студента (4001 і більше) та ID викладача (301-303)
-- Якщо закоментувати верхню строку WHERE - виведе всю таблицю курсів, які студентам читають викладачі.
GROUP BY t.id, t.name_teacher, s.id, s.name_student, l.name_lessons
ORDER BY s.name_student  ASC;


-- Середній бал, який викладач ставить студенту.
SELECT DISTINCT s.id as id_student, s.name_student, t.id as teachers, t.name_teacher, round(avg(g.grade), 2) AS avg_grade
FROM gradebook as g
LEFT JOIN students as s ON s.id = g.student_id
LEFT JOIN lessons as l ON  l.id = g.lesson_id
LEFT JOIN teachers as t ON t.id = l.teacher_id
WHERE s.id = 4005 AND t.id = 301 -- можна вводити ID студента (4001 і більше) та ID викладача (301-303)
-- Якщо закоментувати всю верхню строку з WHERE - виведе всю таблицю по всім викладачам і студентам.
GROUP BY s.id, s.name_student, t.id, t.name_teacher
ORDER BY s.id  ASC;


-- Середній бал, який ставить викладач.
SELECT DISTINCT t.id as teachers, t.name_teacher, round(avg(g.grade), 2) AS avg_grade
FROM gradebook as g
LEFT JOIN lessons as l ON  l.id = g.lesson_id
LEFT JOIN teachers as t ON t.id = l.teacher_id
WHERE t.id = 301 -- можна вводити ID викладача (301-303)
-- Якщо закоментувати всю верхню строку з WHERE - виведе всю таблицю по всім викладачам.
GROUP BY t.id, t.name_teacher
ORDER BY t.id  ASC;
