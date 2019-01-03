import socket

class PhonyClient:

    def __init__(self, server_ip="localhost", server_port=12000):
        print("Starting client")
        self.server_ip = server_ip
        self.server_port = server_port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def run(self):
        running = True

        while running:
            # Get the message
            message = bytes(input("UDP Message: "), encoding="utf-8")

            print("Sending {0} byte-length message.".format(len(message)))

            # Send it
            server_address = (self.server_ip, self.server_port)
            self.client_socket.sendto(message, server_address)

            # Termination Condition
            running = False if message.upper() == 'STOP' else True

if __name__ == '__main__':
    pc = PhonyClient()
    pc.run()
