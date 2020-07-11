# pylint: disable=import-outside-toplevel,wrong-import-position
print("Inside tweaks.__init__")


from .phrase_machine import define_meaning_of_phrase_


@define_meaning_of_phrase_(
    "There will be NO PHRASE",
    name="just_two_objs",
    names_to_bind=["local_AW_server", "Synapse_server"]
)
class Definition:
    # Let's play our li'l game here
    from .AW_proxy_client import AW_proxy_client as local_AW_server
    import tweaks.Synapse_proxy_client as Synapse_server 
