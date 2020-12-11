#!/usr/bin/python3
if __name__ == '__main__':
    """ Function that print methods in a hidden file """
    import hidden_4
    hidden = dir(hidden_4)
    for method in hidden:
        if method[0] != '_':
            print(method)
