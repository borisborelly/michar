import unittest
import michar

class testMichi(unittest.TestCase):
    def testVersion(self):
        print(michar.__version__)