import sys
from stats import count_words, count_characters, chars_dict_to_sorted_list

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

filepath = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read().lower()
        return file_contents
    
def main():
    file_text = get_book_text(filepath)
    character_count = count_characters(file_text)
    word_count = count_words(file_text)
    chars_sorted_list = chars_dict_to_sorted_list(character_count)
    print_report(filepath, word_count, chars_sorted_list)

def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()
