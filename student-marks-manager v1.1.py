students = []

def astd():
    name = input('Enter name: ')

    m = float(input('Math: '))
    s = float(input('Science: '))
    sst = float(input('SST marks: '))
    
    name = name
    marks = [m, s, sst]

    student = (name, marks)
    students.append(student)

    choice = input('Do you want to add more students? (yes/no): ')
    
    if choice.lower() == 'yes':
        astd()
    else:
        print('Finished adding students')


astd()


def calculate_total(marks):
    total = 0
    for mark in marks:
        total += mark
    return total


def avg(marks):
    total = calculate_total(marks)
    average = total / len(marks)
    return average


def show_student_with_marks():
    for student in students:
        name = student[0]
        marks = student[1]

        total = calculate_total(marks)
        student_avg = avg(marks)
            
        print(name, '-->', marks, 'Total marks:', total, 'Average:', student_avg)


show_student_with_marks()
