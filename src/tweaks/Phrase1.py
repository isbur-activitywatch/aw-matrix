from tweaks.Container import Container
from tweaks.phrase_machine import define_meaning_of_phrase_


@define_meaning_of_phrase_(
    "for bucket in buckets /on/ local_server:",
    name = "Phrase1",
    names_to_bind = ["buckets", "on", "local_server"]
)
class Definition():

    buckets = Container()    

    from tweaks.Infix import Infix
    @Infix
    def on (lefthand_operand, righthand_operand):
        lefthand_operand.contents = righthand_operand.get("/api/0/buckets/").json()
        return righthand_operand.get("/api/0/buckets/").json()

    from tweaks.local_AW_server import local_AW_server as local_server
