#!/usr/bin/python3
""" Module for testing DB storage"""
import unittest
from models.engine import db_storage
from models.engine.db_storage import DBStorage

class Test_DBStorage(unittest.TestCase):
    """Comment"""
    def test_documentation(self):
        self.assertTrue(db_storage.__doc__)
        self.assertTrue(db_storage.DBStorage.__doc__)

    def test_method_doc(self):
        for method in dir(DBStorage):
            self.assertTrue(method.__doc__)
