def compress_string(s1):
    if s1 is None:
        return None
    result = ''
    last_char = ''
    count = 0
    for i in range(len(s1)):
        if s1[i]==last_char:
            count+=1
            if i == len(s1)-1:
                result = result + s1[i] + str(count)
        else:
            if count > 0:
                result = result + last_char + str(count)
            last_char = s1[i]
            count = 1

    if len(result) < len(s1):
        return result
    else:
        return s1

print(compress_string('AAABBCCDD'))