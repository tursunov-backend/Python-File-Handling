import csv

input_file = 'Input/grades.csv'
   

with open(input_file) as csv_file:
    reader = csv.DictReader(csv_file, fieldnames=['name', 'grade'])
    next(reader)

    max_grade = max(
        reader,
        key = lambda row: row['grade']
    ) 

    print(max_grade)

output_file = 'Output/output21.txt'
output_file_obj = open(output_file, 'w')
output_file_obj.write(str(max_grade)) 
