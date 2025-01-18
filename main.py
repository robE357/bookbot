def char_count(characters):
    char_dict = {}
    for i in characters:
        if i.lower() not in char_dict:
            char_dict[i.lower()] = 1
        else:
            char_dict[i.lower()] += 1
    return char_dict

def get_book_count(book):
    words = book.split()
    return len(words)


def report(book_name,text, char_dict):
    print(f"--- Begin report of {book_name} ---")
    print(f"{get_book_count(text)} words found in the document")
    print()
    for k, v in char_dict.items():
        if k.isalpha():
            print(f"The '{k}' character was found {v} times")
    print("--- End report ---")
    return ""


def main():
    book = "books/frankenstein.txt"
    with open(book) as f:
        file_contents = f.read()
        #print(file_contents)
        #print(get_book_count(file_contents))
        #print(char_count(file_contents))
        print(report("books/frankenstein.txt",file_contents,char_count(file_contents)))
    return ""


print(main())
