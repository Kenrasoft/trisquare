"""
The purpose of this unittest_cases.py is to do testing using unit test for the singleton instance..
"""

import unittest
import test_functions
from core.configuration.config_singleton import config_singleton_a

class TestFunctions(unittest.TestCase):
    """
    This class takes the argument unittest.TestCase from the imported unittest library.
    """

    def test_config_singleton_a(self):
        """
        create two instances of singleton class and comparing the instances to ensure that they refer to the same object.

	    :return: test case is passed if the both the instances refer to the same class.
        """
        
        object1 = config_singleton_a()
        object1.load_config()
        object2 = config_singleton_a()
        object2.load_config()
        return self.assertEqual(test_functions.test_config_singleton(object1,object2),True)


if __name__ == '__main__':
    unittest.main()