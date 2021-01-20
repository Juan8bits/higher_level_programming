#!/usr/bin/python3
"""100-my_int module"""


class MyInt(int):
    """MyInt class"""
    def __ne__(self, number):
        return super().__eq__(number)

    def __eq__(self, number):
        return super().__ne__(number)
