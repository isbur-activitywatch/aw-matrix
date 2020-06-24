from .Preposition import Preposition


class Function_With_Prepositions:

    def __init__(self, function, prototype=""):
        self.function = function

        prototype = prototype.split("|")[-1:][0]
        prototype = prototype.split("/")
        Infices = []
        for i in range(1, len(prototype), 2):
            Infices.append(prototype[i])
        self.Infices = Infices

        for infix in Infices:
            globals()[infix] = Preposition(infix)
            pass

def foo():
    pass

proto = "Fetch | last-events /originating_at/ bucket"

Fetch = Function_With_Prepositions(foo, proto)