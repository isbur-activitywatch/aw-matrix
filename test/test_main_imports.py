# pylint: disable=no-self-use


import unittest


import sys


import main
import tweaks


class TestImportsInMain(unittest.TestCase):

    def test_target_names_presence(self):
        target_names = [
            "buckets", "on", "local_server",
            # "Fetch", "last", "events", "originating_at",
            # "Post", "them", "to", "Synapse", "server"
        ]

        for name in target_names:
            self.assertTrue(name in dir(sys.modules['main']))




if __name__ == "__main__":
    unittest.main()
