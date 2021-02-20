

def find_encoding_error(filename, preamble):

	numbers = list()
	sum_set = set()

	with open(filename, 'r') as file:

		for number in file:
			numbers.append(number.rstrip())


		starting_index = preamble

		for current_index in range(starting_index, len(numbers)):
			last = preamble
			for previous_index in reversed(range(1, preamble+1)):
				for next_previous_index in reversed(range(1, last)):
					sums = int(numbers[current_index - previous_index]) + int(numbers[current_index - next_previous_index])
					sum_set.add(sums)

			#print(sum_set)
			if int(numbers[current_index]) in sum_set:
				sum_set.clear()
			else:
				return numbers[current_index]
		



print(find_encoding_error('data.txt', 25))

