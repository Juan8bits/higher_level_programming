#!/usr/bin/python3
def best_score(a_d):
    if a_d:
        max_value = max(a_d, key=lambda v: a_d[v])
        return max_value
    return None
