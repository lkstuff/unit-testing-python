import unittest

from phonebook import Phonebook

class PhonebookTest(unittest.TestCase):

    def setUp(self):
        self.phonebook = Phonebook()
   
    def test_lookup_entry_by_name(self):
        self.phonebook.add("Viki", "12345")
        self.assertEqual("12345", self.phonebook.lookup("Viki"))

    def test_missing_entry_raises_KeyError(self):
        with self.assertRaises(KeyError):
            self.phonebook.lookup("missing")

    # @unittest.skip("WIP")
    def test_empty_phonebook_is_consistent(self):
        self.assertTrue(self.phonebook.is_consistent())

    @unittest.skip("Too many things in one case")
    def test_is_consistent(self):
        self.assertTrue(self.phonebook.is_consistent())
        self.phonebook.add("Marci", "12345")
        self.assertTrue(self.phonebook.is_consistent())
        self.phonebook.add("Csilla", "012345")
        self.assertTrue(self.phonebook.is_consistent())
        self.phonebook.add("Erika", "12345") #same as Marci
        self.assertFalse(self.phonebook.is_consistent)
        self.phonebook.add("Erika", "123") #prefix of Marci
        self.assertFalse(self.phonebook.is_consistent)

    def test_phonebook_with_normal_entries_is_consistent(self):
        self.phonebook.add("Marci", "12345")
        self.phonebook.add("Csilla", "012345")
        self.assertTrue(self.phonebook.is_consistent())

    @unittest.skip("WIP")
    def test_phonebook_with_duplicate_entries_is_inconsistent(self):
        self.phonebook.add("Marci", "12345")
        self.phonebook.add("Erika", "12345")
        self.assertFalse(self.phonebook.is_consistent)

    @unittest.skip("WIP")
    def test_phonebook_with_numbers_that_prefix_one_another_is_inconsistance(self):
        self.phonebook.add("Marci", "12345")
        self.phonebook.add("Erika", "123")
        self.assertFalse(self.phonebook.is_consistent)

    @unittest.skip("WIP")
    def test_phonebook_adds_names_and_numbers(self):
        self.phonebook.add("Andi", "12345")
        self.assertIn("Andi", self.phonebook.get_names())
        self.assertIn("12345", self.phonebook.get_numbers())


        


    # def tearDown(self):
    #     pass 














