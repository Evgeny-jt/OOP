class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return 'Имя: {}\nФамилия: {}\nСредняя оценка за домашнее задание: {}\nКурсы в процессе изучения: {}\nЗавершенные курсы: {}'.format(
            self.name, self.surname, self.rating, self.courses_in_progress, self.finished_courses)

    def grade_lecturer(self, mentor, course, grade):
        if isinstance(mentor, Lecturer) and course in self.courses_in_progress:
            if course in mentor.grades:
                mentor.grades[course] += [grade]
            else:
                mentor.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_rating(self, student):
        full_grades = []
        for key in student.grades:
            full_grades += student.grades[key]
        self.rating = round(sum(full_grades) / len(full_grades), 1)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.rating}'

    def average_rating(self, mentor):
        full_grades = []
        for key in mentor.grades:
            full_grades += mentor.grades[key]
        self.rating = round(sum(full_grades) / len(full_grades), 1)


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


student_1 = Student('Ruoy', 'Eman', 'your_gender')
student_1.finished_courses += ['Введение в програмирование']
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']

mentor1 = Lecturer('Питер', 'Паркер')
mentor2 = Reviewer('Мери', 'Отсон')
mentor1.courses_attached += ['Python']
mentor2.courses_attached += ['Python']
mentor2.courses_attached += ['Git']

mentor2.rate_hw(student_1, 'Python', 10)
mentor2.rate_hw(student_1, 'Git', 10)
mentor2.rate_hw(student_1, 'Python', 10)
mentor2.rate_hw(student_1, 'Git', 9)
mentor2.rate_hw(student_1, 'Python', 10)
mentor2.rate_hw(student_1, 'Git', 10)
mentor2.rate_hw(student_1, 'Python', 10)

student_1.grade_lecturer(mentor1, 'Python', 10)
student_1.grade_lecturer(mentor1, 'Git', 10)
student_1.grade_lecturer(mentor1, 'Python', 10)
student_1.grade_lecturer(mentor1, 'Git', 10)
student_1.grade_lecturer(mentor1, 'Python', 10)
student_1.grade_lecturer(mentor1, 'Git', 9)
student_1.grade_lecturer(mentor1, 'Python', 10)

mentor1.average_rating(mentor1)
student_1.average_rating(student_1)

print(mentor1)
print(mentor2)
print(student_1)

if student_1.rating:  # > student_2.rating:
    print('Лучший студент', student_1.name, student_1.surname)
else:
    print('Лучший студент')  # , student_2.name, student_2.surname)

if mentor1.rating:  # > student_2.rating:
    print('Лучший лектор', mentor1.name, mentor1.surname)
else:
    print('Лучший лектор')  # , mentor1.name, mentor1.surname)
