import unittest
from src.deal_flow_management import add_deal, update_deal, delete_deal

class TestDealFlowManagement(unittest.TestCase):

    def setUp(self):
        self.deal_id = None

    def test_add_deal(self):
        self.deal_id = add_deal("Deal 1", "Company 1", "Investor 1", "Stage 1", 1000000)
        self.assertIsNotNone(self.deal_id, "Failed to add deal")

    def test_update_deal(self):
        new_deal_id = update_deal(self.deal_id, "Deal 1 Updated", "Company 1", "Investor 1", "Stage 2", 2000000)
        self.assertEqual(self.deal_id, new_deal_id, "Failed to update deal")

    def test_delete_deal(self):
        result = delete_deal(self.deal_id)
        self.assertTrue(result, "Failed to delete deal")

    def tearDown(self):
        if self.deal_id:
            delete_deal(self.deal_id)

if __name__ == '__main__':
    unittest.main()