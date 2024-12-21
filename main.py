from models import Student, Mentor

def main():
    student = Student("Alexandr", "Zaripov", "male")
    mentor = Mentor("Ivan", "Ivanov")

    print(f"{student.name}")
    print(f"{mentor.name}")

if __name__ == "__main__":
    main()

