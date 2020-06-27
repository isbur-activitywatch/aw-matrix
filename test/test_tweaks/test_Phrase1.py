import unittest
import tweaks


class TestPhrase1(unittest.TestCase):

    def test_Phrase1_launch(self):
        print(dir())
        self.assertTrue("Phrase1" in dir())

if __name__ == "__main__":
    unittest.main()
