from tweaks.Container import Container    
from tweaks.phrase_machine import define_meaning_of_phrase_


@define_meaning_of_phrase_(
    "    Post | them(events) /to/ Synapse-server",
    name = "Phrase3",
    names_to_bind = ["Post", "them", "to", "Synapse", "server"]
)

class Definition():

    from .Prefix import Prefix
    @Prefix
    def Post(events, synapse_server):
        # synapse_server.post(events)
        pass

    def them(events):
        return events

    from tweaks.Infix import Infix
    @Infix
    def to (lefthand_operand, righthand_operand):
        # lefthand_operand.contents = righthand_operand.get("/api/0/buckets/").json()
        # return righthand_operand.get("/api/0/buckets/").json()
        # return (lefthand_operand, righthand_operand.some_magic())
        pass

    class Synapse:
        pass

    from .Useless import useless_instance as server





        
