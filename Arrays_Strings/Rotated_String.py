from traceback import print_tb


def is_substring(s1, s2):
    return s1 in s2

def is_rotation(s1, s2):
    if s1 is None or s2 is None:
        return False
    if len(s1) != len(s2):
        return False
    return is_substring(s1, s2+s2)

print(is_rotation('foobarbaz', 'barbazfoo'))