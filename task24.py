import csv

input_file = 'Input/grades.csv'

with open(input_file) as f:
    reader = csv.DictReader(f, fieldnames=['name', 'grade'])
    next(reader)
    
    students = []
    for row in reader:
        students.append({
            'name': row['name'],
            'grade': int(row['grade'])
        })

total = sum(student['grade'] for student in students)
average = total / len(students)

print(f'O\'rtacha baho: {average}')
print('\nO\'rtacha bahodan yuqori olganlar:')

high_achievers = []

for student in students:
    if student['grade'] > average:
        print(f'{student['name']}: {student['grade']}')
        high_achievers.append(student)  

output_file = 'Output/output24.txt'

with open(output_file, 'w') as output_file_obj:
    output_file_obj.write(f'O\'rtacha baho: {average}\n\n')
    output_file_obj.write('O\'rtacha bahodan yuqori olganlar:\n')
    
    for student in high_achievers:
        output_file_obj.write(f'{student["name"]}: {student["grade"]}\n')