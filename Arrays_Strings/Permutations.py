
def perm(word):
    if len(word) == 0:
        return []
    if len(word) == 1:
        return [word]

    result = []
    perms = perm(word[1:])
    select_char = word[0]

    for p in perms:
        for i in range(len(p)+1):
            result.append(p[:i]+select_char+p[i:])
    return result


print(perm('abcd'))