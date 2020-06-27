from .local_server import local_server


class Last:
    def __sub__(self, righthand_operand):
        return righthand_operand
last = Last()


bucket = "foo"


n_previous = local_server.get_event_count_from_
