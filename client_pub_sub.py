from sys import exit, argv
import zmq

port = "5563"
serv = "localhost"

if len(argv) == 3:
    serv = argv[1]
    port = argv[2]
elif len(argv) == 1:
    print(f'Valore padrao server [{serv}] porta [{port}]\n')
else:
    print(f'Uso: {argv[0]} <SERVER_ADDRESS> <SERVER_PORT>\n')
    exit(0);

# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)

connectTo = f"tcp://{serv}:{port}"

print(f"Coletando mensagens do server: [{connectTo}]")
socket.connect(connectTo)

while True:
    print("Waiting...")
    topicfilter = b"10001"
    socket.setsockopt(zmq.SUBSCRIBE, topicfilter)

    msg = socket.recv()

    print(f"Recebido: [{msg[6:]}]\n")

print("Pausa.")
input()