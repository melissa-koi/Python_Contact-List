import unittest
from contact import Contact


class TestContact(unittest.TestCase):

    def setUp(self):
        self.newContact = Contact("James", "Muriuki", "0712345678", "james@gmail.com")

    def test_init(self):
        self.assertEqual(self.newContact.first_name, "James")
        self.assertEqual(self.new_contact.last_name, "Muriuki")
        self.assertEqual(self.new_contact.phone_number, "0712345678")
        self.assertEqual(self.new_contact.email, "james@gmail.com")


if __name__ == '__main__':
    unittest.main()
