#!/usr/bin/python3
def best_score(a_dic):
    if not a_dic:
        return (None)
    return (max(a_dic, key=a_dic.get))
