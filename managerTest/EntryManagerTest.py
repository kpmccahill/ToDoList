import unittest
from manager.Entry import Entry
from manager.EntryManager import EntryManager


class EntryManagerTest(unittest.TestCase):

    def test_add(self):
        entry_manager = EntryManager()
        entry_manager.addEntry(Entry("Task1", "DateDue"))
        entry_manager.addEntry(Entry("Task2", "DateDue"))

        check_manager = EntryManager([Entry("Task1", "DateDue"),
                                      Entry("Task2", "DateDue")])

        self.assertTrue(entry_manager.equals(check_manager))
        self.assertTrue(entry_manager.equals(entry_manager))

    def test_set(self):
        entry_manager = EntryManager([Entry("Task1", "DateDue"),
                                      Entry("Task2", "DateDue")])

        entry_manager.setEntry(Entry("Task3", "DateDue"), 0)

        check_manager = EntryManager([Entry("Task3", "DateDue"),
                                      Entry("Task2", "DateDue")])

        self.assertTrue(entry_manager.equals(check_manager))
        self.assertTrue(entry_manager.equals(entry_manager))

    def test_remove(self):
        entry_manager = EntryManager([Entry("Task1", "DateDue"),
                                      Entry("Task2", "DateDue")])

        check_manager = EntryManager([Entry("Task2", "DateDue")])

        entry_manager.removeEntry(0)
        self.assertFalse(entry_manager.equals(check_manager))


        entry_manager.flip_flag(0)
        entry_manager.removeEntry(0)

        self.assertTrue(entry_manager.equals(check_manager))


if __name__ == '__main__':
    unittest.main()
