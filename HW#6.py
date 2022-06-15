class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def lecture_grade(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in lector.courses_attached and course in self.courses_in_progress:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            print("Неверный курс")

    def average_stu_score(course, student_list):
        total = 0
        counter = 0
        for student in student_list:
            if course in student.courses_in_progress:
                student_score = sum(student.grades[course]) / len(student.grades[course])
                total += student_score
                counter += 1
                if counter == 0:
                   print('Отсутствуют студенты, изучающие данный курс')

        print(f'Средний балл студентов по курсу {course} составляет {total/counter}')

    def __str__(self):
        ave_score = 0
        for keys in self.courses_in_progress:
            ave_score += sum(self.grades[keys]) / len (self.grades[keys])
            return f"\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашку:{ave_score}\nКурсы в процессе изучения :{self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}"


    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Сравнение возможно только для cтудентов')
            return
        else:
            ave_stud1 = 0
            ave_stud2 = 0
            for keys in self.courses_in_progress:
                ave_stud1 += sum(self.grades[keys]) / len(self.grades[keys])
            for keys in other.courses_in_progress:
                ave_stud2 += sum(other.grades[keys]) / len(other.grades[keys])
            if ave_stud1 > ave_stud2:
                return f"{self.name} {self.surname} имеет более ВЫСОКУЮ среднюю оценку по д/з чем {other.name} {other.surname}"
            else:
                return f"{self.name} {self.surname} имеет более НИЗКУЮ среднюю оценку по д/з чем {other.name} {other.surname}"


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
    def average_lect_score(course, lector_list):
        total = 0
        counter = 0
        for lector in lector_list:
            if course in lector.courses_attached:
                lector_score = sum(lector.grades[course]) / len(lector.grades[course])
                total += lector_score
                counter += 1
                if counter == 0:
                   print('Отсутствуют лекторы, ведущие данный курс')

        print(f'Средний балл лекторов по курсу {course} составляет {total/counter}')

    def __str__(self):
        ave1 = 0
        for keys in self.courses_attached:
            ave1 += sum(self.grades[keys]) / len(self.grades[keys])
        return f"\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции :{ave1}"

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Сравнение возможно только для лекторов')
            return
        else:
            ave1 = 0
            ave2 = 0
            for keys in self.courses_attached:
                ave1 += sum(self.grades[keys]) / len(self.grades[keys])
            for keys in other.courses_attached:
                ave2 += sum(other.grades[keys]) / len(other.grades[keys])
            if ave1 > ave2:
                return f"{self.name} {self.surname} имеет более ВЫСОКУЮ среднюю оценку по лекциям чем {other.name} {other.surname}"
            elif ave1 < ave2:
                return f"{self.name} {self.surname} имеет более НИЗКУЮ среднюю оценку по лекциям чем {other.name} {other.surname}"
            else:
                return f'{self.name} {self.surname} и {other.name} {other.surname} имеют одинаковую сркднюю оценку'

class Reviewer(Mentor):
    def rate_hw(super, student, course, grade):
        if isinstance(student, Student) and course in super.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"



best_student = Student('Roy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
worst_best_student = Student('Bruce', 'Lee', 'your_gender')
worst_best_student.courses_in_progress += ['Python']

some_lecurer = Lecturer('John', 'Doe')
some_lecurer_1 = Lecturer('Don', 'Dragon')
some_lecurer.courses_attached += ['Python']
some_lecurer_1.courses_attached += ['Python']

best_student.lecture_grade(some_lecurer, 'Python', 3)
best_student.lecture_grade(some_lecurer, 'Python', 5)
best_student.lecture_grade(some_lecurer, 'Python', 10)
best_student.lecture_grade(some_lecurer_1, 'Python', 6)
best_student.lecture_grade(some_lecurer_1, 'Python', 7)
best_student.lecture_grade(some_lecurer_1, 'Python', 8)

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

average_student_score = [best_student, worst_best_student]
average_lectors_score = [some_lecurer, some_lecurer_1]
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(worst_best_student, 'Python', 8)
# print(Student)
print(some_lecurer > some_lecurer_1)
Student.average_stu_score('Python', average_student_score)
Lecturer.average_lect_score('Python', average_lectors_score )