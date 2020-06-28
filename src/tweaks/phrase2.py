from tweaks.phrase_machine import define_meaning_of_phrase_


@define_meaning_of_phrase_(
    "    Fetch | last-events /originating_at/ bucket",
    name = "Phrase2",
    names_to_bind = ["Fetch", "last", "events", "originating_at"]
)

class Definition():

    from .Prefix import Prefix
    @Prefix
    def Fetch(events, source):
        pass 
    
    from .Useless import useless_instance as last

    from .Container import Container
    events = Container()

    from .Infix import Infix
    @Infix
    def originating_at(lefthand_operand, righthand_operand):
        return (lefthand_operand, righthand_operand)




n_previous = local_server.get_event_count_from_


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