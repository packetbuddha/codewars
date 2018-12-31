#!/usr/bin/env python

def contain_all_rots(strng, arr):

    def get_rot(strng, i):
        if i > 1:
            rot = []
            rot = list(strng[1:])
            rot.append(strng[0])
            strng = ''.join(rot)

        return strng

    i = 1
    while i <= len(strng):
        strng = get_rot(strng, i)

        if strng not in arr:
            return False
        else:
            i += 1

    return True

if __name__ == '__main__':
    print contain_all_rots("", []) # True
    print contain_all_rots("", ["bsjq", "qbsj"]) # True
    print contain_all_rots("bsjq", ["bsjq", "qbsj", "sjqb", "twZNsslC", "jqbs"]) # True
    print contain_all_rots("XjYABhR", ["TzYxlgfnhf", "yqVAuoLjMLy", "BhRXjYA", "YABhRXj", "hRXjYAB", "jYABhRX", "XjYABhR", "ABhRXjY"]) # False


