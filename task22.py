import csv

input_file = 'Input/grades.csv'
   

with open(input_file) as csv_file:
    reader = csv.DictReader(csv_file, fieldnames=['name', 'grade'])
    next(reader)

    grade_5 = list(filter(
        lambda row: int(row['grade']) == 5,
        reader
    )) 

    count = len(grade_5)

    print('Bahosi 5 bo\'lganlar soni:', count)

output_file = 'Output/output22.txt'
output_file_obj = open(output_file, 'w')
output_file_obj.write(str(count)) 
