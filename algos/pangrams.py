# pangrams

s = 'the quick brown fox jumps over the lazy dog'


def pangrams(s):
    cleanS = s.replace(' ', '').lower()
    # print(cleanS)
    # print(set(cleanS))
    # print(set('abcdefghijklmnopqrstuvwxyz'))
    if set(cleanS) == set('abcdefghijklmnopqrstuvwxyz'):
        return('pangram')
    return('not pangram')


pangrams(s)
