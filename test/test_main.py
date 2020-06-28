# pylint: disable=no-self-use,unused-import,undefined-variable


import unittest


import sys


import main
import tweaks


class TestMainImports(unittest.TestCase):

    def test_succesful_launch_award(self):
        pass


class TestImportsInMain(unittest.TestCase):

    def test_target_names_presence(self):
        target_names = [
            "buckets", "on", "local_server",
            # "Fetch", "last", "events", "originating_at",
            # "Post", "them", "to", "Synapse", "server"
        ]

        for name in target_names:
            self.assertTrue(name in dir(sys.modules['main']))


class TestMainWorks(unittest.TestCase):

    def test_Phrase1(self):

        test_module = sys.modules['test.test_main']
        main_module = sys.modules['main']
        for var in dir(main_module):
            setattr(test_module, var, getattr(main_module, var))

        self.assertEqual(
            type(buckets /on/ local_server),
            type({})
        )



if __name__ == "__main__":
    unittest.main()
