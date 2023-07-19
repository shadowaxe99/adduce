import unittest
from src.investor_relations_management import add_investor, update_investor, delete_investor

class TestInvestorRelationsManagement(unittest.TestCase):

    def setUp(self):
        self.investor_data = {
            "name": "John Doe",
            "email": "johndoe@example.com",
            "investments": []
        }

    def test_add_investor(self):
        response = add_investor(self.investor_data)
        self.assertEqual(response, {"message": "Investor added successfully"})

    def test_update_investor(self):
        response = update_investor(self.investor_data)
        self.assertEqual(response, {"message": "Investor updated successfully"})

    def test_delete_investor(self):
        response = delete_investor(self.investor_data)
        self.assertEqual(response, {"message": "Investor deleted successfully"})

if __name__ == '__main__':
    unittest.main()