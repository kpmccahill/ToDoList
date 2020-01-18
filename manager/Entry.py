"""
Defines the Entry class. Which contains all info
that each task entry has.

:author: Kyle McCahill
"""


class Entry:
    def __init__(self, item, dDate):
        self.item = item
        self.dueDate = dDate
        self.flag = 0

    """
    Converts the Entry into a string
    
    :returns: Full string of the Entry 
    """
    def to_string(self):
        entryString = self.item + " | " + self.dueDate
        return entryString

    """
    Tests whether or not this Entry is equal to
    another Entry.

    :param otherEntry:  another Entry class
    :returns: true if equal to each other
    """
    def equals(self, otherEntry):
        isEqual = True
        if (self.item != otherEntry.item) or (self.dueDate != otherEntry.dueDate):
            isEqual = False

        return isEqual


if __name__ == "__main__":
    entry = Entry("Task", "DueDate")
    print(entry.to_string())