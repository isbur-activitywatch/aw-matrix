import sys


class define_meaning_of_phrase_:

    def __init__(self, phrase_to_define, name, names_to_bind):
        self.function_name = name
        self.names_to_bind = names_to_bind

    def __call__(self, Definition):

        for name in self.names_to_bind:
            setattr(
                sys.modules['main'], 
                name, 
                getattr(
                    Definition, 
                    name
                )
            )


        return None
