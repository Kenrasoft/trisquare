"""
The purpose of this test_functions.py is to define a method which compares two instances of singleton class.
"""

def test_config_singleton(a, b):
    """
    comparing two instances of singleton class.
    :return: True if they both refer to the same object else false.
	"""

    return (a is b)
