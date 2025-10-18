import sys
from stats import count_words, num_characters, sort_char_counts

if len(sys.argv) != 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

book_path = sys.argv[1]

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    text = get_book_text(book_path)

    total_words = count_words(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")

    counts = num_characters(text)
    sorted_chars = sort_char_counts(counts)

    for item in sorted_chars:
        ch = item["char"]
        if not ch.isalpha():
            continue
        print(f"{ch}: {item['num']}")

    print("============= END ===============")

if __name__ == "__main__":
    main()
