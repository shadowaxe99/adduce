import unittest
from src import collaboration_tools

class TestCollaborationTools(unittest.TestCase):

    def setUp(self):
        self.collaboration_tools = collaboration_tools.CollaborationTools()

    def test_add_message(self):
        result = self.collaboration_tools.add_message("Test message")
        self.assertEqual(result, "Test message added")

    def test_delete_message(self):
        self.collaboration_tools.add_message("Test message")
        result = self.collaboration_tools.delete_message("Test message")
        self.assertEqual(result, "Test message deleted")

    def test_update_message(self):
        self.collaboration_tools.add_message("Test message")
        result = self.collaboration_tools.update_message("Test message", "Updated message")
        self.assertEqual(result, "Test message updated to Updated message")

    def test_view_messages(self):
        self.collaboration_tools.add_message("Test message")
        result = self.collaboration_tools.view_messages()
        self.assertEqual(result, ["Test message"])

if __name__ == '__main__':
    unittest.main()