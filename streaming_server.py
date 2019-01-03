from queue import Queue
import multiprocessing
import socket

class BmaWifiLogServer:
    
    def __init__(self, port=12000, ip=''):
        self.port = port
        self.ip = ip
        self.fifos = {}


    def start_listening(self):

        p = multiprocessing.Process(
            target=BmaWifiLogServer.listen,
            args=(self.fifos,),
            kwargs={"ip": self.ip, "port":self.port}
        )
        p.start()


    @staticmethod
    def listen(request_reader_queue_dict: dict, port=12000, ip=''):
        print("Starting to listen on port 12000")
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_socket.bind((ip,port))
        running = True

        while(running):
            message, address = server_socket.recvfrom(45) #bytes
            list_message = message.decode("utf-8").split(",")
            list_message = list(map(lambda x: x.strip(), list_message))

            if(address[0] not in request_reader_queue_dict):
                request_reader_queue_dict[address[0]] = multiprocessing.Queue()

            request_reader_queue_dict[address[0]].put(list_message)

            print(list_message)
            print(request_reader_queue_dict)

            running = False if  message.decode("utf-8").upper() == 'STOP' else True

        print("Stopped listening on port 12000")


class BmaWifiPacketBuilder:
    def __init__(self, ip, queue: multiprocessing.Queue):
        self.ip = ip
        self.queue = queue
        self.learner = BmaWifiLearner(self.ip, self.queue)
        self.current_packet = {}

    def handle_partial_packet(self,partial_packet):
        if len(partial_packet < 45):
            new_packet_length = len(partial_packet) + len(self.current_packet) 

class BmaWifiLearner:
    def __init__(self, ip):
        print("Side effects~!")


if __name__ == '__main__':
    ls = BmaWifiLogServer()
    ls.start_listening()
