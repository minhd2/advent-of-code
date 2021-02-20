import re

def shiny_gold_bag_amount(filename, wanted_color):

	bags_with_color = set()
	count = 0
	pattern = re.compile('\d '+wanted_color)
	total_colors = 0

	with open(filename, 'r') as file:

		for line in file:
			if re.search(pattern, line):
				count += 1
				bags_with_color.add(line.split('contain')[0].rstrip('s '))
				total_colors -= 1
			total_colors += 1


		file.seek(0)
		#print(len(bags_with_color))
		print(bags_with_color)
		second_pattern = re.compile('|'.join(bags_with_color))
		#print(second_pattern)
		for line in file:

			before_contain, keyword_contain, after_contain = line.partition('contain')
			if re.search(second_pattern, before_contain):
				#print(before_contain)
				continue
			elif re.search(second_pattern, after_contain):
				print(after_contain)
				print(re.search(second_pattern, after_contain))
				count += 1
				total_colors -= 1

		print(total_colors)
		print(count)





shiny_gold_bag_amount('data.txt', 'shiny gold bag')
#shiny_gold_bag_amount('smol.txt', 'shiny gold bag')