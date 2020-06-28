"""
Fetch |, Post | - обёртки над функциями fetch, post, которые и делают всю грязную работу
(остально всё суть перекладывание и перепаковывание аргументов)
"""
#     for bucket in buckets /on/ local_server:
import tweaks.Phrase1

#         Fetch | last-events /originating_at/ bucket
# import tweaks.Phrase2

#         Post | them(events) /to/ Synapse-server


# maybe some good ideas for testing
"""
>>> a = Preposition("a")
>>> 1 /a/ 2 /a/ 3
{'obj': 1, 'a': 3}

>>> a = Preposition("a")
>>> b = Preposition("b")
>>> 1 /a/ 2 /b/ 3
{'obj': 1, 'a': 2, 'b': 3}


Some more contentful examples:

>>> last_events, bucket = ("foo","bar")
>>> originating_at = Preposition("originating_at")
>>> last_events /originating_at/ bucket
{'obj': 'foo', 'originating_at': 'bar'}
"""
