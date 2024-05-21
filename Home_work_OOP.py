# Задание № 1. Наследование
# ... у нас есть класс преподавателей и класс студентов.

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.all_grades = []
        self.aver_grade = 0

    def average_grade(self):
        self.all_grades = []
        for course in self.grades:
            self.all_grades.extend(self.grades[course])
        self.aver_grade = round(sum(self.all_grades) / len(self.all_grades),2)
        return


# Реализуйте метод выставления оценок лекторам у класса Student (оценки
# по 10-балльной шкале, хранятся в атрибуте-словаре у Lecturer, в котором ключи – названия курсов,
# а значения – списки оценок). Лектор при этом должен быть закреплен за тем курсом, на который записан студент.

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer):
            if course in lecturer.courses_attached:
                if course in self.courses_in_progress or course in self.finished_courses:
                    if course in lecturer.grades:
#                        print('проверено, добавляем')
                        lecturer.grades[course] += [grade]
#                        print(lecturer.grades)
                    else:
#                        print('проверено, создаем')
                        lecturer.grades[course] = [grade]
#                        print(lecturer.grades)
                else:
                    print('Студент может оценивать только те курсы, на которых учился или учился')
                    return 'Ошибка'                        
            else:
                print('Можно оценивать только те курсы, за которыми лектор закреплен')
                return 'Ошибка'
        else:
            print('Можно оценивать только лектора')
            return 'Ошибка'
        lecturer.average_grade(course)
        return


# Задание № 3. Полиморфизм и магические методы
# Перегрузите магический метод __str__ у всех классов.
# А у студентов так:
#
# print(some_student)
# Имя: Ruoy
# Фамилия: Eman
# Средняя оценка за домашние задания: 9.9
# Курсы в процессе изучения: Python, Git
# Завершенные курсы: Введение в программирование

    def __str__(self):
        return f"""
Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {self.aver_grade}
Курсы в процессе изучения: {', '.join(self.courses_in_progress)}
Завершенные курсы: {', '.join(self.finished_courses)}
"""

# Реализуйте возможность сравнивать (через операторы сравнения) между собой лекторов по средней
# оценке за лекции и студентов по средней оценке за домашние задания.

    def __eq__(self, other_student):
        return self.aver_grade == other_student.aver_grade
    
    def __lt__(self, other_student):
        return self.aver_grade < other_student.aver_grade


# теперь класс Mentor должен стать родительским классом,
# имя, фамилия и список закрепленных курсов логично реализовать на уровне родительского класса.

class Mentor:
    def __init__(self, name, surname, title=''):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.title = title


# от него нужно реализовать наследование классов Lecturer (лекторы) ... могут ... Получать оценки за лекции от студентов
# Реализуйте метод выставления оценок лекторам у класса Student

class Lecturer(Mentor):
    def __init__(self, name, surname, title):
        super().__init__(name, surname, title)
        self.courses_attached = []
        self.grades = {}
        self.aver_grades = {}
        self.total_aver_grade = 0

    def average_grade(self, course):
        self.aver_grades[course] = round(sum(self.grades[course]) / len(self.grades[course]),2)
        self.total_aver_grade = round(sum(self.aver_grades.values()) / len(self.aver_grades),2)
        return


# Задание № 3. Полиморфизм и магические методы
# Перегрузите магический метод __str__ у всех классов.
# У лекторов:

# print(some_lecturer)
# Имя: Some
# Фамилия: Buddy
# Средняя оценка за лекции: 9.9

    def __str__(self):
        return f"""
Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {self.total_aver_grade}"""


# Реализуйте возможность сравнивать (через операторы сравнения) между собой лекторов по средней
# оценке за лекции и студентов по средней оценке за домашние задания.

    def __eq__(self, other_lectorer):
        return self.total_aver_grade == other_lectorer.total_aver_grade
    def __lt__(self, other_lectorer):
        return self.total_aver_grade < other_lectorer.total_aver_grade


# и Reviewer (эксперты, проверяющие домашние задания).
# возможность выставлять студентам оценки за домашние задания могут только Reviewer (реализуйте такой метод)!

class Reviewer(Mentor):
    def __init__(self, name, surname, title):
        super().__init__(name, surname, title)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
            student.average_grade()
        else:
            return 'Ошибка'


# Задание № 3. Полиморфизм и магические методы
# Перегрузите магический метод __str__ у всех классов.
# У проверяющих он должен выводить информацию в следующем виде:
#
# print(some_reviewer)
# Имя: Some
# Фамилия: Buddy

    def __str__(self):
        return f"""
Имя: {self.name}
Фамилия: {self.surname}"""
    

# Реализуйте возможность сравнивать (через операторы сравнения) между собой лекторов по средней оценке за лекции

def compare_lecturer (lecturer1, lecturer2):
    if lecturer1.title == 'Лектор' and lecturer2.title == 'Лектор':
        if lecturer1.total_aver_grade > lecturer2.total_aver_grade:
            print(f"Рейтинг лектора {lecturer1.name} {lecturer1.surname} выше рейтинга лектора {lecturer2.name} {lecturer2.surname}.")
        elif lecturer1.total_aver_grade < lecturer2.total_aver_grade:
            print(f"Рейтинг лектора {lecturer2.name} {lecturer2.surname} выше рейтинга лектора {lecturer1.name} {lecturer1.surname}.")
        else:
            print(f"Рейтинги лекторов {lecturer1.name} {lecturer1.surname} и {lecturer2.name} {lecturer2.surname} равны.")
    else:
        print('Сравнивать можно только лекторов')
    return
# Реализуйте возможность сравнивать (через операторы сравнения) между собой студентов по средней оценке за домашние задания.

def compare_student (student1, student2):
    if student1.aver_grade > student2.aver_grade:
        print(f"Рейтинг студента {student1.name} {student1.surname} выше рейтинга студента {student2.name} {student2.surname}.")
    elif student1.aver_grade < student2.aver_grade:
        print(f"Рейтинг студента {student2.name} {student2.surname} выше рейтинга студента {student1.name} {student1.surname}.")
    else:
        print(f"Рейтинги студентов {student1.name} {student1.surname} и {student2.name} {student2.surname} равны.")


# Задание № 4. Полевые испытания
# Создайте по 2 экземпляра каждого класса, вызовите все созданные методы, а также реализуйте две функции:
# - для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса (в качестве
# аргументов принимаем список студентов и название курса);
# - для подсчета средней оценки за лекции всех лекторов в рамках курса (в качестве аргумента принимаем список
# лекторов и название курса).

student_1 = Student('Иван', 'Иванов', 'man')
student_1.finished_courses += ['Основы']
student_1.finished_courses += ['Git']
student_1.courses_in_progress += ['OOP']
student_1.courses_in_progress += ['API']
student_2 = Student('Марья', 'Сидорова', 'woman')
student_2.finished_courses += ['Основы']
student_2.finished_courses += ['Git']
student_2.courses_in_progress += ['OOP']
student_2.courses_in_progress += ['API']
student_3 = Student('Петр', 'Попов', 'man')
student_3.finished_courses += ['Основы']
student_3.finished_courses += ['Git']
student_3.courses_in_progress += ['OOP']
student_3.courses_in_progress += ['API']

lecturer_1 = Lecturer('Петр', 'Петров', 'Лектор')
lecturer_1.courses_attached += ['OOP']
lecturer_2 = Lecturer('Сидор', 'Сидоров', 'Лектор')
lecturer_2.courses_attached += ['API']
lecturer_3 = Lecturer('Игнат', 'Козлов', 'Лектор')
lecturer_3.courses_attached += ['API']
lecturer_4 = Lecturer('Олег', 'Лебедев', 'Лектор')
lecturer_4.courses_attached += ['API']

reviewer_1 = Reviewer('Михаил', 'Михайлов','Эксперт')
reviewer_1.courses_attached += ['OOP']
reviewer_2 = Reviewer('Степан', 'Степанов','Эксперт')
reviewer_2.courses_attached += ['API']

print(reviewer_1, reviewer_2)

reviewer_1.rate_hw(student_1, 'OOP', 10)
reviewer_1.rate_hw(student_1, 'OOP', 9)
reviewer_1.rate_hw(student_2, 'OOP', 8)
reviewer_1.rate_hw(student_2, 'OOP', 7)
reviewer_2.rate_hw(student_1, 'API', 7)
reviewer_2.rate_hw(student_1, 'API', 8)
reviewer_2.rate_hw(student_2, 'API', 9)
reviewer_2.rate_hw(student_2, 'API', 10)
reviewer_1.rate_hw(student_3, 'OOP', 7)
reviewer_1.rate_hw(student_3, 'OOP', 8)
reviewer_2.rate_hw(student_3, 'API', 9)
reviewer_2.rate_hw(student_3, 'API', 8)

print(student_1, student_2, student_3)

student_1.rate_lect(lecturer_1, 'OOP', 10)
student_1.rate_lect(lecturer_2, 'API', 9)
student_1.rate_lect(lecturer_3, 'API', 10)
student_1.rate_lect(lecturer_4, 'API', 9)
student_2.rate_lect(lecturer_1, 'OOP', 9)
student_2.rate_lect(lecturer_2, 'API', 10)
student_2.rate_lect(lecturer_3, 'API', 10)
student_2.rate_lect(lecturer_4, 'API', 9)
student_3.rate_lect(lecturer_1, 'OOP', 10)
student_3.rate_lect(lecturer_2, 'API', 10)
student_3.rate_lect(lecturer_3, 'API', 10)
student_3.rate_lect(lecturer_4, 'API', 9)

print(lecturer_1, lecturer_2, lecturer_3, lecturer_4)


# - для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса (в качестве
# аргументов принимаем список студентов и название курса);
# - для подсчета средней оценки за лекции всех лекторов в рамках курса (в качестве аргумента принимаем список
# лекторов и название курса).


list_of_students =[student_1, student_2, student_3]
course = 'API'
list_of_lecturers = [lecturer_1, lecturer_2, lecturer_3, lecturer_4]

def aver_hw_rate_in_course(students, course):
    all_grade_hw_course = []
    aver_grade_hw_course = 0
    for student in students:
        if course in student.courses_in_progress:
            all_grade_hw_course.extend(student.grades[course])
        else:
            continue
    aver_grade_hw_course = round(sum(all_grade_hw_course) / len(all_grade_hw_course),2)
    return aver_grade_hw_course 

a_hw_r_c = aver_hw_rate_in_course(list_of_students,course)

print(f'Средняя оценка домашних заданий по курсу {course} : {a_hw_r_c}')

def aver_lect_rate_in_course(lecturers, course):
    all_grade_lect_course = []
    aver_grade_lect_course = 0
    for lecturer in lecturers:
        if course in lecturer.courses_attached:
            all_grade_lect_course.extend(lecturer.grades[course])
        else:
            continue
    aver_grade_lect_course = round(sum(all_grade_lect_course) / len(all_grade_lect_course),2)
    return aver_grade_lect_course

a_l_r_c = aver_lect_rate_in_course(list_of_lecturers, course)

print(f'Средняя оценка лекций по курсу {course} : {a_l_r_c}')

print (lecturer_1 == lecturer_2)
print (lecturer_1 < lecturer_2)
print (lecturer_1 > lecturer_2)

print (lecturer_3 == lecturer_4)
print (lecturer_3 < lecturer_4)
print (lecturer_3 > lecturer_4)

print(student_1 == student_2)
print(student_1 < student_2)
print(student_1 > student_2)

print(student_1 == student_3)
print(student_1 < student_3)
print(student_1 > student_3)
