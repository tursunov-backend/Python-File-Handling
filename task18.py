input_file = 'Input/students.txt'
input_file_obj = open(input_file, 'r')

content = input_file_obj.read()
input_file_obj.close()

students = content.split()

ism = input('Ism kiriting: ')

if ism in students:
    result = f"{ism} faylda mavjud"
else:
    result = f"{ism} faylda mavjud emas"

print(result)

output_file = 'Output/output18.txt'
output_file_obj = open(output_file, 'w')
output_file_obj.write(result)
output_file_obj.close()
