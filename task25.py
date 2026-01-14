import csv

input_file = 'Input/grades.csv'
with open(input_file) as csv.file:
    reader = csv.DictReader(csv.file, fieldnames=['name', 'grade'])
    next(reader)

    grade_5 = list(filter(
        lambda row: int(row['grade']) == 5,
        reader 
    ))

    print(grade_5)

output_file = 'Output/output25.txt'
output_file_obj = open(output_file, 'w')
output_file_obj.write(str(grade_5)) 