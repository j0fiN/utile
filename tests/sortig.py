import sys
sys.path.append('..')
from utile.Sorter import sort
def test_sort():
        a = [1, 3, 4, 2, 5]
        return sort(a)

print(test_sort())