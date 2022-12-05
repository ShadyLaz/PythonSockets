
import rpyc
import socket
import json
import ast


# host = socket.gethostbyname(socket.gethostname())
# OR
HOST = "10.180.55.54"
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(5)


# def imAnInt(message):
#     # Parsing and operation
#
#     message_new = message.split(" ")
#     if message_new[0] == 'sum':
#         output = int(message_new[1]) + int(message_new[2])
#     elif message_new[0] == 'dif':
#         output = int(message_new[1]) - int(message_new[2])
#     else:
#         output = 'error'
#     AaString = str(output)
#
#     return AaString


try:
    while True:
        # comment here

        communication_socket, adress = server.accept()
        print(f"Connected to {adress}")

        #message = communication_socket.recv(1024).decode("utf-8")

        with open(r"C:\Users\clazkani\OneDrive - Capgemini\Documents\EmployeeJsonData.json", 'r') as outfile:
            #outfile.write(json_string)
            lines = outfile.readlines()
            output_line = ''
            for line in lines:
                print(line)
                output_line = output_line + line
            print(type(line))
            dict_obj = ast.literal_eval(output_line)
            data = json.dumps(dict_obj)
            print(dict_obj)
            print(type(data))
            communication_socket.send(f"{data}".encode("utf-8"))

       #output = imAnInt(message)


     #communication_socket.send(f"Got your message! Answer is = {output}".encode("utf-8"))

        communication_socket.close()


except KeyboardInterrupt:
    print("Interrupted")


