import unittest
from src import portfolio_companies_management as pcm

class TestPortfolioCompaniesManagement(unittest.TestCase):

    def setUp(self):
        self.company_data = {
            "name": "Test Company",
            "industry": "Tech",
            "stage": "Seed",
            "valuation": 1000000
        }
        self.company_id = None

    def test_add_company(self):
        response = pcm.add_company(self.company_data)
        self.company_id = response['id']
        self.assertEqual(response['message'], "Company added successfully")

    def test_update_company(self):
        update_data = {
            "name": "Updated Test Company",
            "industry": "Tech",
            "stage": "Series A",
            "valuation": 2000000
        }
        response = pcm.update_company(self.company_id, update_data)
        self.assertEqual(response['message'], "Company updated successfully")

    def test_delete_company(self):
        response = pcm.delete_company(self.company_id)
        self.assertEqual(response['message'], "Company deleted successfully")

if __name__ == '__main__':
    unittest.main()