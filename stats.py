def num_of_words(text):
	words = text.split()

	return len(words)

def num_of_char_counts(text):
	counts = {}
	lower_str = text.lower()

	for char in lower_str:
		if char not in counts:
			counts[char] = 1
		else:
			counts[char] += 1

	return counts

def sort_dict_list(dict):
	sorted_list = []

	for key in dict:
		sorted_list.append({"char": key, "num": dict[key]})
	sorted_list.sort(reverse=True, key=sort_on)

	return sorted_list


def sort_on(dict):
    return dict["num"]