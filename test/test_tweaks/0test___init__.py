# import sys
# print(sys.path)

# import unittest


# from tweaks import on, local_server

# class Container:

#     def __init__(self, contents):
#         self.contents = contents

# a = Container("")
# a /on/ local_server

# class TestOnPreposition(unittest.TestCase):

#     def test_it_works(self):
#         self.assertEqual(
#             type(a.contents),
#             type({})
#         )


# from tweaks import buckets, on, local_server

# class TestFirstPhrase(unittest.TestCase):

#     def test_first_phrase(self):
#         for bucket in buckets /on/ local_server:
#             print(bucket)
#             self.assertEqual(
#                 type(bucket),
#                 type("")
#             )


# from tweaks import Fetch, last

# class TestSecondPhrase(unittest.TestCase):

#     def test_second_phrase(self):

#         bucket = "aw-watcher-window_LAPTOP-K7OIHKV4"
#         events = ["placeholder"]

#         # Fetch | last-events /originating_at/ bucket

#         self.assertEqual(type(events), type([]))






# # """
# # >>> test_test_function()
# # foo
# # bar
# # """

# # def test_test_function():
# #     from .Phrases import Function_With_Prepositions
# #     proto = "Fetch | last-events /originating_at/ bucket"
# #     def foo(obj = "bzz", originating_at = "baz"):
# #         print(obj)
# #         print(originating_at)
    
# #     Fetch = Function_With_Prepositions(foo, proto)
# #     last_events = "foo"
# #     bucket = "bar"
# #     Fetch | last_events /originating_at/ bucket



# # from .Phrases import Function_With_Prepositions

# if __name__ == "__main__":
#     print("YEAH!")
#     unittest.main()