from models import *

def main():
    ### Создаем объекты и наполняем данными
    student_1 = Student("Aleksandr", "Zaripov", "male")
    student_1.courses_in_progress.append("ООП и работа с API")
    student_1.finished_courses.append("Основы языка программирования Python")
    student_1.finished_courses.append("Git - система контроля версий")

    student_2 = Student("Irina", "Zaripova", "female")
    student_2.courses_in_progress.append("ООП и работа с API")
    student_2.courses_in_progress.append("Git - система контроля версий")
    student_2.finished_courses.append("Основы языка программирования Python")
    
    lecturer_1 = Lecturer("Ivan", "Ivanov")
    lecturer_1.courses_attached.append("Основы языка программирования Python")
    lecturer_1.courses_attached.append("ООП и работа с API")

    lecturer_2 = Lecturer("Petr", "Petrov")
    lecturer_2.courses_attached.append("Git - система контроля версий")

    reviewer_1 = Reviewer("Semen", "Semenov")
    reviewer_1.courses_attached.append("Основы языка программирования Python")
    reviewer_1.courses_attached.append("ООП и работа с API")
    
    reviewer_2 = Reviewer("Oleg", "Olegov")
    reviewer_2.courses_attached.append("Git - система контроля версий")

    ### Студенты оценивают лекторов
    rate_lectures(student_1, student_2, lecturer_1, lecturer_2)

    ### Ревьюеры оценивают студентов 
    rate_homeworks(student_1, student_2, reviewer_1, reviewer_2)

    ### Выводим на экран инфо о студентах, лекторах, ревьюерах, средних баллов за ДЗ и за проведенные лекции
    print_results(student_1, student_2, lecturer_1, lecturer_2, reviewer_1, reviewer_2)


def rate_lectures(student_1, student_2, lecturer_1, lecturer_2):
    student_1.rate_lecture(lecturer_1, "Основы языка программирования Python", 9)
    student_1.rate_lecture(lecturer_2, "Git - система контроля версий", 4)
    student_1.rate_lecture(lecturer_1, "ООП и работа с API", 7)
    #Должно выкинуть исключение, так как лектор не читал курс
    #student_1.rate_lecture(lecturer_2, "ООП и работа с API", 7)                     

    student_2.rate_lecture(lecturer_1, "Основы языка программирования Python", 5)
    student_2.rate_lecture(lecturer_2, "Git - система контроля версий", 6)
    student_2.rate_lecture(lecturer_1, "ООП и работа с API", 1)

def rate_homeworks(student_1, student_2, reviewer_1, reviewer_2):
    reviewer_1.rate_hw(student_1, "Основы языка программирования Python", 10)
    reviewer_1.rate_hw(student_1, "ООП и работа с API", 6)
    reviewer_2.rate_hw(student_1, "Git - система контроля версий", 2)

    reviewer_1.rate_hw(student_2, "Основы языка программирования Python", 8)
    reviewer_1.rate_hw(student_2, "ООП и работа с API", 4)
    reviewer_2.rate_hw(student_2, "Git - система контроля версий", 3)

def print_results(student_1: Student, student_2: Student, lecturer_1: Lecturer, lecturer_2: Lecturer, reviewer_1: Reviewer, reviewer_2: Reviewer):
    print(student_1)
    print()
    print(student_2)
    print()
    print(lecturer_1)
    print()
    print(lecturer_2)
    print()
    print(reviewer_1)
    print()
    print(reviewer_2)
    print()
    print(f"Средняя оценка за домашнее задание: {get_average_grade_for_homework([student_1, student_2], 'Основы языка программирования Python')}")
    print(f"Средняя оценка за лекции: {get_average_grade_for_lecture([lecturer_1, lecturer_2], 'ООП и работа с API')}")
    print()
    print(lecturer_1 == lecturer_2)
    print(student_1 > student_2)

def get_average_grade_for_homework(students: list, course: str):
    total_grade = 0
    grades_count = 0  

    for student in students:
        if isinstance(student, Student): 
            if course in student.grades: 
                total_grade += sum(student.grades[course]) 
                grades_count += 1 

    if grades_count > 0:
        return total_grade / grades_count 
    else:
        return 0

def get_average_grade_for_lecture(lecturers: list, course: str):
    total_grade = 0
    grades_count = 0  

    for lecturer in lecturers:
        if isinstance(lecturer, Lecturer): 
            if course in lecturer.courses_attached: 
                total_grade += sum(lecturer.grades[course]) 
            grades_count += len(lecturer.grades.get(course, [])) 

    if grades_count > 0:
        return total_grade / grades_count 
    else:
        return 0

if __name__ == "__main__":
    main()

