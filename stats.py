def count_words(text):
        words = text.split()
        return len(words)
def num_characters(text):
	counter = {}
	character_string = text.lower()
	for character in character_string:
		if character not in counter:
			counter[character] = 0
		counter[character] += 1
	return counter
def sort_char_counts(counter):
	items = []
	for char, num in counter.items():
		items.append({"char": char, "num": num})
	def sort_on(d):
		return d["num"] 
	sorted_char = items.sort(key=sort_on, reverse=True)
	return items
