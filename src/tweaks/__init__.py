#     for every-bucket in buckets /on/ local_server:
#         Fetch | last-events /originating_at/ bucket
#         Post | them(events) /to/ Synapse-server




####
#### First Phrase
#### *for every-bucket in buckets /on/ local_server:*
####


from .local_server import local_server  # requests.Session bound to address of local AW server

from .Infix import Infix
@Infix
def on (lefthand_operand, righthand_operand):
    lefthand_operand.contents = righthand_operand.get("/api/0/buckets/").json()
    return righthand_operand.get("/api/0/buckets/").json()

class Container:
    pass
buckets = Container()    # just to call dibs on name to no to bind name in introspective manner using inspect module

# bucket is just... bucket? See AW-specification
#       - server returns list of bucket-id on /api/0/buckets




####
#### Second Phrase
#### *    Fetch | last-events /originating_at/ bucket*
####


from .Phrases import Function_With_Prepositions
@Function_With_Prepositions("Fetch | last-events /originating_at/ bucket")
def Fetch(events=[], originating_at=""):
    local_server.post(
        "/api/0/query",
        params = {
            
        }
    )

    pass




# last-events должно быть то же, что и просто events 
# (например, пустой объект last и перегрузка оператора __rsub__ так, чтобы он ничего не делал)

# last-events /originating_at/ bucket
# /originating_at/ - извлекает события из ведра и кладёт их в events

def them(events):
    return events

# Fetch |, Post | - обёртки над функциями fetch, post, которые и делают всю грязную работу
# (остально всё суть перекладывание и перепаковывание аргументов)