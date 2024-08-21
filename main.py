def count_words(file_contents):
    words = file_contents.split()
    return len(words)


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        print(f"There are {word_count} words in this file.")


if __name__ == "__main__":
    main()
