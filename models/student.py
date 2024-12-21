class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def rate_lecture(self, lecturer, course, grade):
        from models import Lecturer
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and (course in self.courses_in_progress or course in self.finished_courses):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            raise Exception("У студента и лектора курсы не совпадают")
    
    def get_average_grade(self):
        grades_sum = 0
        grades_counter = 0
        
        for grades in self.grades.values():
            for grade in grades:
                grades_sum += grade
            grades_counter += len(grades)
        
        if grades_counter == 0:
            return "Нет выставленных оценок" 
        
        return grades_sum / grades_counter

    def get_courses_in_progress(self):
        return ", ".join(self.courses_in_progress)
    
    def get_finished_courses(self):
        return ", ".join(self.finished_courses)
        
    def __str__(self):
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за домашние задания: {self.get_average_grade()}\n"
            f"Курсы в процессе изучения: {self.get_courses_in_progress()}\n"
            f"Завершенные курсы: {self.get_finished_courses()}"
        )
    
    def __eq__(self, student):
        if isinstance(student, Student):
            return self.get_average_grade() == student.get_average_grade()
        else:
            raise TypeError("Нельзя сравнить студента с 'не студентом'!")
    
    def __lt__(self, student):
        if isinstance(student, Student):
            return self.get_average_grade() < student.get_average_grade()
        else:
            raise TypeError("Нельзя сравнить студента с 'не студентом'!")
    
    def __rt__(self, student):
        if isinstance(student, Student):
            return self.get_average_grade() > student.get_average_grade()
        else:
            raise TypeError("Нельзя сравнить студента с 'не студентом'!")