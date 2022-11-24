import pandas as pd
from turtle import left
import os

data1 = {'Name':['Tom','Joseph', 'Krish', 'John'], 'Age':[20,21,19,18]}
df1 = pd.DataFrame(data1)
df1.set_index('Name')
data2 = {'Name':['Andy','Joseph', 'Krish', 'John'], 'Color':['red', 'yellow', 'blue','green']}
df2 = pd.DataFrame(data2)
df2.set_index('Name')

print( df1)
print( df2)

df3 = pd.merge(df1[['Name','Age']],df2[['Name','Color']], how='inner')
print(df3)

