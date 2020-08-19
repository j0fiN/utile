def tester(return_test=False, test=False):
    import unittest
    from functools import wraps

    def tes(func: 'function') -> 'function':

        @wraps(func)
        def wrapper(*args: 'arguments', **kwargs: 'keyword arguments') -> 'function':
            if test is True:
                if return_test is not None:
                    RESULT = func(*args, **kwargs)
                    test_model = unittest.TestCase()
                    test_model.assertEqual(RESULT, return_test['value'], msg="Not equal")
                    test_model.assertEqual(type(RESULT), return_test['type'], msg="Not equal")
                    print("return test successful")
            else:
                return func(*args, **kwargs)

        return wrapper

    return tes


if __name__ == '__main__':
    @tester(test=True, return_test={'value': 12,
                                    'type': int})
    def foo():
        return 12


    foo()
