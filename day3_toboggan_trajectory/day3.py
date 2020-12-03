

def trees_cut(filename, down, right):

	with open(filename, 'r') as file:

		treemap = [list(line.rstrip()) for line in file]
		column = 0
		row = 0 
		tree_count = 0
		last_index = len(treemap[0]) - 1


		while row < len(treemap):

			current_index = treemap[row][column]
			if current_index == '#':
				tree_count += 1
				row += down
				column += right
				if column > last_index:
					column = column - len(treemap[0])

			else:
				row += down
				column += right
				if column > last_index:
					column = column - len(treemap[0])


		return tree_count


# Part 2 below
a = trees_cut('data.txt', 1, 1)
b = trees_cut('data.txt', 1, 3)
c = trees_cut('data.txt', 1, 5)
d = trees_cut('data.txt', 1, 7)
e = trees_cut('data.txt', 2, 1)

print(b)
print(a*b*c*d*e)
