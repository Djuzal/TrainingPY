

def to_case_string(string):
    list_words = string.split()
    result = []
    for words in list_words:
        list_word = list(words)
        if list_word[0].islower:
            list_word[0] = list_word[0].upper()
        list_word = "".join(list_word)
        result.append(list_word)        
        continue
    return " ".join(result)


print(to_case_string("How can mirrors be real if our eyes aren't real"))