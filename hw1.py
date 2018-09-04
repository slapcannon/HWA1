#import pandas for dataframe manipulation

import pandas as pd

#open file in folder

df=pd.read_csv('originaldata.csv')

#use the transform function to flip the table

T=df.T

#break data down into one line

f = T.melt()

#write to a file

f.to_csv('divorcerateslong.csv')

print(f)

