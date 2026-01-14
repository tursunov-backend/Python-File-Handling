input_file = 'Input/students.txt'
input_file_obj = open(input_file, 'r')

content = input_file_obj.read()
input_file_obj.close()

students = content.split()

result = list(filter(
    lambda student: len(student) > 5,
    students
))

output_file = 'Output/output16.txt'
output_file_obj = open(output_file, 'w')
output_file_obj.write(str(result))
output_file_obj.close()
