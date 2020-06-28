class Prefix:

    def __init__(self, function):
        self.function = function
    
    def __or__(self, righthand_operand):
        return self.function(*righthand_operand)