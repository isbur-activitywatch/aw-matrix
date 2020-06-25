from .Preposition import Preposition
class Function_With_Prepositions:
    

    def __init__(self, function, prototype=""):

        # print("#"*40)
        # print("I'm in __init__")

        self.function = function

        prototype = prototype.split("|")[-1:][0]
        prototype = prototype.split("/")
        Infices = []
        for i in range(1, len(prototype), 2):
            Infices.append(prototype[i])
        self.Infices = Infices
        # print(Infices)

        # import sys
        # module = sys.modules[__name__]

        import inspect
        import sys
        
        # for i in range(5):

        # i = 0
        # for caller_frame in inspect.stack():
        #     print("#"*10)
        #     print(caller_frame)
        #     print(caller_frame.frame.f_locals.keys())
        #     print("#"*10)
        #     i += 1
        #     if i > 4:
        #         break
        
        # print("#"*40)
        # print(inspect.stack()[1])
        # print()
        # print(inspect.getmodule(inspect.stack()[1]))
        # print(inspect.stack()[1][0])
        # print(inspect.getmodule(inspect.stack()[1][0]))
        # print(inspect.stack()[1][1])
        # print(inspect.getmodule(inspect.stack()[1][1]))
        #print(sys.modules.keys())
        module_name = inspect.currentframe().f_back.f_globals["__name__"]
        # print(module_name)
        # print(sys.modules[module_name])
        # 
        module2 = sys.modules[module_name]
        # print("#"*40)
        # print(module2)
        # print(module2.__dict__.keys())
        # print("#"*10)

        # print(caller_name())
        # print(module2)
        # print(module2.__name__)

        for infix in Infices:
            setattr(module2, infix, Preposition(infix))
        
        # print(module2)
        # print(module2.__dict__.keys())
        # print("#"*40)
    
    def __or__(self, righthand_operand):
        return self.function(**righthand_operand)


# import inspect

# def caller_name(skip=2):
#     """Get a name of a caller in the format module.class.method
    
#        `skip` specifies how many levels of stack to skip while getting caller
#        name. skip=1 means "who calls me", skip=2 "who calls my caller" etc.
       
#        An empty string is returned if skipped levels exceed stack height
#     """
#     stack = inspect.stack()
#     start = 0 + skip
#     if len(stack) < start + 1:
#       return ''
#     parentframe = stack[start][0]    
    
#     name = []
#     module = inspect.getmodule(parentframe)
#     # `modname` can be None when frame is executed directly in console
#     # TODO(techtonik): consider using __main__
#     if module:
#         name.append(module.__name__)
#     # detect classname
#     if 'self' in parentframe.f_locals:
#         # I don't know any way to detect call from the object method
#         # XXX: there seems to be no way to detect static method call - it will
#         #      be just a function call
#         name.append(parentframe.f_locals['self'].__class__.__name__)
#     codename = parentframe.f_code.co_name
#     if codename != '<module>':  # top level usually
#         name.append( codename ) # function or a method
#     del parentframe
#     return ".".join(name)



# proto = "Fetch | last-events /originating_at/ bucket"
# def foo(obj = "bzz", originating_at = "baz"):
#     print(obj)
#     print(originating_at)
# Fetch = Function_With_Prepositions(foo, proto)
# last_events = "foo"
# bucket = "bar"
# Fetch | last_events /originating_at/ bucket