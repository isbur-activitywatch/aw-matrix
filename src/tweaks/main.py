"""
>>> test_test_function()
foo
bar
"""

def test_test_function():
    from .Phrases import Function_With_Prepositions
    proto = "Fetch | last-events /originating_at/ bucket"
    def foo(obj = "bzz", originating_at = "baz"):
        print(obj)
        print(originating_at)
    
    Fetch = Function_With_Prepositions(foo, proto)
    last_events = "foo"
    bucket = "bar"
    Fetch | last_events /originating_at/ bucket



from .Phrases import Function_With_Prepositions


@Function_With_Prepositions
def Fetch():
    pass


@Function_With_Prepositions
def Post():
    pass


