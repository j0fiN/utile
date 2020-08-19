def tester(return_test=None):
    import unittest
    from functools import wraps

    def tes(func: 'function') -> 'function':

        @wraps(func)
        def wrapper(*args: 'arguments', **kwargs: 'keyword arguments') -> 'function':
            if kwargs['test'] is True:
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
    @tester(return_test={'value': 21,
                         'type': int})
    def foo(a, b, **_):

        return a + b


    foo(10, 11, test=True)
