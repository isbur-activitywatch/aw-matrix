import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.setsockopt(zmq.RCVTIMEO, 30000)
socket.connect("tcp://localhost:5555")

def post(message):
    socket.send_string(str(message))

    socket.recv_string()
