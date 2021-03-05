# -*- coding: utf-8 -*-
"""
The python package which eases your <codeflow> using @decorators.

Sorter.sort(List)
    sorts the list in ascending order.

@timer(store=False, round_off=10)
    Decorator which print execution time of any function.

@threader(funcs, func_result=False)
    A Frame-Determined decorator to spring up number of I/O bound tasks.

@processor(funcs, func_result=False, get_result=False)
    A Frame-Determined decorator to spring up number of CPU bound tasks.

For more info: https://pypi.org/project/utile/
Author : JOFIN F ARCHBALD
"""
from .Processor import processor
from .Threader import threader
from .Timer import timer
from .Sorter import sort
