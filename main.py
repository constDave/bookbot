def count_words(file_contents):
    words = file_contents.split()
    return len(words)


def read_file(file_path):
    with open(file_path, "r") as f:
        return f.read()


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
    return characters_count


def main():
    file_path = "books/frankenstein.txt"
    file_contents = read_file(file_path)
    word_count = count_words(file_contents)
    characters_count = count_characters(file_contents)
    print("--- Begin report of books/frankenstein.txt ---")
    print("Letter occurrences:\n")
    print(characters_count)
    print("\n\n")
    print(f"There are {word_count} words in this file.")


if __name__ == "__main__":
    main()
