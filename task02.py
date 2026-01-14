input_file = 'Input/numbers.txt'
input_file_opj = open(input_file)
content = input_file_opj.read()

numbers = content.split()
numbers = list(map(
    lambda num: int(num),
    numbers
))
result = sum(numbers)
print(numbers)

output_file = 'Output/output02.txt'
output_file_obj = open(output_file, 'w')
output_file_obj.write(str(result))