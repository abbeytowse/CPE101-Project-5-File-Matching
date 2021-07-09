# Project 5 – File Matching
# Name: Abbey Towse
# Section: 11
# Instructor: Clark Turner

import unittest
from fileMatchingFuncs import *


class TestCases(unittest.TestCase):
          
    def test_entry_init(self):
        entry = Entry('345', 'Bob Jones', 87.12, '8055551234', 'SLO')
        self.assertEqual(entry.account_num, '345')
        self.assertEqual(entry.name, 'Bob Jones')
        self.assertAlmostEqual(entry.balance, 87.12)
        self.assertEqual(entry.phone, '8055551234')
        self.assertEqual(entry.city, 'SLO')

    def test_read_file_0(self):
        entries = []
        entries.append(Entry('100', 'Alan Jones', 348.17, '8053564820', 'SLO'))
        entries.append(Entry('700', 'Suzy Green', -14.22, '8052586912', 'SLO'))
        # call read_file with 'test0.dat'
        self.assertEqual(read_file('test0.dat'), entries)

    def test_read_file_1(self):
        entries = []
        entries.append(Entry('100', 'Alan Jones', 348.17, '8053564820', 'SLO'))
        entries.append(Entry('700', 'Suzy Green', -14.22, '8052586912', 'SLO'))
        entries.append(Entry('300', 'Mary Smith', 27.19, '8057901237', 'Santa_Maria'))
        entries.append(Entry('800', 'Mike Rosen', -104.58, '8051200891', 'Pismo_Beach'))
        # call read_file with 'test1.dat'
        self.assertEqual(read_file('test1.dat'), entries)

    def test_read_files_2(self):
        entries = []
        entries.append(Entry('0', '0', 0, '0', '0'))
        self.assertNotEqual(read_file('test1.dat'), entries)

    def test_sort_entry_list_0(self):
        entry_list = []
        sorted_list = []
        self.assertEqual(sort_entry_list(entry_list), sorted_list)

    def test_sort_entry_list_1(self):
        entry_list = [Entry('300', 'Bob P', 23.45, '8008008000', 'Chicago'),
                      Entry('100', 'Joe W', 12.34, '1001001000', 'LA'),
                      Entry('123', 'Sam Q', 67.89, '2002002000', 'Poway')]
        sorted_list = [Entry('100', 'Joe W', 12.34, '1001001000', 'LA'),
                       Entry('123', 'Sam Q', 67.89, '2002002000', 'Poway'),
                       Entry('300', 'Bob P', 23.45, '8008008000', 'Chicago')]
        self.assertEqual((sort_entry_list(entry_list)), sorted_list)

    def test_sort_transaction_list_0(self):
        transaction_list = []
        sorted_list = []
        self.assertEqual(sort_transaction_list(transaction_list), sorted_list)

    def test_sort_transaction_list_1(self):
        transaction_list = [['200', 23.45], ['100', 12.34], ['150', 67.89]]
        sorted_list = [['100', 12.34], ['150', 67.89], ['200', 23.45]]
        self.assertEqual(sort_transaction_list(transaction_list), sorted_list)

    def test_binary_search_0(self):
        entry_list = []
        transaction_num = '123'
        self.assertEqual(binary_search(entry_list, transaction_num), -1)

    def test_binary_search_1(self):
        entry_list = [Entry('100', 'Joe W', 12.34, '1001001000', 'LA'),
                      Entry('123', 'Sam Q', 67.89, '2002002000', 'Poway'),
                      Entry('300', 'Bob P', 23.45, '8008008000', 'Chicago')]
        transaction_num = '123'
        self.assertEqual(binary_search(entry_list, transaction_num), 1)

    def test_account_balance_update_0(self):
        entry_list = []
        file_name = "transaction.dat"
        updated_list = []
        self.assertEqual(account_balance_update(entry_list, file_name), updated_list)

    def test_account_balance_update_1(self):
        entry_list = [Entry('100', 'Joe W', 12.34, '1001001000', 'LA'),
                      Entry('123', 'Sam Q', 67.89, '2002002000', 'Poway'),
                      Entry('500', 'Bob P', 23.45, '8008008000', 'Chicago')]
        file_name = "transaction.dat"
        updated_list = [Entry('100', 'Joe W', 109.65, '1001001000', 'LA'),
                        Entry('123', 'Sam Q', 67.89, '2002002000', 'Poway'),
                        Entry('500', 'Bob P', -31.80, '8008008000', 'Chicago')]
        self.assertEqual(account_balance_update(entry_list, file_name), updated_list)


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
