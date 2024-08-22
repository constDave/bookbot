def count_words(file_contents):
    words = file_contents.split()
    return len(words)


def read_file(file_path):
    with open(file_path, "r") as f:
        return f.read()


def sort_on(dict):
    return dict["count"]


def format_report_string(sorted_char_list):
    report_string = ""
    for char in sorted_char_list:
        if char["char"].isalpha():
            report_string += (
                f"The '{char['char']}' character was found {char['count']} times\n"
            )
    return report_string


def count_characters(file_contents):
    words = file_contents.split()
    characters_count = {}
    for word in words:
        word = word.lower()
        for char in word:
            if char in characters_count:
                characters_count[char] += 1
            else:
                characters_count[char] = 1

    # Convert the dictionary to a list of dictionaries
    char_list = [
        {"char": char, "count": count} for char, count in characters_count.items()
    ]
    sorted_char_list = sorted(char_list, key=sort_on, reverse=True)

    return sorted_char_list


def main():
    file_path = "books/frankenstein.txt"
    file_contents = read_file(file_path)
    word_count = count_words(file_contents)

    print("--- Begin report of books/frankenstein.txt --- \n")
    print(f"There are {word_count} words in this file.")
    print(format_report_string(count_characters(file_contents)))
    print("\n")
    print("--- End report ---")


if __name__ == "__main__":
    main()
