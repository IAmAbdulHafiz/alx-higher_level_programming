#!/usr/bin/python3

def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    _returns = list(a_dictionary.keys())[0]
    _bigg = a_dictionary[_returns]
    for k, j in a_dictionary.items():
        if j > _bigg:
            b_bigg = j
            _returns = k
    return (_returns)
