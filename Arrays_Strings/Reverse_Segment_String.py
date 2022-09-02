def reverse_words(sentence):
    arr = sentence.split(' ')
    arr.reverse()
    output = ' '
    sentence = output.join(arr)
    return sentence   

print(reverse_words("Hello World"))


def string_segmentation(s, arr):
    for i in arr:
        if i in s:
            s.replace(i, '')
        else:
            return "Cannot segment"
    return "Can segment"

print(string_segmentation('applepenapple',["apple","pen","Pen"]))
