import unittest
import test_functions
from core.configuration.config_singleton import config_singleton

class TestFunctions(unittest.TestCase):

    def test_config_singleton(self):
        object1 = config_singleton()
        object1.load_config()
        object2 = config_singleton()
        object2.load_config()
        return self.assertEqual(test_functions.singleton(object1,object2),True)


if __name__ == '__main__':
    unittest.main()