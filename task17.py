input_file = 'Input/students.txt'
output_file = 'Output/output17.txt'

pattern = input('pattern: ')

with open(input_file) as file:
    names = file.readlines()

result = filter(
    lambda name: name.startswith(pattern),
    names
)

with open(output_file, 'w') as file:
    file.writelines(result)


