input_file = 'Input/numbers.txt'

with open(input_file) as input_file_obj:
    content = input_file_obj.read()

nums = content.split()
nums = list(map(int, nums))

print('Sonlar va ularning raqamlari soni:')
for num in nums:
    digit_count = len(str(num))  
    print(f'{num}: {digit_count} xonali')

output_file = 'Output/output09.txt'

with open(output_file, 'w') as output_file_obj:
    for num in nums:
        digit_count = len(str(abs(num)))
        output_file_obj.write(f'{num}: {digit_count} xonali\n')