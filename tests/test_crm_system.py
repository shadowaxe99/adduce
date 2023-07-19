import unittest
from src import crm_system

class TestCRMSytem(unittest.TestCase):

    def setUp(self):
        self.crm = crm_system.CRMSystem()
        self.user = {"username": "test_user", "password": "test_password"}
        self.investor = {"name": "test_investor", "email": "investor@test.com"}
        self.company = {"name": "test_company", "industry": "tech"}
        self.deal = {"company": self.company, "investor": self.investor, "amount": 1000000}

    def test_login(self):
        response = self.crm.login(self.user["username"], self.user["password"])
        self.assertEqual(response, "login_success")

    def test_signup(self):
        response = self.crm.signup(self.user["username"], self.user["password"])
        self.assertEqual(response, "signup_success")

    def test_add_investor(self):
        response = self.crm.add_investor(self.investor)
        self.assertEqual(response, "Investor added successfully")

    def test_update_investor(self):
        response = self.crm.update_investor(self.investor)
        self.assertEqual(response, "Investor updated successfully")

    def test_delete_investor(self):
        response = self.crm.delete_investor(self.investor)
        self.assertEqual(response, "Investor deleted successfully")

    def test_add_company(self):
        response = self.crm.add_company(self.company)
        self.assertEqual(response, "Company added successfully")

    def test_update_company(self):
        response = self.crm.update_company(self.company)
        self.assertEqual(response, "Company updated successfully")

    def test_delete_company(self):
        response = self.crm.delete_company(self.company)
        self.assertEqual(response, "Company deleted successfully")

    def test_add_deal(self):
        response = self.crm.add_deal(self.deal)
        self.assertEqual(response, "Deal added successfully")

    def test_update_deal(self):
        response = self.crm.update_deal(self.deal)
        self.assertEqual(response, "Deal updated successfully")

    def test_delete_deal(self):
        response = self.crm.delete_deal(self.deal)
        self.assertEqual(response, "Deal deleted successfully")

if __name__ == "__main__":
    unittest.main()