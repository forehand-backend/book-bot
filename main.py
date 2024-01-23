def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    # count_words(text)
    each_char_amount = (count_characters(text))
    char_amount_pairs = pairs_prepare(each_char_amount)
    report(char_amount_pairs)





def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(text):
    count = 0
    for word in text.split():
        count +=1
    print(count)


def count_characters(text):
    characters = {}
    for ch in text:
        if ch.lower() in characters:
            characters[ch.lower()] += 1
        else:
            characters[ch.lower()] = 1
    return characters


def pairs_prepare(characters):
    char_appears = []
    for key in characters:
        if key.isalpha():
            each_char = (key, characters[key])
            char_appears.append(each_char)
    char_appears.sort()
    return char_appears



def report(data):
    for pair in data:
        print(f"The {pair[0]} character was found {pair[1]} times")   



        

    



main()