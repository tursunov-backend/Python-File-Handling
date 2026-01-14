import csv

input_file = 'Input/grades.csv'

total = 0      
count = 0      

with open(input_file) as csv_file:
    reader = csv.DictReader(csv_file)

    for row in reader:
        grade = int(row['Grade'])  
        total += grade
        count += 1

if count > 0:
    average = total / count
else:
    average = 0

print('O\'rtacha baho:', average)

output_file = 'Output/output20.txt'
output_file_obj = open(output_file, 'w')
output_file_obj.write(str(average))