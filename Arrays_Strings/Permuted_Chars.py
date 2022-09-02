def is_permutation(string1, string2):
    if string1 is None or string2 is None:
        return False
    return sorted(string1) == sorted(string2)

print(is_permutation('abc', 'bca'))

print(is_permutation('Nib', 'bin'))
