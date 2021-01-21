#!/usr/bin/python3
"""Script that adds all arguments to a Python
   list, and then save them to a file
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

name_file = "add_item.json"
try:
    arrPy = load_from_json_file(name_file)
except:
    arrPy = []
for i in sys.argv[1:]:
    arrPy.append(i)
save_to_json_file(arrPy, name_file)
