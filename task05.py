with open('Input/numbers.txt') as f:
    nums = [int(n) for n in f.read().split()]

if nums:
    average = sum(nums) / len(nums)
else:
    average = 0

print(average)

output_file = 'Output/output05.txt'

out = open(output_file, 'w')
out.write(str(average))
out.close()
