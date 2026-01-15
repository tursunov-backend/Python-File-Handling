input_file = 'Input/students.txt'
input_file_obj = open(input_file)
content = input_file_obj.read()
input_file_obj.close()

student = content.split()

for name in student:
    print(f'{name}: {len(name)}')

print(student)

output_file = 'Output/output15.txt'
output_file_obj = open(output_file, 'w')
output_file_obj.write(str(student))  
output_file_obj.close()