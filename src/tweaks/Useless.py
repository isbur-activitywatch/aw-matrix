class Useless:
    def __sub__(self, righthand_operand):
        return righthand_operand
    def __rsub__(self, lefthand_operand):
        return lefthand_operand

useless_instance = Useless()
