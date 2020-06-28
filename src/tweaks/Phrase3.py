# pylint: disable=no-self-argument,attribute-defined-outside-init

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
        return synapse_server.post(events.contents)

    def them(events):
        return events

    from tweaks.Infix import Infix
    @Infix
    def to (lefthand_operand, righthand_operand):
        return (lefthand_operand, righthand_operand)

    from .synapse_server import Synapse
    Synapse = Synapse()

    from .Useless import useless_instance as server





        
