# -*- coding: utf-8 -*-
"""
Author : JOFIN F ARCHBALD
"""


def sort(arr: list) -> list:
    """
    Timsort built in Rust.
    """
    import rusty_sorter as so
    if str(type(arr[0])) == "<class 'int'>":
        return so.sort_int(arr)
    elif str(type(arr[0])) == "<class 'float'>":
        return so.sort_float(arr)
    else:
        return so.sort_str(arr)

