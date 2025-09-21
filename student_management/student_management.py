import sqlite3
conn=sqlite3.connect('students.db')
c=conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS students
             (id INTEGER PRIMARY KEY, name TEXT, email TEXT, age INTEGER, course TEXT)''')
conn.commit()

def view_students():
    c.execute('SELECT * FROM students')
    rows = c.fetchall()
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}, Age: {row[3]}, Course: {row[4]}")
def add_student():
    print('Student Management System ')
    student_info={}
    id=int(input('Enter Student ID: '))
    name=input('Enter Student Name: ')
    email=input('Enter Student Email: ')
    age=int(input('Enter Student Age: '))
    course=input('Enter Student Course: ')
    student_info['ID']=id
    student_info['Name']=name
    student_info['Email']=email
    student_info['Age']=age
    student_info['Course']=course
    return student_info  
def search_student(student_id):
    c.execute('SELECT * FROM students WHERE id=?', (student_id,))
    row = c.fetchone()
    if row:
        print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}, Age: {row[3]}, Course: {row[4]}")
    else:
        print("Student not found.")
def delete_student(student_id):
    c.execute('DELETE FROM students WHERE id=?', (student_id,))
    conn.commit()
    print("Student deleted if existed.")
def update_student(student_id, field, new_value):
    if field not in ['name', 'email', 'age', 'course']:
        print("Invalid field.")
        return
    c.execute(f'UPDATE students SET {field}=? WHERE id=?', (new_value, student_id))
    conn.commit()
    print("Student updated if existed.")
def close_connection():
    conn.close()    
while True:
    choice=input('1. Add Student\n2. View Students\n3. Search Student\n4. Delete Student\n5. Update Student\nEnter your choice: ')
    if choice == '1':
        student_info = add_student()
        c.execute("INSERT INTO students (id, name, email, age, course) VALUES (?, ?, ?, ?, ?)",
              (student_info['ID'], student_info['Name'], student_info['Email'], student_info['Age'], student_info['Course']))
        conn.commit()
    elif choice == '2':
        view_students()
    elif choice == '3':
        student_id = int(input("Enter Student ID to search: "))
        search_student(student_id)
    elif choice == '4':
        student_id = int(input("Enter Student ID to delete: "))
        delete_student(student_id)
    elif choice == '5':
        student_id = int(input("Enter Student ID to update: "))
        field = input("Enter field to update (name, email, age, course): ")
        new_value = input("Enter new value: ")
        if field == 'age':
            new_value = int(new_value)
        update_student(student_id, field, new_value)
    else:
        print("Invalid choice.")                    