from matrix_client.client import MatrixClient


class Synapse:

    def __init__(self):
        client =  MatrixClient(
            "https://matrix.org"
        )
        token = client.login(
            "isbur",
            "QLz4EgVc4EyQY5L"
        )
        self.client =  MatrixClient(
            "https://matrix.org",
            token = token,
            user_id = "@isbur:matrix.org"
        )
        self.room = client.join_room("!BeLEKkRmKBJzNOdqxB:matrix.org")
    
    def post(self, msg):
        self.room.send_text(str(msg))
