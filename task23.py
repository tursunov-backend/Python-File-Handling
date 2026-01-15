import csv 

input_file = 'Input/grades.csv'
with open(input_file) as f:
    reader = csv.DictReader(f, fieldnames=['name', 'grade'])
    next(reader)

    grades = list(map(
        lambda grade: grade['grade'],
        reader
    ))

print(grades)

shown = []

for grade in grades:
    if grade not in shown:
        print(f'Baho {grade}: {grades.count(grade)} marta')
        shown.append(grade)

output_file = 'Output/output23.txt'
output_file_obj = open(output_file, 'w')
output_file_obj.write(str(grades)) 