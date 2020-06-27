from .Preposition import Preposition
class Function_With_Prepositions:

    bucket = []
    

    def __init__(self, prototype=""):

        prototype = prototype.split("|")[-1:][0]
        prototype = prototype.split("/")
        Infices = []
        for i in range(1, len(prototype), 2):
            Infices.append(prototype[i])
        self.Infices = Infices

        import inspect
        import sys
        
        module_name = inspect.currentframe().f_back.f_globals["__name__"]
        module2 = sys.modules[module_name]

        for infix in Infices:
            setattr(module2, infix, Preposition(infix))
    
    def __call__(self, function):
        pass
    
    def __or__(self, righthand_operand):
        return self.function(**righthand_operand)


class define_meaning_of_phrase_:
    """
    Sort of dumb decorator class
    Why have I created this one?
    Dunno
    """
    def __init__(self, phrase_to_define, name):
        self.function_name = name
        
        # setattr(module)
        # pass

    def __call__(self, Definition):
        Definition()

        import inspect
        import sys
        module_name = inspect.currentframe().f_back.f_globals["__name__"] # I'm afraid it's too fragile
        module = sys.modules[module_name]
        setattr(module, self.function_name, Definition)

        return None






# proto = "Fetch | last-events /originating_at/ bucket"
# def foo(obj = "bzz", originating_at = "baz"):
#     print(obj)
#     print(originating_at)
# Fetch = Function_With_Prepositions(foo, proto)
# last_events = "foo"
# bucket = "bar"
# Fetch | last_events /originating_at/ bucket