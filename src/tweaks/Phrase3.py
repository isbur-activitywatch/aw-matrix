# def them(events):
#     return events


from tweaks.Container import Container    
from tweaks.Phrases import define_meaning_of_phrase_


@define_meaning_of_phrase_(
    "for bucket in buckets /on/ local_server:",
    name = "Phrase3"
)
def Definition():

    buckets = Container()    

    from tweaks.Infix import Infix
    @Infix
    def on (lefthand_operand, righthand_operand):
        lefthand_operand.contents = righthand_operand.get("/api/0/buckets/").json()
        return righthand_operand.get("/api/0/buckets/").json()

    from tweaks.local_AW_server import local_AW_server

    objs = {
        "buckets": buckets,
        "on": on,
        "local_server": local_AW_server
    }

    # import inspect
    # import sys
    # module_name = inspect.currentframe().f_back.f_globals["__name__"] # I'm afraid it's too fragile
    # module = sys.modules[module_name]
    import sys
    module = sys.modules['main']
    for key, value in objs.items():
        setattr(module, key, value)


        
    # from matrix_client import *
#     # synapse_server.post(events)