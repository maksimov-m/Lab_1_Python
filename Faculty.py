import copy

class Student(object):
    def __init__(self, FIO: str, age: int, kurs: int, sessions: list):
        self.id = -1
        self.__FIO = FIO
        self.__age = age
        self.__kurs = kurs
        self.__sessions = sessions

    @property
    def FIO(self):
        return self.__FIO

    @property
    def kurs(self):
        return self.__kurs

    @property
    def age(self):
        return self.__age

    @property
    def sessions(self):
        return self.__sessions

    def __del__(self):
        print("Destructor Student")

    def __str__(self):
        return f"Id: {self.id}\nFIO: {self.FIO} \nAge: {self.age} \nKurs: {self.kurs}\n"


class Teacher(object):
    def __init__(self, FIO: str, age: int, themes: list):
        self.id = 0
        self.__FIO = FIO
        self.__age = age
        self.__themes = themes

    @property
    def FIO(self):
        return self.__FIO

    @property
    def themes(self):
        return self.__themes

    @property
    def age(self):
        return self.__age

    def __str__(self):
        return f"Id: {self.id}\nFIO: {self.FIO}\n" \
               f"Age: {self.age}\n" \

    def __del__(self):
        print("Destructor Teacher")


class Faculty(object):

    def __init__(self, name: str, students: list, teachers: list, timetable: dict):
        self.id_students = 0
        self.id_teachers = 0

        self.__name = name

        self.__teachers = teachers
        self.__students = students

        for i in range(len(teachers)):
            self.__teachers[i].id = self.id_teachers
            self.id_teachers += 1

        for i in range(len(students)):
            self.__students[i].id = self.id_students
            self.id_students += 1

        self.__timetable = timetable

    @property
    def name(self):
        return self.__name

    @property
    def teachers(self):
        return self.__teachers

    @property
    def students(self):
        return self.__students

    def print_teachers(self):
        print("Teachers:")
        for i in self.teachers:
            print(i)

    def print_students(self):
        print("Students:")
        for i in self.students:
            print(i)

    def print_timetable(self, kurs: int):
        if 0 > kurs > 3:
            print("Kurs out of range!")
            return
        print(f"Расписание для {kurs} курса:\n")
        timetable = self.__timetable[kurs]
        for i in timetable:
            print(f"{i}")
        print()

    def pay_scholatship(self):
        print("Выплата стипендии: \n")
        tmp = False
        for i in self.students:
            for j in i.sessions:
                if j[1] == 3:
                    tmp = True
            if not tmp:
                print(f"Pay scholarship {i.FIO}\n")
            tmp = False

    def add_student(self, student: Student):
        if self.id_students == 1000:
            print("Out of range!")
            return
        student.id = self.id_students
        self.students.append(student)
        self.id_students += 1

    def add_teacher(self, teacher: Teacher):
        if self.id_teachers == 1000:
            print("Out of range!")
            return
        teacher.id = self.id_teachers
        self.teachers.append(teacher)
        self.id_teachers += 1

    def del_student(self, id: int):
        for i in self.students:
            if i.id == id:
                self.students.remove(i)
                return
        print("Nothing")

    def del_teacher(self, id: int):
        for i in self.teachers:
            if i.id == id:
                self.teachers.remove(i)
                return
        print("Nothing")

    def __str__(self):
        return f"Name: {self.name}\n" \
               f"Count Students: {len(self.students)}\n" \
               f"Count Teachers: {len(self.teachers)}"

    def __del__(self):
        print("Destructor Faculty")
