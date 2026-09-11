import pandas as pd

# Creating a dictionary containing student data
data = {
    'Name': ['Ajay', 'Jack', 'Vinit', 'Salni', 'Neha'],
    'Maths': [78, 67, 88, 82, 99],
    'Comp': [99, 87, 90, 67, 78],
    'Sci': [56, 78, 78, 89, 90],
    'Eng': [98, 89, 78, 76, 54]
}

# Creating a DataFrame
df = pd.DataFrame(data)

# List of subject columns
sub = ['Maths', 'Comp', 'Sci', 'Eng']


# Adding Total and Average columns
mark = df.assign(
    Total=lambda x: x['Maths'] + x['Comp'] + x['Sci'] + x['Eng'],
    Average=lambda x: x[sub].mean(axis=1)
)

# Displaying the complete DataFrame
print(mark)


# Finding the highest marks in Maths
maths_marks = df['Maths'].max()

# Finding the index of the student with highest Maths marks
row_marks = df['Maths'].idxmax()

# Finding the student's name using the index
top_name = df.loc[row_marks, 'Name']


# Finding the lowest marks in Science
sci_marks = df['Sci'].min()

# Finding the index of the student with lowest Science marks
sci_row = df['Sci'].idxmin()

# Finding the student's name
low_name = df.loc[sci_row, 'Name']


# Displaying Maths topper and lowest student in Science
print(
    '\nTopper in Maths:', top_name, '-', maths_marks, 'marks',
    '\nLowest in Science:', low_name, '-', sci_marks, 'marks'
)


# Finding the maximum total marks
max_total = mark['Total'].max()

# Finding the index of the student with maximum total
max_row = mark['Total'].idxmax()

# Finding the topper's name
top_student = mark.loc[max_row, 'Name']


# Finding the minimum total marks
min_total = mark['Total'].min()

# Finding the index of the student with minimum total
min_row = mark['Total'].idxmin()

# Finding the student's name
weak_student = mark.loc[min_row, 'Name']


# Displaying the topper and lowest scorer
print('\nTopper in total marks:', top_student, '-', max_total)
print('Lowest in total marks:', weak_student, '-', min_total)


# Finding the average marks of each subject
print('\nAverage marks subject-wise:\n', mark[sub].mean())

# Finding maximum marks in each subject
print('\nMax marks subject-wise:\n', mark[sub].max())

# Finding minimum marks in each subject
print('\nMin marks subject-wise:\n', mark[sub].min())


# Saving the DataFrame to a CSV file
mark.to_csv('student.csv', index=False)