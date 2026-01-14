input_file = 'Input/students.txt'
input_file_obj = open(input_file, 'r')

content = input_file_obj.read()
input_file_obj.close()

students = content.split()

idx = students[::-1]  

print(idx)

output_file = 'Output/output14.txt'
output_file_obj = open(output_file, 'w')
output_file_obj.write(' '.join(idx))
output_file_obj.close()
