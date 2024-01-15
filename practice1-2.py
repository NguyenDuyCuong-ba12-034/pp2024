class Student:
    def __init__(self, student_id, name):
        self.id = student_id
        self.name = name

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def show_info(self):
        print(f"ID: {self.id}, Name: {self.name}")

def add_student(ds):
    student_id = input("Input ID of the student: ")
    name = input("Input name of the student: ")
    ds.append(Student(student_id, name))

def update_student_info(ds):
    student_id = input("Input ID of the student you want to update: ")
    for student in ds:
        if student.get_id() == student_id:
            student.set_name(input("Input new name: "))
            student.show_info()

def delete_student(ds):
    student_id = input("Input ID of the student you want to delete: ")
    for student in ds:
        if student.get_id() == student_id:
            ds.remove(student)
            print("Student deleted successfully.")
            break
    else:
        print("No student found with the given ID.")

def show_all_students(ds):
    if len(ds) == 0:
        print("\nNo students in the list. You must add a new student to the list.")
    else:
        print(f"\nInformation of all students. The list has {len(ds)} students:")
        for student in ds:
            student.show_info()

def show_student_by_id(ds):
    student_id = input("Input ID of the student you want to see: ")
    for student in ds:
        if student.get_id() == student_id:
            student.show_info()
            break
    else:
        print("No student found with the given ID.")

def find_student_by_name(ds):
    name = input("Input name of the student you want to find: ")
    for student in ds:
        if student.get_name() == name:
            student.show_info()
            break
    else:
        print("No student found with the given name.")

def show_number_of_students(ds):
    print(f"The list has {len(ds)} students.")

ds = []

while True:
    print('''\n
    0. exit the program 
    1. add a student 
    2. update information of a student 
    3. delete a student
    4. see information of all students
    5. see information of a student by ID
    6. find information of a student by name
    7. the number of students
    ''')
    select = input("Enter your choice: ")

    if select.isdigit():
        select = int(select)
        if select == 0:
            break
        elif select == 1:
            add_student(ds)
        elif select == 2:
            update_student_info(ds)
        elif select == 3:
            delete_student(ds)
        elif select == 4:
            show_all_students(ds)
        elif select == 5:
            show_student_by_id(ds)
        elif select == 6:
            find_student_by_name(ds)
        elif select == 7:
            show_number_of_students(ds)
    else:
        print("You must input a number. Please re-input.")
