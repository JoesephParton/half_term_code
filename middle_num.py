def middle_word(word):
    middle = len(word) // 2
    if len(word) % 2 == 1:
        return word[middle]
    else:
        return "No Middle Number"

print(middle_word(input("word: ")))
