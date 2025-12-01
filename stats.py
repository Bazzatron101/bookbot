def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    book = {}

    for char in text:
        c = char.lower()
        if c in book:
            book[c] += 1

        else:
            book[c] = 1

    book = sort_list(book)

    return book

def sort_list(book):
    sorted_list = []

    for ch in book:
        sorted_list.append({"char": ch, "num": book[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(d):
    return d["num"]
