from string import digits
import re

def shiny_gold_bag_amount(filename, wanted_color):

	bags_with_color = dict()
	
	with open(filename, 'r') as file:

		for line in file:
			main_bag, keyword_contain, after_contain = line.partition('contain')
			bag_contents = after_contain.lstrip(' ').rstrip('\n').split(',')
			#print(bag_contents)
			for item in bag_contents:
				print(item.lstrip(digits+' ').rstrip('s.'))
			
			#bags_with_color[main_bag.rstrip('s ')] = bag_contents
			
	#print(bags_with_color)

	#visited = set()

	#dfs(visited, bags_with_color, wanted_color)


def dfs(visited, graph, node):
	if node not in visited:
		print(node)
		visited.add(node)
		for neighbor in graph[node]:
			dfs(visited, graph, neighbor)

	return visited

shiny_gold_bag_amount('data.txt', 'shiny gold bag')
#shiny_gold_bag_amount('smol.txt', 'shiny gold bag')