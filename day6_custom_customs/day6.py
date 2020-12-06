

def count_questions(filename):

	unique_questions = set()
	total_questions = 0 

	with open(filename, 'r') as file:

		for line in file:
			if line == '\n':
				total_questions += len(unique_questions)
				print(unique_questions)
				unique_questions.clear()
			else:
				for character in line.rstrip('\n'):
					unique_questions.add(character)

		total_questions += len(unique_questions)
		return total_questions


print(count_questions('data.txt'))