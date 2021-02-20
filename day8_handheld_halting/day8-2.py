

def calculate_acc(filename):


	actionlist = list()
	jmp_nop_set = set()
	action_set = set()
	acc_value = 0

	with open(filename, 'r') as file:

		for index, action in enumerate(file):
				if action[:3] == 'jmp' or action[:3] == 'nop':
					jmp_nop_set.add(index)

				actionlist.append(action.rstrip())




		for index in jmp_nop_set:

			if complete_game(index, actionlist.copy()) == False:
				continue
			else:
				acc_value = complete_game(index, actionlist.copy())
				break

	return acc_value


def complete_game(jmp_nop_index, actionlist):

	game_on = True
	action_set = set()
	acc = 0
	index = 0

	if actionlist[jmp_nop_index][:3] == 'nop':
		actionlist[jmp_nop_index] = 'jmp' + actionlist[jmp_nop_index][3:]
	elif actionlist[jmp_nop_index][:3] == 'jmp':
		actionlist[jmp_nop_index] = 'nop' + actionlist[jmp_nop_index][3:]

	#print(actionlist)
	while game_on:
			if index in action_set:
				game_on = False
				return False
			elif index == len(actionlist) - 1:
				if actionlist[index][:3] == 'acc':
					if actionlist[index][4] == '-':
						acc -= int(actionlist[index][5:])
					else:
						acc += int(actionlist[index][5:])
				return acc
			elif actionlist[index][:3] == 'nop':
				action_set.add(index)
				index += 1
				continue
			elif actionlist[index][:3] == 'jmp':
				action_set.add(index)
				if actionlist[index][4] == '-':
					index -= int(actionlist[index][5:])
				else:
					index += int(actionlist[index][5:])
			elif actionlist[index][:3] == 'acc':
				action_set.add(index)
				if actionlist[index][4] == '-':
					acc -= int(actionlist[index][5:])
					index += 1
				else:
					acc += int(actionlist[index][5:])
					index += 1



print(calculate_acc('data.txt'))

