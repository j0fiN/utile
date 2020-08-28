

def sort(arr: list) -> list:
    import rusty_sorter as so
    """
    Timsort built in Rust.
    """
    if str(type(arr[0])) == "<class 'int'>":
        return so.sort_int(arr)
    elif str(type(arr[0])) == "<class 'float'>":
        return so.sort_float(arr)
    else:
        return so.sort_str(arr)


if __name__ == '__main__':
    print(sort([1, 3, 4, 2, 5]))