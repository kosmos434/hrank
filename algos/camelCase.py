# 🐫


#
# Complete the 'camelcase' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
import re
s = "saveChangesInTheEditor"


def camelcase(s):
    # we use regex magick to split the words, then count that list o' words
    return(len(re.split('(?=[A-Z])', s)))


camelcase(s)
