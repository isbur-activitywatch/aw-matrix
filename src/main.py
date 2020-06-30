# pylint: disable=undefined-variable
import tweaks   # pylint: disable=unused-import

import time


def tick():
    for bucket in buckets /on/ local_AW_server:
        Fetch | last-events /originating_at/ bucket
        Post | them(events) /to/ Synapse-server


def run_routine():
    while True:
        tick()
        time.sleep(1)
