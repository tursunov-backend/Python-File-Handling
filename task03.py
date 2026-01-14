input_file = 'Input/numbers.txt'
input_file_obj = open(input_file)
content = input_file_obj.read()

numbers = content.split()
max_number = max(numbers, key=lambda num: int(num))
print(int(max_number))

output_file = 'Output/output03.txt'
output_file_obj = open(output_file, 'w')
output_file_obj.write(str(max_number))