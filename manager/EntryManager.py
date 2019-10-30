"""Defines the Manager class. Which handles the runtime
modification and storage of the entries, by storing them
in a list

:author: Kyle McCahill
"""
from manager import Entry


class EntryManager:

    def __init__(self, entryList=[]):  # default is empty list
        self.entryList = entryList

    """Adds a new entry to the end of the list
    :param entry: the new entry to append
    """
    def addEntry(self, entry):
        self.entryList.append(entry)

    """Sets the entry at the given index to 
    the new entry.
    
    :param newEntry: the new entry to set
    :param index: where to place the new Entry
    """
    def setEntry(self, newEntry, index):
        self.entryList[index] = newEntry

    """Flips the flag of that entry to opposite
    boolean value.
    
    :param index: the Entry who's flag to flip
    """
    def flip_flag(self, index):
        if not self.entryList[index].flag:
            self.entryList[index].flag = True
        else:
            self.entryList[index].flag = False

    """Removes an entry from the list
    
    :param index: the Entry to remove
    """
    def removeEntry(self, index):
        print(self.entryList[index].to_string() + str(self.entryList[index].flag))
        if self.entryList[index].flag == True:
            self.entryList.remove(self.entryList[index])

    """Tests whether or not this Entry Manager is equal to
    another entry manager.
    
    :param otherEntry:  another entry manager
    :returns: true if equal to each other
    """
    def equals(self, otherManager):
        isEqual = True
        if len(self.entryList) == len(otherManager.entryList):
            for i in range(len(self.entryList)):
                if not self.entryList[i].equals(otherManager.entryList[i]):
                    isEqual = False
        else:
            isEqual = False
        return isEqual

    """Converts the manager to a readable string format
    
    :returns managerString: the formatted string
    """
    def to_string(self):
        NEWLINE = "\n"
        managerString = ""
        for i in range(len(self.entryList)):
            managerString += self.entryList[i].to_string() + NEWLINE

        return managerString
