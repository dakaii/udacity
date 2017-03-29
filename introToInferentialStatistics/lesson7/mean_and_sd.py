import pandas as pd

xl = pd.ExcelFile('Klout scores (Lesson 7).xlsx')
#df = xl.parse(xl.sheet_names[0])
sheet1 = xl.parse(0)
sum = 0
for i in range(len(sheet1)):
    sum += sheet1.iloc[i].real[0]
print(sum)
mean = str(sum/len(sheet1))
print('The mean value is: ' + mean)
