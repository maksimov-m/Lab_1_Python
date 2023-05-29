import copy

from Faculty import *


students = []

file_students = open("C:\\Users\\Maksim\\Desktop\\Python Lab\\students.txt", "r", encoding="utf-8")

count_students = int(file_students.readline())

for i in range(count_students):
    FIO = file_students.readline().replace("\n","")
    age = int(file_students.readline())
    kurs = int(file_students.readline())

    session = []

    count_themes = int(file_students.readline())

    for j in range(count_themes):
        themes, grade  = file_students.readline().split()
        session.append((themes.replace("\n",""),int(grade)))

    student = Student(FIO, age, kurs, session)
    students.append(student)

file_students.close()

teachers = []
file_teachers = open("C:\\Users\\Maksim\\Desktop\\Python Lab\\teachers.txt", "r", encoding="utf-8")

count_teachers = int(file_teachers.readline())

for i in range(count_teachers):
    FIO = file_teachers.readline().replace("\n","")
    age = int(file_teachers.readline())

    count_themes = int(file_teachers.readline())

    themes = []
    for j in range(count_themes):
        themes.append(file_teachers.readline().replace("\n",""))

    teacher = Teacher(FIO, age, themes)

    teachers.append(teacher)
file_teachers.close()

file_timetable = open("C:\\Users\\Maksim\\Desktop\\Python Lab\\Timetable.txt", "r", encoding="utf-8")

count_kurs = int(file_timetable.readline())

timetable = {}
for i in range(count_kurs):
    kurs = int(file_timetable.readline())

    themes = []
    for j in range(3):
        themes.append(file_timetable.readline().replace("\n", ""))
    timetable[kurs] = themes



##ДЕМОНСТРАЦИОННАЯ ПРОГРАММА

#конструктор
BSU = Faculty("BSU", students, teachers, timetable)

#копирование
BSU_1 = copy.deepcopy(BSU)

print("Timetable: ")
#расписание
BSU_1.print_timetable(1)
BSU_1.print_timetable(2)

print("Scholarship")
#стипендия
BSU_1.pay_scholatship()


#список студентов и учителей
print("Teachers:")
BSU_1.print_teachers()
print("Students:")
BSU_1.print_students()

#удаление добавление
BSU_1.del_student(0)
BSU_1.add_student(Student("Max Max Max", 22, 1, []))
print("Students Update:")
BSU_1.print_students()

print("Teachers Update")
BSU_1.del_teacher(12)
BSU_1.add_teacher(Teacher("SERGO", 33, []))
BSU_1.print_teachers()

#остался без изменений
print("----BSU----")
BSU.print_teachers()
BSU.print_students()