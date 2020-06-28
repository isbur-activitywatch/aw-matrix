from .local_server import local_server


class Last:
    def __sub__(self, righthand_operand):
        return righthand_operand
last = Last()


bucket = "foo"


n_previous = local_server.get_event_count_from_



from .phrase2 import *
from .Phrases import Function_With_Prepositions
@Function_With_Prepositions("Fetch | last-events /originating_at/ bucket")
def Fetch(events=[], originating_at=""):
    bucket = originating_at
    n_present = local_server.get_event_count_from_(bucket)
    events = local_server.get(
        "/api/0/buckets/"   +
                    bucket  +
                    "/events",
        params = {
            "limit": n_present - n_previous
        }
    )
    n_previous = n_present



# # last-events должно быть то же, что и просто events 
# # (например, пустой объект last и перегрузка оператора __rsub__ так, чтобы он ничего не делал)

# # last-events /originating_at/ bucket
# # /originating_at/ - извлекает события из ведра и кладёт их в events



# Some kind of test?

# proto = "Fetch | last-events /originating_at/ bucket"
# def foo(obj = "bzz", originating_at = "baz"):
#     print(obj)
#     print(originating_at)
# Fetch = Function_With_Prepositions(foo, proto)
# last_events = "foo"
# bucket = "bar"
# Fetch | last_events /originating_at/ bucket