import unittest
from unittest.mock import patch
from src import user_interface

class TestUserInterface(unittest.TestCase):

    @patch('src.user_interface.login')
    def test_login_success(self, mock_login):
        mock_login.return_value = "login_success"
        result = user_interface.login("test_username", "test_password")
        self.assertEqual(result, "login_success")

    @patch('src.user_interface.login')
    def test_login_fail(self, mock_login):
        mock_login.return_value = "login_fail"
        result = user_interface.login("wrong_username", "wrong_password")
        self.assertEqual(result, "login_fail")

    @patch('src.user_interface.signup')
    def test_signup_success(self, mock_signup):
        mock_signup.return_value = "signup_success"
        result = user_interface.signup("new_username", "new_password")
        self.assertEqual(result, "signup_success")

    @patch('src.user_interface.signup')
    def test_signup_fail(self, mock_signup):
        mock_signup.return_value = "signup_fail"
        result = user_interface.signup("existing_username", "existing_password")
        self.assertEqual(result, "signup_fail")

if __name__ == '__main__':
    unittest.main()