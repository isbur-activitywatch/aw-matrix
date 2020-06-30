# pylint: disable=no-self-argument,attribute-defined-outside-init

from tweaks.Container import Container
from tweaks.phrase_machine import define_meaning_of_phrase_


@define_meaning_of_phrase_(
    "for bucket in buckets /on/ local_AW_server:",
    name = "Phrase1",
    names_to_bind = ["buckets", "on", "local_AW_server"]
)

class Definition():

    buckets = Container()    

    from tweaks.Infix import Infix
    @Infix
    def on (lefthand_operand, righthand_operand):
        lefthand_operand.contents = righthand_operand.get_buckets()
        return righthand_operand.get_buckets()

    from .AW_client import AW_client as local_AW_server
