import unittest
import michar

class testMichi(unittest.TestCase):
    def testVersion(self):
        print(f"{michar.__name__=} {michar.__version__=}")
        self.assertIsNotNone(michar.__name__)
        self.assertIsNotNone(michar.version)