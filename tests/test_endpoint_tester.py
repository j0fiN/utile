import unittest
import requests
response = requests.request("GET", url="https://covid-api-19.glitch.me/api/notildore2020/country/India")
print(response.raw)
print(response.reason)
print(response.request)
print(response.text)
print(response.url)
print(response.apparent_encoding)
print(response.history)
print(response.cookies)

# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)
#
#
# if __name__ == '__main__':
#     unittest.main()
