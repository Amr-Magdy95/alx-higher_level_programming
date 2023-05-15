#!/usr/bin/python3
# mul ret

def multiple_returns(sentence):
    """ ret len of a string"""
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
