class Student:
    objects_list = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.objects_list.append(self)

    def add_finished_courses(self, course_name):
        self.finished_courses.extend(course_name)

    def avg(self, personal_grades):
        return round(sum([sum(rates) / len(rates) for rates in personal_grades.values()]) / len(personal_grades), 1)

    def __lt__(self, other_person):
        if not isinstance(other_person, Student):
            print('Ошибка')
            return
        else:
            return self.avg(self.grades) < other_person.avg(other_person.grades)

    def __str__(self):
        return (f'Имя: {self.name}'
                f'\nФамилия: {self.surname}'
                f'\nСредняя оценка за домашние задания: {self.avg(self.grades)}'
                f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}'
                f'\nЗавершенные курсы: {", ".join(self.finished_courses)}')

    def rate_lecturer(self, lecturer, course, marks):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course].extend(marks)
            else:
                lecturer.grades[course] = marks
        else:
            print('Ошибка')
        return


class Mentor:
    objects_list = []

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.objects_list.append(self)


class Lecturer(Mentor):
    grades = {}
    objects_list = []

    def avg(self, personal_grades):
        return round(sum([sum(rates) / len(rates) for rates in personal_grades.values()]) / len(personal_grades), 1)

    def __str__(self):
        return (f'Имя: {self.name}'
                f'\nФамилия: {self.surname}'
                f'\nСредняя оценка за лекции: {self.avg(self.grades)}')

    def __lt__(self, other_person):
        if not isinstance(other_person, Lecturer):
            print('Ошибка')
            return
        else:
            return self.avg(self.grades) < other_person.avg(other_person.grades)


class Reviewer(Mentor):
    objects_list = []

    def rate_student(self, student, course, marks):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].extens(marks)
            else:
                student.grades[course] = marks
        else:
            print('Ошибка')
        return

    def __str__(self):
        return (f'Имя: {self.name}'
                f'\nФамилия: {self.surname}')


def average_marks(persons, subject):
    marks = []
    for person in persons:
        # [print(mark) for subj, mark in person.grades.items() if subj == subject]
        marks.extend([sum(mark) / len(mark) for subj, mark in person.grades.items() if subj == subject])
    return round(sum(marks) / len(marks), 1)


# ------------------------------------------------------------------------------------------------------------------
student_1 = Student('Bob', 'Thornton', 'Male')
student_2 = Student('Catherine', 'Parkinson', 'Female')
lecturer_1 = Lecturer('Peter', 'Gregory')
lecturer_2 = Lecturer('Gavin', 'Belson')
reviewer_1 = Reviewer('Tanya', 'Kane')
reviewer_2 = Reviewer('Jack', 'Daniels')

student_1.courses_in_progress.extend(['Math', 'Chemistry', 'Literature', 'Chinese'])
student_2.courses_in_progress.extend(['Math', 'Chemistry', 'Literature', 'Chinese'])
lecturer_1.courses_attached.extend(['Math', 'Chemistry'])
lecturer_2.courses_attached.extend(['Literature', 'Chinese'])
reviewer_1.courses_attached.extend(['Math', 'Chemistry'])
reviewer_2.courses_attached.extend(['Literature', 'Chinese'])

student_1.add_finished_courses(['Physics', 'Geometry'])
student_2.add_finished_courses(['Logistics', 'English poetry'])

[reviewer_1.rate_student(student_1, course, grade) for course, grade in (['Math', [5, 8, 10]], ['Chemistry', [6]])]
[reviewer_2.rate_student(student_1, course, grade) for course, grade in (['Literature', [8]], ['Chinese', [2]])]
[reviewer_1.rate_student(student_2, course, grade) for course, grade in (['Math', [4, 3, 5]], ['Chemistry', [3]])]
[reviewer_2.rate_student(student_2, course, grade) for course, grade in (['Literature', [8]], ['Chinese', [9]])]

[student_1.rate_lecturer(lecturer_1, course, grade) for course, grade in (['Math', [9, 5, 8]], ['Chemistry', [8]])]
[student_1.rate_lecturer(lecturer_2, course, grade) for course, grade in (['Literature', [6, 10]], ['Chinese', [2]])]
[student_2.rate_lecturer(lecturer_1, course, grade) for course, grade in (['Math', [6, 9]], ['Chemistry', [4, 7]])]
[student_2.rate_lecturer(lecturer_2, course, grade) for course, grade in (['Literature', [9]], ['Chinese', [9]])]

print('Студенты:')
[print(person, '\n') for person in Student.objects_list]

print('Преподаватели')
[print(person, '\n') for person in Lecturer.objects_list]

print('Проверяющие:')
[print(person, '\n') for person in Reviewer.objects_list]

if student_1 < student_2:
    print(f'Средние оценки у {student_1.name} {student_1.surname} хуже чем у {student_2.name} {student_2.surname}')
else:
    print(f'Средние оценки у {student_1.name} {student_1.surname} лучше чем у {student_2.name} {student_2.surname} или такие же.')

if lecturer_1 < lecturer_2:
    print(
        f'Средние оценки у {lecturer_1.name} {lecturer_1.surname} хуже чем у {lecturer_2.name} {lecturer_2.surname}\n')
else:
    print(
        f'Средние оценки у {lecturer_1.name} {lecturer_1.surname} лучше чем у {lecturer_2.name} {lecturer_2.surname} или такие же.\n')

print(f'Средняя оценка студентов по математике {average_marks(Student.objects_list, "Math")}')
print(f'Средняя оценка лекторов по математике {average_marks(Lecturer.objects_list, "Math")}')
