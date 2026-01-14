input_file = 'Input/numbers.txt'
input_file_obj = open(input_file)
content = input_file_obj.read()

nums = content.split()
nums = list(map(int, nums))

nums = sorted(nums)

print(nums)

output_file = 'Output/output10.txt'
output_file_obj = open(output_file, 'w')
output_file_obj.write(str(nums))


