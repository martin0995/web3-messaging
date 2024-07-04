import unittest
from bot.bot import app

class BotTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_webhook(self):
        response = self.app.post('/webhook', data={'Body': 'balance'})
        self.assertIn('Fetching your balance...', response.data.decode())

if __name__ == '__main__':
    unittest.main()