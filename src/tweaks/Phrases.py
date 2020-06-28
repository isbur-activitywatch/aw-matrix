class define_meaning_of_phrase_:
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

