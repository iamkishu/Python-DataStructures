def has_unique_chars(word):
    if word is None:
        return False
    return len(set(word)) == len(word)


print(has_unique_chars('Kishu'))
print(has_unique_chars('Bala'))