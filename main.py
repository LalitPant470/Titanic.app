import pandas as pd
data={
    'Name':['Ram','Hari','Gopal','Sita'],
    'Age':[20,30,40,34],
    'City':['Doti','Dadeldhur','Baitadi','Darchula']

}
df=pd.DataFrame(data)
print(df)
print(type(df))
print(df['Name'])
print(type(df['Name']))