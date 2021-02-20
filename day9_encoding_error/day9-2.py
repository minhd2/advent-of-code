

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
				number_error = int(numbers[current_index])
				break

		current_list = list()
		print(number_error)
		for current_index in range(len(numbers)-1):
			copy_error = number_error
			copy_error -= int(numbers[current_index])
			current_list.append(int(numbers[current_index]))

			for next_index in range(current_index+1, len(numbers)):
				current_list.append(int(numbers[next_index]))
				copy_error -= int(numbers[next_index])
				#print(copy_error)
				if copy_error == 0:
					solution_list = current_list.copy()
				elif copy_error < 0:
					break
			if copy_error == 0:
				break
			current_list.clear()

		sorted_solution = sorted(solution_list)
		print(sorted_solution[0]+sorted_solution[-1])





print(find_encoding_error('data.txt', 25))

