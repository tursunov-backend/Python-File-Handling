input_file = 'Input/students.txt'
input_file_obj = open(input_file, 'r')

content = input_file_obj.read()
input_file_obj.close()

students = content.split()
count = len(students)

print(count)

output_file = 'Output/output12.txt'
output_file_obj = open(output_file, 'w')
output_file_obj.write(str(count))
output_file_obj.close()
