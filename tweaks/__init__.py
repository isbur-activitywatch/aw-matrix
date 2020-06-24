# bucket is just... bucket?
# bucket-metadata
# events (in lazy manner)

# every-bucket must return a property of bucket to which for loop will write values from iterable

# (buckets /on/ local_server) must be iterable

from .main import Fetch, Post
from .local_server import local_server


# last-events должно быть то же, что и просто events 
# (например, пустой объект last и перегрузка оператора __rsub__ так, чтобы он ничего не делал)

# last-events /originating_at/ bucket
# /originating_at/ - извлекает события из ведра и кладёт их в events

# them(events) возвращает events

# Fetch |, Post | - обёртки над функциями fetch, post, которые и делают всю грязную работу
# (остально всё суть перекладывание и перепаковывание аргументов)