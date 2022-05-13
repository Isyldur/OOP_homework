from random import randint


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return (f'''Имя: {self.name} 
Фамилия: {self.surname}
Средняя оценка за домашние задания: {self.avg():.1f}
Курсы в процессе изучения: {', '.join(self.courses_in_progress)}
Заверщенные курсы: {', '.join(self.finished_courses)}
                '''
                )

    def __lt__(self, other):
        if isinstance(other, Student) and other.avg() > 0:
            return self.avg() < other.avg()

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def avg(self):
        count = 0
        total = 0
        for grade in self.grades.values():
            total += (sum(grade) / len(grade))
            count += 1
        if count > 0:
            return total / count
        else:
            return

    def rate_lector(self, lector, course, grade):
        if isinstance(grade, int) and (0 < grade <= 10):
            if isinstance(lector,
                          Lecturer) and course in self.courses_in_progress and course in lector.courses_attached:
                if course in lector.grades:
                    lector.grades[course] += [grade]
                else:
                    lector.grades[course] = [grade]
            else:
                return 'Error'
        else:
            return "Invalid grade"


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super(Lecturer, self).__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return (f'''Имя: {self.name} 
Фамилия: {self.surname}
Средняя оценка за лекции: {Student.avg(self):.1f}
                '''
                )

    def __lt__(self, other):
        if isinstance(other, Lecturer) and Student.avg(other) > 0:
            return Student.avg(self) < Student.avg(other)


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(grade, int) and (0 < grade <= 10):
            if isinstance(student,
                          Student) and course in self.courses_attached and course in student.courses_in_progress:
                if course in student.grades:
                    student.grades[course] += [grade]
                else:
                    student.grades[course] = [grade]
            else:
                return 'Ошибка'
        else:
            return 'Invalid grade'

    def __str__(self):
        return (f'''Имя: {self.name} 
Фамилия: {self.surname}''')


dron = Student('Андрей', 'Сергеев', 'Мужской')
dron.add_courses('Java')
dron.courses_in_progress.append('Git')
dron.courses_in_progress.append('Python')

kate = Student('Катерина', 'Александрова', 'Женский')
kate.add_courses('Git')
kate.courses_in_progress.append('Python')
kate.courses_in_progress.append('Web-design')

ivan = Lecturer('Иван', 'Борисов')
ivan.courses_attached.append('Python')
ivan.courses_attached.append('Java')
ivan.courses_attached.append('Git')

shprot = Lecturer('Денис', 'Килька')
shprot.courses_attached.append('Web-design')
shprot.courses_attached.append('Git')

jendos = Reviewer('Евгений', 'Каленый')
jendos.courses_attached.append('Python')
jendos.courses_attached.append('Web-design')
jendos.courses_attached.append('Git')

alenka = Reviewer('Алена', 'Филиппова')
alenka.courses_attached.append('Python')
alenka.courses_attached.append('Java')


def grade_all():
    for i in range(5):
        dron.rate_lector(ivan, 'Python', randint(1, 10))
        dron.rate_lector(ivan, 'Git', randint(1, 10))
        dron.rate_lector(shprot, 'Git', randint(1, 10))

        kate.rate_lector(ivan, 'Python', randint(1, 10))
        kate.rate_lector(shprot, 'Web-design', randint(1, 10))

        alenka.rate_hw(dron, 'Python', randint(1, 10))
        alenka.rate_hw(kate, 'Python', randint(1, 10))

        jendos.rate_hw(kate, 'Python', randint(1, 10))
        jendos.rate_hw(kate, 'Web-design', randint(1, 10))
        jendos.rate_hw(dron, 'Python', randint(1, 10))
        jendos.rate_hw(dron, 'Git', randint(1, 10))


def course_avg(students, course):
    total = 0
    count = 0
    for student in students:
        if course in student.grades:
            total += sum(student.grades[course])/len(student.grades[course])
            count += 1
        else:
            continue
    if count != 0:
        return total/count
    else:
        return 'Error'


def lector_course_avg(lectors, course):
    total = 0
    count = 0
    for lector in lectors:
        if course in lector.grades:
            total += sum(lector.grades[course])/len(lector.grades[course])
            count += 1
        else:
            continue
    if count != 0:
        return total/count
    else:
        return 'Error'


grade_all()
print('Студенты:')
print(dron)
print()
print(kate)
print()
print(f'''Сравниваем наших студентов:
Катя круче? {kate > dron} 
или Андрей {kate < dron}
''')
print()
print("Наши лекторы:")
print(ivan)
print()
print(shprot)
print()
print(f'''Кто тут лучший лектор:
Ваня? {ivan > shprot}
Денис? {ivan < shprot}
''')
print()
print("Ну и напоследок наши эксперты:")
print(jendos)
print()
print(alenka)
print()
print(f'Средняя оценка студентов по курсу Python: {course_avg([dron, kate], "Python"):.1f}')
print(f'Средняя оценка преподавателей курса Git: {lector_course_avg([ivan, shprot], "Git"):.1f}')