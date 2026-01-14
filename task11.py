input_file = 'Input/students.txt'
input_file_obj = open(input_file)
content = input_file_obj.read()

students = content.split()
students = list(map(
    lambda student: student,
    students
))
print(students) 

output_file = 'Output/output11.txt'
output_file_obj = open(output_file, 'w')
output_file_obj.write(str(students))