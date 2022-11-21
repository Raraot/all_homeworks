from connect import create_connect
from random import randint, choice
import faker

def create_table(sql):
    with create_connect() as conn:
        if conn is not None:
            try:
                c = conn.cursor()
                c.execute(sql)
                c.close()
                conn.commit()
            except Exception as e:
                print(e)

def generate_fake_peoples(how_many):
    fake_peoples = []  
    fake_data = faker.Faker('uk-UA')
    for _ in range(how_many):
        fake_peoples.append(fake_data.name().replace('пані ', '').replace('пан ', ''))
    return fake_peoples

if __name__ == '__main__':
    teachers = generate_fake_peoples(3)
    students = generate_fake_peoples(12)
    groups = {101: 'first', 102: 'second', 103: 'third'}
    lessons = {201: 'Теоретична механіка', 202: 'Аеродинаміка', 203: 'Англійська мова', 204: 'Опір матеріалів', 205: 'Історія України'}
    lessons_and_teachers = {201: ['Теоретична механіка', 301], 202: ['Аеродинаміка', 302], 203: ['Англійська мова', 303], 204: ['Опір матеріалів', 301], 205: ['Історія України', 303]}
    dates_of_grade = ['2022-09-21', '2022-10-19', '2022-10-25', '2022-11-10', '2022-10-15']



    # TEACHERS TABLE ##########################################
    sql_teachers = '''CREATE TABLE IF NOT EXISTS teachers (
        id SERIAL PRIMARY KEY,
        name_teacher VARCHAR(130));'''
    create_table(sql_teachers)
    print("Створено таблицю вчителів...")
    
    sql_insert_teachers ="INSERT INTO teachers (id, name_teacher) VALUES(%s, %s)"
    with create_connect() as conn:
        if conn is not None:
            c = conn.cursor()
            id_t = 301
            for teacher in teachers:
                c.execute(sql_insert_teachers, (id_t, teacher))
                id_t +=1
            c.close()
            conn.commit()
    print("Заповнено таблицю вчителів...\n")


    # GROUPS TABLE --kgroupsss-- ##########################################
    sql_groups = '''CREATE TABLE IF NOT EXISTS kgroupsss (
        id SERIAL PRIMARY KEY,
        name_group VARCHAR(130));'''
    create_table(sql_groups)
    print("Створено таблицю груп...")
    
    sql_insert_groups ="INSERT INTO kgroupsss (id, name_group) VALUES(%s, %s)"
    with create_connect() as conn:
        if conn is not None:
            c = conn.cursor()
            for k, v in groups.items():
                c.execute(sql_insert_groups, (k, v))
            c.close()
            conn.commit()
    print("Заповнено таблицю груп...\n")

    # STUDENTS TABLE ##########################################
    sql_students = '''CREATE TABLE IF NOT EXISTS students (
        id SERIAL PRIMARY KEY, 
        name_student VARCHAR(130), 
        id_group INT,
        FOREIGN KEY (id_group) REFERENCES kgroupsss (id)
            ON DELETE SET NULL
            ON UPDATE CASCADE);'''
    create_table(sql_students)
    print("Створено таблицю студентів...")

    sql_insert_students ="INSERT INTO students (id, name_student, id_group) VALUES(%s, %s, %s)"
    with create_connect() as conn:
        if conn is not None:
            c = conn.cursor()
            id_s = 4001
            for student in students:
                c.execute(sql_insert_students, (id_s, student, randint(list(groups.keys())[0],list(groups.keys())[-1])))
                id_s +=1
            c.close()
            conn.commit()
    print("Заповнено таблицю студентів...\n")


    # LESSONS (SUBJECTS) TABLE ##########################################
    sql_lessons = '''CREATE TABLE IF NOT EXISTS lessons (
        id SERIAL PRIMARY KEY,
        name_lessons VARCHAR(130),
        teacher_id INT,
        FOREIGN KEY (teacher_id) REFERENCES teachers (id)
            ON DELETE SET NULL
            ON UPDATE CASCADE);'''
    create_table(sql_lessons)
    print("Створено таблицю предметів...")
    
    sql_insert_lessons ="INSERT INTO lessons (id, name_lessons, teacher_id) VALUES(%s, %s, %s)"
    with create_connect() as conn:
        if conn is not None:
            c = conn.cursor()
            for k, v in lessons.items():
                teacher_id = lessons_and_teachers[k][1]
                c.execute(sql_insert_lessons, (k, v, teacher_id))
            c.close()
            conn.commit()
    print("Заповнено таблицю предметів...\n")


    # GRADEBOOK (ЖУРНАЛ УСПІШНОСТІ) TABLE ##########################################
    sql_gradebook = '''CREATE TABLE IF NOT EXISTS gradebook (
        id SERIAL PRIMARY KEY,
        student_id INT,
        lesson_id INT,
        teacher_id INT,
        date_of_grade DATE,
        grade INT,
        FOREIGN KEY (student_id) REFERENCES students (id),
        FOREIGN KEY (lesson_id) REFERENCES lessons (id)
          ON DELETE SET NULL
          ON UPDATE CASCADE);'''

    create_table(sql_gradebook)
    print("Створено таблицю GRADEBOOK...")
    

    sql_insert_gradebook ="INSERT INTO gradebook (id, student_id, lesson_id, teacher_id, date_of_grade, grade) VALUES(%s, %s, %s, %s, %s, %s)"
    with create_connect() as conn:
        if conn is not None:
            c = conn.cursor()
            for i in range(501,599):
                student_id = randint(1,len(students))+4000
                lesson_id = randint(201, 205)
                teacher_id = lessons_and_teachers[k][1]
                date_of_grade = dates_of_grade[randint(0,4)]
                grade = randint(2,12)
                c.execute(sql_insert_gradebook, (i, student_id, lesson_id, teacher_id, date_of_grade, grade))
            c.close()
            conn.commit()
    print("Заповнено таблицю GRADEBOOK...\n")






