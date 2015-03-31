"""
	Some simple examples that make use of the map function
"""
def get_name_lengths(names):
	""" Returns a list of name lengths """
	return list(map(len, names))

def get_hashed_names(names):
	""" Returns a list of hashed names """
	return list(map(hash, names))


if __name__ == '__main__':
	people = ["Mary", "Isla", "Sam"]
	print("Length of names: " + str(get_name_lengths(people)))
	print("=================")
	print("Hashed Names: " + str(get_hashed_names(people)))
	print("=================")