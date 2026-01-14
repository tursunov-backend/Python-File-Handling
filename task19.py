import csv

input_file = 'Input/grades.csv'
rows = []

with open(input_file) as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        rows.append(row)
        print(row)

output_file = 'Output/output19.txt'
with open(output_file, 'w') as out:
    for r in rows:
        out.write(f"{r['Name']} - {r['Grade']}\n")
