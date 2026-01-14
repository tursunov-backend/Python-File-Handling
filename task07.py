input_file = 'Input/numbers.txt'
input_file_obj = open(input_file, 'r')

content = input_file_obj.read()
input_file_obj.close()

nums = content.split()
squares = list(map(
    lambda num: int(num) ** 2,
    nums
))

print(squares)

output_file = 'Output/output07.txt'
output_file_obj = open(output_file, 'w')

output_file_obj.write(' '.join(map(str, squares)))
output_file_obj.close()
