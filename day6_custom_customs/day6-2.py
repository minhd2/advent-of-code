

def count_questions(filename):

	unique_questions = dict()
	unique_count = 0
	line_counter = 0

	with open(filename, 'r') as file:

		for line in file:
			if line == '\n':
				for key, value in unique_questions.items():
					if value == line_counter:
						unique_count += 1
					else:
						continue

				unique_questions.clear()
				line_counter = 0 
			else:
				for character in line.rstrip('\n'):
					unique_questions[character] = unique_questions.get(character, 0) + 1
				line_counter += 1
		for key, value in unique_questions.items():
			if value == line_counter:
				unique_count += 1 
			else:
				continue


		return unique_count
print(count_questions('data.txt'))