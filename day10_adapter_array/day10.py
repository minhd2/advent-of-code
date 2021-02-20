


def find_1_3_jolts(filename):

	adapters = set()

	one_count = 0
	three_count = 1
	with open(filename, 'r') as file:

		for line in file:
			adapters.add(int(line.rstrip()))


		max_jolts = max(adapters)

		start_jolt = 0

		while start_jolt < max_jolts:

			if (start_jolt + 1) in adapters:
				one_count += 1
				start_jolt += 1
				continue
			elif (start_jolt + 3) in adapters:
				three_count += 1
				start_jolt += 3
				continue



		print(one_count, three_count)


	print(max_jolts)
	print(adapters)





find_1_3_jolts('smol.txt')