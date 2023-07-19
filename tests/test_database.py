import unittest
from src.database import db_connection

class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.db = db_connection

    def test_db_connection(self):
        self.assertIsNotNone(self.db, "Database connection failed.")

    def test_add_user(self):
        user = {"username": "test_user", "password": "test_password"}
        result = self.db.add("UserSchema", user)
        self.assertTrue(result, "Adding user failed.")

    def test_add_investor(self):
        investor = {"name": "test_investor", "email": "test_investor@test.com"}
        result = self.db.add("InvestorSchema", investor)
        self.assertTrue(result, "Adding investor failed.")

    def test_add_company(self):
        company = {"name": "test_company", "description": "test_description"}
        result = self.db.add("CompanySchema", company)
        self.assertTrue(result, "Adding company failed.")

    def test_add_deal(self):
        deal = {"company": "test_company", "investor": "test_investor", "amount": 1000000}
        result = self.db.add("DealSchema", deal)
        self.assertTrue(result, "Adding deal failed.")

    def test_delete_user(self):
        result = self.db.delete("UserSchema", "test_user")
        self.assertTrue(result, "Deleting user failed.")

    def test_delete_investor(self):
        result = self.db.delete("InvestorSchema", "test_investor")
        self.assertTrue(result, "Deleting investor failed.")

    def test_delete_company(self):
        result = self.db.delete("CompanySchema", "test_company")
        self.assertTrue(result, "Deleting company failed.")

    def test_delete_deal(self):
        result = self.db.delete("DealSchema", {"company": "test_company", "investor": "test_investor"})
        self.assertTrue(result, "Deleting deal failed.")

if __name__ == '__main__':
    unittest.main()