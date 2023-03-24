#!/usr/bin/python3
""" Testing console"""
import unittest
from console import HBNBCommand


class TestConsoleProgram(unittest.TestCase):
    ''' Testing do_create() and do_all()'''
    def test_create(self):
        ''' Creates person object and checks if matches with dict format'''
        program = HBNBCommand()
        program.do_create("Person name=John age=25")
        self.assertEqual(program.storage.all()["Person.1"].to_dict(),
                         {"id": "Person.1", "name": "John", "age": 25})

    def test_all(self):
        ''' Creates another person and checks if info is correct'''
        program = HBNBCommand()
        program.do_create("Person name=John age=25")
        program.do_create("Person name=Sarah age=30")
        all_people = program.do_all("Person")
        self.assertEqual(len(all_people), 2)
        self.assertIn(("John", 25), all_people)
        self.assertIn(("Sarah", 30), all_people)
