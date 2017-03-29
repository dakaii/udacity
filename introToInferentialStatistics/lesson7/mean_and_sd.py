import pandas as pd
import math

xl = pd.ExcelFile('Klout scores (Lesson 7).xlsx')
df = xl.parse(xl.sheet_names[0])
print('pandas calculates the mean value to be: ' + str(df.mean()))
print('pandas calculates the standard deviation to be: ' + str(df.std()))
sheet1 = xl.parse(0)
sum = 0
for i in range(len(sheet1)):
    sum += sheet1.iloc[i].real[0]
mean = sum/len(sheet1)
print('The mean value is: ' + str(mean))

#----
sum_of_deviation_squared = 0 
for i in range(len(sheet1)):
    sum_of_deviation_squared += (mean-sheet1.iloc[i].real[0])**2 
std = math.sqrt(sum_of_deviation_squared/len(sheet1))
print('The standard deviation is: ' + str(std))
