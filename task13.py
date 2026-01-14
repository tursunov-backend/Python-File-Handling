input_file = 'Input/students.txt'
input_file_obj = open(input_file, 'r')

content = input_file_obj.read()
input_file_obj.close()

students = content.split()

students.sort()   

print(students)

output_file = 'Output/output13.txt'
output_file_obj = open(output_file, 'w')
output_file_obj.write(' '.join(students))
output_file_obj.close()
