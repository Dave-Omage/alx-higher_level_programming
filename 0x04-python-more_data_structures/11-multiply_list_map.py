#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrates how to return a list with all values multiplied by a number
# -----------------------------------------------------------


def multiply_list_map(my_list=[], number=0):
    return list(map(lambda i: number * i, my_list))
