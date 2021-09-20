# 📚🔍

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#

import string
word = "zaba"
h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5,
     5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]


def designerPdfViewer(h, word):
    height = 0
    width = len(word)
    alphab = string.ascii_lowercase
    word = str.lower(word)

    for i in word:
        wordHeight = h[alphab.index(i)]
        if wordHeight > height:
            height = wordHeight

    return(width * height)


designerPdfViewer(h, word)
