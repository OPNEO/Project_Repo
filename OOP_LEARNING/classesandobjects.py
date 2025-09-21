class student:
    crs='Python' #It is class level Data member Can be called using claass name

s1=student()
s2=student()
print('Content Of S1 Before Adding Data Members\n',s1.__dict__)
print('Content of s2\n',s2.__dict__)
s1.sno=1
s1.sname='Ramesh'
s1.marks=63.86
print('Content Of S1 After Adding Data Members \n',s1.__dict__)
print(f'Content of Sno\nNo={s1.sno}\nName={s1.sname}\nMarks={s1.marks}\n{student.crs}')