import unittest


from ..tweaks import on, local_server

class Container:

    def __init__(self, contents):
        self.contents = contents

a = Container("")
a /on/ local_server

class TestOnPreposition(unittest.TestCase):



    def test_it_works(self):
        self.assertEqual(
            type(a.contents),
            type({})
        )


from ..tweaks import buckets, on, local_server

class TestFirstPhrase(unittest.TestCase):



    def test_first_phrase(self):
        for bucket in buckets /on/ local_server:
            print(bucket)
            self.assertEqual(
                type(bucket),
                type("")
            )