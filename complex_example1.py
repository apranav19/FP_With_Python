import functools

"""
	This file contains a tougher example that makes use of map, reduce, and filter
"""

def get_average_height(data):
	""" Returns the average height of a person """
	people_with_heights = list(filter(lambda x: 'height' in x, data))
	sum_of_heights = functools.reduce(lambda a, x: a + x, list(map(lambda x: x['height'], people_with_heights)))*1.0 # we could've easily used sum() instead
	return sum_of_heights/len(people_with_heights)

if __name__ == '__main__':
	people = [{'name': 'Mary', 'height': 160},
    {'name': 'Isla', 'height': 80},
    {'name': 'Sam'}]

	print("Average Height: " + str(get_average_height(people)))

