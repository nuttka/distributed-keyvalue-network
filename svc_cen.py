from concurrent import futures
import sys
import threading
import socket

import grpc

import central_management_pb2, central_management_pb2_grpc

class CentralManagementService(central_management_pb2_grpc.CentralManagementServicer):

    def __init__(self, stop_event, host):
        self.host = host
        self.stop_event = stop_event
        self.central_list = []


    def register(self, request, context):
        server_id = request.server_id
        arr = request.arr
        self.central_list.append((server_id, arr))
        return central_management_pb2.RegisterReply(number_of_keys = len(arr))

    
    def find(self, request, context):
        key = request.key
        find = next((i for i, kv in enumerate(self.central_list) if key in kv[1]), None)
        value = "" if find == None else self.central_list[find][0]
        return central_management_pb2.Server(server = value)

    
    def finish(self, request, context):
        number_of_keys = 0

        for item in self.central_list:
            number_of_keys += len(item[1])

        self.stop_event.set()
        return central_management_pb2.FinishReply(number_of_keys = number_of_keys)

def serve(port):
    host = socket.getfqdn() + ':' + port
    stop_event = threading.Event()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    central_management_pb2_grpc.add_CentralManagementServicer_to_server(CentralManagementService(stop_event = stop_event, host = host), server)
    server.add_insecure_port(host)
    server.start()
    
    stop_event.wait()
    server.stop(50)

if __name__ == '__main__':
    port = sys.argv[1]
    serve(port)