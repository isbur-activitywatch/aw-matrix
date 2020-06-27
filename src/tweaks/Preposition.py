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
class Preposition:

    def __init__(self, name):
        self.name = name
    
    def __rtruediv__(self, lefthand_operand):
        self.innerObject = lefthand_operand
        return self

    def __truediv__(self, righthand_operand):
        if type(self.innerObject) == type({}):
            self.innerObject[self.name] = righthand_operand
            return self.innerObject
        else:
            return {
                "first_arg": self.innerObject,
                self.name: righthand_operand
            }


