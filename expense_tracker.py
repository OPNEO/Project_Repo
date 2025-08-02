import pandas
import os
print('WELCOME TO MINI EXPENSE TRACKER')
def user_inputs_records():
    amount = input('Enter amount Spent')
    category = input('Enter category where you spent')
    note = input('Any NOte Vroo')
    return amount,category,note
def append_and_save_record(amount, category, note):
    record = {
        'amount': amount,
        'category': category,
        'note': note
    }
    df = pandas.DataFrame([record])
    file_exists = os.path.exists('csv_data/data.csv')
    df.to_csv('csv_data/data.csv', mode='a', header=not file_exists, index=False)
def view_data():
    df=pandas.read_csv('csv_data/data.csv')
    print("\n🧾 Expense Records:\n")
    print(df)
while True:
    option=int(input('1.Write_Rocords\n2.View_Records:'))
    if option==1:
        amount,category,note=user_inputs_records()
        append_and_save_record(amount,category,note)
    elif option==2:
        view_data()
    else:
        print('Correct Option')
