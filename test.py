import pandas
data=[[{'amount': '10', 'category': '20', 'note': '30'}], [{'amount': '10', 'category': '20', 'note': '30'}]]
df=pandas.DataFrame(data)
df.to_csv('csv_data/data.csv')