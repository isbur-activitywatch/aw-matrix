from functools import partial


class Infix:
    """
    >>> @Infix
    ... def foo(a, b):
    ...     return a + b
    ...
    >>> '1' /foo/ '2'
    '12'
    """

    def __init__(self, func):
        self.func = func
    
    def __rtruediv__(self, lefthand_operand):
        return Infix(partial(self.func, lefthand_operand))
    
    def __truediv__(self, righthand_operand):
        return self.func(righthand_operand)