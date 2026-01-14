input_file = 'Input/numbers.txt'
input_file_obj = open(input_file)

content = input_file_obj.read()

nums = content.split()
nums = list(map(int, nums))

result = list(filter(
    lambda num: num % 2 == 0,
    nums
))

print(result)

output_file = 'Output/output04.txt'
output_file_obj = open(output_file, 'w')
output_file_obj.write(str(result))