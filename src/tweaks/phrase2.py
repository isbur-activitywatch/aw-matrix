# pylint: disable=no-self-argument,attribute-defined-outside-init

from tweaks.phrase_machine import define_meaning_of_phrase_
from .AW_client import AW_client as local_server


@define_meaning_of_phrase_(
    "    Fetch | last-events /originating_at/ bucket",
    name = "Phrase2",
    names_to_bind = ["Fetch", "last", "events", "originating_at"]
)

class Definition():

    from .Prefix import Prefix
    @Prefix
    def Fetch(events, bucket_id):
        n_present = local_server.get_event_count_from_(bucket_id)
        events.contents = local_server.get(
            "/api/0/buckets/"   +
                        bucket_id  +
                        "/events",
            # params = {
            #     "limit": n_present - local_server.buckets[bucket_id]["n_previous"]
            # }
            params = {
                "limit": n_present - local_server.buckets[bucket_id]["n_previous"] + 1
            }
        )
        local_server.buckets[bucket_id]["n_previous"] = n_present 
    
    from .Useless import useless_instance as last

    from .Container import Container
    events = Container()

    from .Infix import Infix
    @Infix
    def originating_at(lefthand_operand, righthand_operand):
        return (lefthand_operand, righthand_operand)



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
