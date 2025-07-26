import unittest
from unittest.mock import patch
from web_app import app, fetch_data

class TestWebApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to the Web App', response.data)

    @patch('web_app.fetch_data')
    def test_fetch_data(self, mock_fetch):
        mock_fetch.return_value = {'data': 'Sample data'}
        response = self.app.get('/data')
        mock_fetch.assert_called_once()
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Sample data', response.data)

if __name__ == '__main__':
    unittest.main()