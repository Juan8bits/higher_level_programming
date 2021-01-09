#!/usr/bin/python3
"""Function that prints a text with 2 new lines
   after each of these characters: ., ? and :.
"""


def text_indentation(text):
    """function that prints a text with 2 new lines after
       special characters (.,?,:).
    """

    if type(text) is not (str):
        raise TypeError('text must be a string')
    char = 0
    status = False
    while text[char] == ' ':
        char += 1

    while char < len(text):

        if text[char - 1] in ('.', '?', ':') and char > 0:
            print('\n')
            if text[char] != ' ':
                print("{}".format(text[char]), end='')
            while text[char] == ' ':
                char += 1
                status = True
            if status:
                char -= 1
                status = False
        else:
            print("{}".format(text[char]), end='')
        char += 1
    if text[char - 1] in ('.', '?', ':') and char > 0:
        print('\n')
