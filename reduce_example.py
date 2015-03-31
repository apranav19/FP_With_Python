import functools
"""
	Code samples that illustrate how the reduce() can be used
	NOTE: Python 2.x users do not need to import functools
"""
def get_sum(data):
	""" Returns the sum of a list of numbers """
	return functools.reduce(lambda a, x: a + x, data)

def get_word_count(data, word):
	""" Returns the total # of occurences of the word supplied. """
	return functools.reduce(lambda a, x: a + x.count(word), data, 0)

if __name__ == '__main__':
	print("Sum of data: " + str(get_sum([5, 3, 10, 17, 4])))
	print("===========")

	sentences = ['Mary read a story to Sam and Isla.',
             'Isla cuddled Sam.',
             'Sam chortled.']

	print("Word count: " + str(get_word_count(sentences, "Sam")))

