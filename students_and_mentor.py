class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.rating = 0

    def __str__(self):
        return 'Имя: {}\nФамилия: {}\nСредняя оценка за домашнее задание: {}\nКурсы в процессе изучения: {}\nЗавершенные курсы: {}'.format(
            self.name, self.surname, self.rating, self.courses_in_progress, self.finished_courses)

    def __gt__(self, other):
        return self.rating > other.rating

    def __eq__(self, other):
        return self.rating == other.rating

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
        self.rating = 0

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.rating}'

    def __gt__(self, other):
        return self.rating > other.rating

    def __eq__(self, other):
        return self.rating == other.rating

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


def average_rating_courses(students, courses):
    average_rating = {}
    for course in courses:
        all_rating_cource = []
        for student in students:
            all_rating_cource += student.grades[course]
        average_rating[course] = round(sum(all_rating_cource) / len(all_rating_cource), 1)
    return average_rating

def average_rating_lecturers(lecturers, courses):
    average_rating = {}
    for course in courses:
        all_rating_lecturer = []
        for lecturer in lecturers:
            all_rating_lecturer += lecturer.grades[course]
        average_rating[course] = round(sum(all_rating_lecturer) / len(all_rating_lecturer), 1)
    return average_rating

student_1 = Student('Ruoy', 'Eman', 'Man')
student_1.finished_courses += ['Введение в програмирование']
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']

student_2 = Student('Kevin', 'Feige', 'Man')
student_2.finished_courses += ['Введение в програмирование']
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Git']

mentor1 = Lecturer('Питер', 'Паркер')
mentor1.courses_attached += ['Python']
mentor1.courses_attached += ['Git']

mentor2 = Lecturer('Гарри', 'Озборн')
mentor2.courses_attached += ['Python']
mentor2.courses_attached += ['Git']

mentor3 = Reviewer('Мери', 'Отсон')
mentor3.courses_attached += ['Python']
mentor3.courses_attached += ['Git']

mentor4 = Reviewer('Фелиция', 'Харди')
mentor4.courses_attached += ['Python']
mentor4.courses_attached += ['Git']

students = [student_1, student_2]
lecturers = [mentor1, mentor2]
courses = ['Python', 'Git']

mentor3.rate_hw(student_1, 'Python', 10)
mentor3.rate_hw(student_1, 'Git', 10)
mentor3.rate_hw(student_1, 'Python', 10)
mentor3.rate_hw(student_1, 'Git', 9)
mentor3.rate_hw(student_1, 'Python', 9)
mentor3.rate_hw(student_1, 'Git', 10)
mentor3.rate_hw(student_1, 'Python', 10)

mentor3.rate_hw(student_2, 'Python', 10)
mentor3.rate_hw(student_2, 'Git', 9)
mentor3.rate_hw(student_2, 'Python', 9)
mentor3.rate_hw(student_2, 'Git', 9)
mentor3.rate_hw(student_2, 'Python', 10)
mentor3.rate_hw(student_2, 'Git', 9)
mentor3.rate_hw(student_2, 'Python', 10)

mentor4.rate_hw(student_1, 'Python', 10)
mentor4.rate_hw(student_1, 'Git', 10)
mentor4.rate_hw(student_1, 'Python', 10)
mentor4.rate_hw(student_1, 'Git', 9)
mentor4.rate_hw(student_1, 'Python', 10)
mentor4.rate_hw(student_1, 'Git', 10)
mentor4.rate_hw(student_1, 'Python', 10)

mentor4.rate_hw(student_2, 'Python', 10)
mentor4.rate_hw(student_2, 'Git', 9)
mentor4.rate_hw(student_2, 'Python', 10)
mentor4.rate_hw(student_2, 'Git', 9)
mentor4.rate_hw(student_2, 'Python', 10)
mentor4.rate_hw(student_2, 'Git', 9)
mentor4.rate_hw(student_2, 'Python', 10)

student_1.grade_lecturer(mentor1, 'Python', 10)
student_1.grade_lecturer(mentor1, 'Git', 9)
student_1.grade_lecturer(mentor1, 'Python', 10)
student_1.grade_lecturer(mentor1, 'Git', 9)
student_1.grade_lecturer(mentor1, 'Python', 10)
student_1.grade_lecturer(mentor1, 'Git', 9)
student_1.grade_lecturer(mentor1, 'Python', 10)

student_1.grade_lecturer(mentor2, 'Python', 10)
student_1.grade_lecturer(mentor2, 'Git', 8)
student_1.grade_lecturer(mentor2, 'Python', 10)
student_1.grade_lecturer(mentor2, 'Git', 8)
student_1.grade_lecturer(mentor2, 'Python', 9)
student_1.grade_lecturer(mentor2, 'Git', 8)
student_1.grade_lecturer(mentor2, 'Python', 10)

student_2.grade_lecturer(mentor1, 'Python', 10)
student_2.grade_lecturer(mentor1, 'Git', 9)
student_2.grade_lecturer(mentor1, 'Python', 9)
student_2.grade_lecturer(mentor1, 'Git', 9)
student_2.grade_lecturer(mentor1, 'Python', 10)
student_2.grade_lecturer(mentor1, 'Git', 10)
student_2.grade_lecturer(mentor1, 'Python', 10)

student_2.grade_lecturer(mentor2, 'Python', 10)
student_2.grade_lecturer(mentor2, 'Git', 8)
student_2.grade_lecturer(mentor2, 'Python', 9)
student_2.grade_lecturer(mentor2, 'Git', 8)
student_2.grade_lecturer(mentor2, 'Python', 9)
student_2.grade_lecturer(mentor2, 'Git', 8)
student_2.grade_lecturer(mentor2, 'Python', 9)

mentor1.average_rating(mentor1)
mentor2.average_rating(mentor2)
student_1.average_rating(student_1)
student_2.average_rating(student_2)

print(mentor1)
print(mentor2)
print(mentor3)
print(mentor4)
print(student_1)
print(student_2)

if student_1 == student_2:
    print(student_1.name, student_1.surname, student_2.name, student_2.surname, 'Одинакого хороши')
elif student_1 > student_2:
    print('Лучший студент', student_1.name, student_1.surname)
else:
    print('Лучший студент', student_2.name, student_2.surname)

if mentor1 == mentor2:
    print(mentor1.name, mentor1.surname, mentor2.name, mentor2.surname, 'Одинакого хороши')
elif mentor1 > mentor2:
    print('Лучший лектор', mentor1.name, mentor1.surname)
else:
    print('Лучший лектор', mentor2.name, mentor2.surname)

print('Средняя оценка всех студентов в рамках курсов: ', average_rating_courses(students, courses))
print('Средняя оценка всех лекторов в рамка курсов', average_rating_lecturers(lecturers, courses))