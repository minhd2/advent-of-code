

def adapters_creation(filename):

	adapters = [0]
	split_adapters = list()
	total_paths = 1

	with open(filename, 'r') as file:

		for line in file:
			adapters.append(int(line.rstrip()))

		adapters.sort()
		start = 0
		for i in range(len(adapters) - 1):
			if (adapters[i + 1] - adapters[i]) == 3:
				split_adapters.append(adapters[start:i+1])
				start = i+1

		split_adapters.append(adapters[start:])
		print(split_adapters)
		for j in split_adapters:
			total_paths *= valid_adapters(j, int(min(j)))

		print(total_paths)


# recursive function
def valid_adapters(adapters, start=0):

	new_starts = list()
	count = 0
	for i in adapters:
		if (i - start) <= 0:
			continue
		elif (i - start) <= 3:
			new_starts.append(i)
	if len(new_starts) == 0:
		return 1 
	else:
		for j in new_starts:
			count += valid_adapters(adapters ,j)
	
	return count

#print(adapters_creation('data.txt'))


