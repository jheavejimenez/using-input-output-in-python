"""
  Implemented using Coleman - Liau formula
  https://en.wikipedia.org/wiki/Coleman%E2%80%93Liau_index

"""


# Declare a variables
# find a word and count that
# find all sentence that have '.' '!' '?'
def main():
    letter = 0
    word = 0
    sentence = 0

    # ask the user to enter a text
    string = input(str("Text: "))

    for elem in range(len(string)):
        if str.isalpha(string[elem]):
            letter += 1
        if elem == 0 and string[elem] != ' ' or elem != len(string) - 1 and \
                string[elem] == ' ' and string[elem + 1] != '':
            word += 1
        if string[elem] in ['.', '?', '!']:
            sentence += 1

    word = float(word)  # convert int to float

    L = (letter / word) * 100  # average the number of letter per 100 words
    S = (sentence / word) * 100  # average number of sentence per 100 words
    index = round(0.0588 * L - 0.296 * S - 15.8)

    if index < 1:
        print("Before Grade 1")
    elif index >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {index}")


if __name__ == '__main__':
    main()
