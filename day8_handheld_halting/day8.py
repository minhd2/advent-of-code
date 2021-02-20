

def calculate_acc(filename):


	acc = 0
	game_on = True
	game_steps = dict()
	index_set = set()
	with open(filename, 'r') as file:

		lines = [line.rstrip() for line in file]

		#print(lines)
		index = 0
		while game_on:
			if index in index_set:
				print(index)
				game_on = False
				break
			elif lines[index][:3] == 'nop':
				index_set.add(index)
				index += 1
				continue
			elif lines[index][:3] == 'jmp':
				index_set.add(index)
				if lines[index][4] == '-':
					index -= int(lines[index][5:])
				else:
					index += int(lines[index][5:])
			elif lines[index][:3] == 'acc':
				index_set.add(index)
				if lines[index][4] == '-':
					acc -= int(lines[index][5:])
					index += 1
				else:
					acc += int(lines[index][5:])
					index += 1

		print(index_set)
		print(acc)





print(calculate_acc('data.txt'))