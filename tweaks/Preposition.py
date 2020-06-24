'''
>>> a = Preposition("a")
>>> 1 /a/ 2 /a/ 3
{'object': 1, 'a': 3}

>>> a = Preposition("a")
>>> b = Preposition("b")
>>> 1 /a/ 2 /b/ 3
{'object': 1, 'a': 2, 'b': 3}
'''
class Preposition:

    def __init__(self, name):
        self.name = name
    
    def __rdiv__(self, lefthand_operand):
        self.innerObject = lefthand_operand
        return self

    def __div__(self, righthand_operand):
        if type(self.innerObject) == type({}):
            self.innerObject[self.name] = righthand_operand
            return self.innerObject
        else:
            return {
                "object": self.innerObject,
                self.name: righthand_operand
            }


