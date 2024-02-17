import unittest
import requests

class TestFlaskApp(unittest.TestCase):
    base_url='http://127.0.0.1:5000'

    def test_home_endpoint(self):
        response= requests.get(f'{self.base_url}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, 'Welcome to the Flask API!')

    def test_total_spending_by_age_endpoint(self):
        user_id= 123
        response= requests.get(f'{self.base_url}/total_spending_by_age/{user_id}')
        self.assertEqual(response.status_code, 200)

    def test_total_spent_endpoint(self):
        user_id= 123
        response= requests.get(f'{self.base_url}/total_spent/{user_id}')
        self.assertEqual(response.status_code, 200)

    def test_write_to_mongodb_endpoint(self):
        data = {'user_id': 1, 'total_spending': 100}
        response = requests.post(f'{self.base_url}/write_to_mongodb', json=data)
        self.assertEqual(response.status_code, 201)
        response_get= requests.get(f'{self.base_url}/write_to_mongodb')
        self.assertEqual(response_get.status_code, 200)


if __name__== '__main__':
    unittest.main()
