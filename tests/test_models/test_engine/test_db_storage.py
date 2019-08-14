#!/usr/bin/python3
import os
""" test for db_storage """
import unittest
import pep8
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestDBStorage(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_pep8_FileStorage(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_all(self):
        pass

    def test_new(self):
        pass

    def test_save(self):
        pass

    def test_reload(self):
        pass

    def test_delete(self):
        pass
