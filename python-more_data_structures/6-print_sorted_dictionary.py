#!/usr/bin/python3

def sort_dict_by_keys(a_dictionary):
    sorted_dict = {}
    for key in sorted(a_dictionary):
        sorted_dict[key] = a_dictionary[key]
    return sorted_dict
