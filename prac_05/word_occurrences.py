def main():
    text = input("Text: ")
    words = text.split()

    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0)
    sorted_words = sorted(word_counts.keys())
    max_word_length = max(len(word) for word in sorted_words)


    for word in sorted_words:
        print(f"{word:{max_word_length}} : {word_counts[word]}")


if __name__ == "__main__":
    main()