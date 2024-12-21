from models import Mentor

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    
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

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.get_average_grade()}"
    
    def __eq__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            return self.get_average_grade() == lecturer.get_average_grade()
        else:
            raise TypeError("Нельзя сравнить лектора с 'не лектором'!")
    
    def __lt__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            return self.get_average_grade() < lecturer.get_average_grade()
        else:
            raise TypeError("Нельзя сравнить лектора с 'не лектором'!")
    
    def __rt__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            return self.get_average_grade() > lecturer.get_average_grade()
        else:
            raise TypeError("Нельзя сравнить лектора с 'не лектором'!")