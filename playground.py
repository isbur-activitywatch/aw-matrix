# import zmq

# context = zmq.Context()
# socket = context.socket(zmq.REQ)
# socket.connect("tcp://localhost:5555")

# def post(message):
#     socket.send_string(str(message))

#     answer = socket.recv_string()

#     print("Received:\t", answer)

# post("hello")
