#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stringReduction' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def StringReduction(strParam):

  # code goes here
    def reduce(two_letters):
        if two_letters[0] == two_letters[1]:
            return two_letters
        elif two_letters in ('ab', 'ba'):
            return 'c'
        elif two_letters in ('ac', 'ca'):
            return 'b'
        else:
            return 'a'
    
    if len(strParam) < 2:
        return strParam

    i = 1
    reduced = reduce(strParam[0:2])
    ans = ''
    while i < len(strParam) - 1:
        if len(reduced) == 2:
            ans += reduced[0]
        i += 1
        reduced = reduce(reduced[-1] + str[i])
    if reduced:
        ans += reduced
    return len(ans)


def StringReduction(the_strParam):
    change =  False
    letters = set(['a', 'b', 'c'])
    duo = [the_strParam[0]]
    final = ''
    for s in the_strParam[1:]:
        duo.append(s)
        if duo[0] == duo[1]:
            final += duo[0]
            duo = [duo[1]]
        else:
            change = True
            reduced = list((letters - set(duo)))[0]
            duo = [reduced]
    final += ''.join(duo)
    if change:
        return StringReduction(final)
    return len(final)
# keep this function call here 
print(StringReduction(input()))




