students=[]
def add_students():
    name=input('enter name:')
    roll=int(input('enter roll number:'))

    m=float(input('maths marks='))
    sst=float(input('sst marks='))
    s=float(input('science marks='))

    marks=[m,sst,s]
    student=(name,marks)
    students.append(student)

def show_students():
    for student in students:
        print(student)
add_students()
show_students()
