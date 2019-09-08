# This function returns true if a given word is an isogram or false otherwise
def is_isogram(word):
    count = 0
    if not isinstance(word, str):
        print("Argument should be a string")
    else:
        for alphabet in "abcdefghijklmnopqrstuvwxyz":
            if (word.count(alphabet) > 1):
                count += 1
        if (count > 0):
            return tuple([word, False])
        else:
            return tuple([word, True])