from stats import num_of_words, num_of_char_counts, sort_dict_list
import sys

def main():
	if len(sys.argv) < 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)

	text = get_book_text(sys.argv[1])	
	word_count = num_of_words(text)
	char_count = num_of_char_counts(text)
	sorted = sort_dict_list(char_count)

	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {sys.argv[1]}...")
	print("----------- Word Count ----------")
	print(f"Found {word_count} total words")
	print(f"--------- Character Count -------")
	
	for dict in sorted:
		if dict["char"].isalpha():
			print(f"{dict['char']}: {dict['num']}")

	print("============= END ===============")

def get_book_text(fp):
	with open(fp) as f:
		return f.read()	

main()