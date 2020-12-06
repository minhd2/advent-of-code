

def highest_seat(filename):


	seat_list = list()

	with open(filename, 'r') as file:


		for line in file:
			highest_row = 127
			lowest_row = 0
			highest_column = 7
			lowest_column = 0 
			column = 0
			for character in line.rstrip("\n"):
				if character == 'F':
					highest_row = (highest_row + lowest_row) // 2
				elif character == 'B':
					lowest_row = (highest_row + lowest_row) // 2 + 1
				elif character == 'L':
					highest_column = (highest_column + lowest_column) // 2
				elif character == 'R':
					lowest_column = (highest_column + lowest_column) // 2 + 1


			if character[-1] == 'L':
				column = highest_column
			elif character[-1] == 'R':
				column = lowest_column

			current_seat =  (highest_row * 8) + column

			seat_list.append(current_seat)

		sorted_seats = sorted(seat_list)
		for i in range(len(sorted_seats) - 1):
			if (sorted_seats[i] + 1) != sorted_seats[i+1]:
				return sorted_seats[i] + 1



print(highest_seat('data.txt'))