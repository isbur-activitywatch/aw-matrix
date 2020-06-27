#     for bucket in buckets /on/ local_server:
#         Fetch | last-events /originating_at/ bucket
#         Post | them(events) /to/ Synapse-server


# Common imports
from .Container import Container    # just to call dibs on name to no to bind name in introspective manner using inspect module
from .Phrases import define_meaning_of_phrase_


@define_meaning_of_phrase_(
    "for bucket in buckets /on/ local_server:"
)
def Definition():

    buckets = Container()    

    from .Infix import Infix
    @Infix
    def on (lefthand_operand, righthand_operand):
        lefthand_operand.contents = righthand_operand.get("/api/0/buckets/").json()
        return righthand_operand.get("/api/0/buckets/").json()

    from .local_AW_server import local_AW_server

    objs = {
        "buckets": buckets, 
        "on": on, 
        "local_server": local_AW_server
    }
    





####
#### Second Phrase
#### *    Fetch | last-events /originating_at/ bucket*
####


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

    # from matrix_client import *
    # synapse_server.post(events)






# last-events должно быть то же, что и просто events 
# (например, пустой объект last и перегрузка оператора __rsub__ так, чтобы он ничего не делал)

# last-events /originating_at/ bucket
# /originating_at/ - извлекает события из ведра и кладёт их в events

def them(events):
    return events

# Fetch |, Post | - обёртки над функциями fetch, post, которые и делают всю грязную работу
# (остально всё суть перекладывание и перепаковывание аргументов)