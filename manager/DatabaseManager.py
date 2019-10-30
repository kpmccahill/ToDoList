"""Class that handles adding all entries to the database for
permanent storage, and retrieving them from permanent storage
on launch.

:author: Kyle McCahill
"""

import os
import sqlite3
from manager.Entry import Entry
from manager.EntryManager import EntryManager


class DatabaseManager:

    def __init__(self, EntryManager):
        if os.path.exists(os.path.expanduser("~/ToDoManager/")):
            pass


if __name__ == "__main__":
    x = check_manager = EntryManager()

    print(x.to_string())