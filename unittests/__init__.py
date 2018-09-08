import unittest
import requests
import json

class TestStringMethods(unittest.TestCase):

    def test_sucessful_login(self):
        result = requests.post('http://localhost:5000/api_login',
                               data={'username':'WhiteSummeRK','pwd':'123'})
        self.assertEqual(json.loads(result.text)['is_authenticated'],1)

    def test_unsucessful_login(self):
        result = requests.post('http://localhost:5000/api_login',
                               data={'username':'xxx','pwd':'xxx'})
        self.assertEqual(json.loads(result.text)['is_authenticated'],0)

if __name__ == '__main__':
    unittest.main()
