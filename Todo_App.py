import os

print('#'*20,'Welcome To TODO TASK','#'*20)
if not os.path.exists('data.txt'):
    open('data.txt', 'w').close()
def read_data():
    with open('data.txt','r') as file1:
        data_list=file1.readlines()
        return data_list
data_list=read_data()

def write_data():
    name=input('Enter Your TODO Task:')
    data_list.append(name+'\n')
    with open('data.txt','w') as file:
        file.writelines(data_list)
    print('Task Added')
def remove_item():
    for i, x in enumerate(data_list, 1):
        print(f"{i}.{x.strip()}")
    number=int(input('Choose Which Task To Remove:'))
    data_list.pop(number-1)
    print(f'{number} Task Removed')
    with open('data.txt','w') as file:
        file.writelines(data_list)
while True:
    option=int(input('Choose option\n1.View_data\n2.Insert_data\n3.Remove_item:'))
    if option==1:
        print('#'*5,'Current TODO Task :','#'*5)
        for i,x in enumerate(data_list,1):
            print(f"{i}.{x.strip()}")
    elif option==2:
        write_data()
    elif option==3:
        remove_item()
    else:
        print('Try Again Choose Correct Option ')
