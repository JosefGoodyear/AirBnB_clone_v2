#!/usr/bin/python3
"""test for file storage"""
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


class TestFileStorage(unittest.TestCase):
    '''this will test the FileStorage'''

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.user = User()
        cls.user.first_name = "Kev"
        cls.user.last_name = "Yo"
        cls.user.email = "1234@yahoo.com"
        cls.storage = FileStorage()

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.user

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_FileStorage(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_all(self):
        """tests if all works in File Storage"""
        storage = FileStorage()
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, storage._FileStorage__objects)

    def test_new(self):
        """test when new is created"""
        storage = FileStorage()
        obj = storage.all()
        user = User()
        user.id = 123455
        user.name = "Kevin"
        storage.new(user)
        key = user.__class__.__name__ + "." + str(user.id)
        self.assertIsNotNone(obj[key])

    def test_reload_filestorage(self):
        """
        tests reload
        """
        self.storage.save()
        Root = os.path.dirname(os.path.abspath("console.py"))
        path = os.path.join(Root, "file.json")
        with open(path, 'r') as f:
            lines = f.readlines()
        try:
            os.remove(path)
        except:
            pass
        self.storage.save()
        with open(path, 'r') as f:
            lines2 = f.readlines()
        self.assertEqual(lines, lines2)
        try:
            os.remove(path)
        except:
            pass
        with open(path, "w") as f:
            f.write("{}")
        with open(path, "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(self.storage.reload(), None)

    def test_for_delete(self):
        """test for delete"""
        fs = FileStorage()
        new_state = State()
        new_state.name = "California"
        fs.new(new_state)
        fs.save()
        all_states = fs.all(State)
        # placeholder. change later.
        self.assertEqual(len(all_states.keys()), 2)
        fs.delete(new_state)
        all_states = fs.all(State)
        self.assertEqual(len(all_states.keys()), 1)

    def test_for_all(self):
        """test for all"""
        f = FileStorage()
        new_state = State()
        new_state.name = "California"
        f.new(new_state)
        f.save()
        new_2 = User()
        new_2.name = "Betty"
        f.new(new_2)
        f.save()
        all_1 = f.all(State)
        self.assertEqual(len(all_1.keys()), 1)

    def test_holder1(self):
        """testing placeholder"""
        pass

    def test_holder2(self):
        """testing placeholder"""
        pass

    def test_holder3(self):
        """testing placeholder"""
        pass

    def test_holder4(self):
        """testing placeholder"""
        pass


if __name__ == "__main__":
    unittest.main()
