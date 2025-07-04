def count_words(text):
    return len(text.split())

def count_characters(book_text):
    word_count = {}

    for character in book_text:
        if character.lower() in word_count:
            word_count[character.lower()] += 1
        else:
            word_count[character.lower()] = 1
    
    return word_count

def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
