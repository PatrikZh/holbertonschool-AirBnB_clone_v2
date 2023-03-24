#!/usr/bin/python3
""" Module for testing DB storage"""
import unittest
from models.engine import db_storage
from models.engine.db_storage import DBStorage

class Test_DBStorage(unittest.TestCase):
    """ Module for testing DB storage"""
    def test_documentation(self):
        """ Module for testing DB storage"""
        self.assertTrue(db_storage.__doc__)
        self.assertTrue(db_storage.DBStorage.__doc__)

    def test_method_doc(self):
        """ Module for testing DB storage"""
        for method in dir(DBStorage):
            self.assertTrue(method.__doc__)

if __name__ == "__main__":
    unittest.main()
