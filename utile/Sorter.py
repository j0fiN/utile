import rusty_sorter as so


def sort(arr: list) -> list:
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
    arrr = ["ap", "ca", "aap"]
    print(sort(arrr))