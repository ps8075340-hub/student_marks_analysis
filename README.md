# student_marks_analysis
Pandas project based on school syllabus. 
import pandas as pd


data = {'Name':['Ajay', 'Jack', 'Vinit', 'Salni', 'Neha'], 'Maths':[78, 67, 88, 82, 99], 'Comp':[99, 87, 90, 67, 78], 'Sci':[56, 78, 78, 89, 90],'Eng':[98, 89, 78, 76, 54]}

df = pd.DataFrame(data)
sub = ['Maths', 'Comp', 'Sci', 'Eng']

# Total marks and Average marks
mark = df.assign(Total = lambda x: x['Maths']+x['Comp']+x['Sci']+x['Eng'], Average = lambda x: x[sub].mean(axis = 1))

print(mark)

# highest marks and lowest marks
maths_marks = df['Maths'].max()
row_marks = df['Maths'].idxmax()
top_name = df.loc[row_marks, 'Name']

sci_marks = df['Sci'].min()
sci_row = df['Sci'].idxmin()
low_name = df.loc[sci_row, 'Name']

print('\n', 'Topper in maths : ', top_name, '-',maths_marks, 'marks', '\n Lower in Science : ', low_name, '-', sci_marks, 'marks')

# max and min in total marks
# Maximum total marks
max_total = mark['Total'].max()
max_row = mark['Total'].idxmax() 
top_student = mark.loc[max_row, 'Name'] 

# Minimum total marks
min_total = mark['Total'].min()
min_row = mark['Total'].idxmin()
weak_student = mark.loc[min_row, 'Name']

print('\nTopper in total marks:', top_student, '-', max_total)
print('Lowest in total marks:', weak_student, '-', min_total)

# Subject wise average marks
print('\nAverage marks in subject wise\n', mark[sub].mean()) 
print('\nMax marks subject wise\n',mark[sub].max())
print('\nMin marks subject wise\n', mark[sub].min())

mark.to_csv('student.csv')


