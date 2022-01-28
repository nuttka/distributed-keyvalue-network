from concurrent import futures
import threading
import socket
import sys

import grpc

import key_value_pb2, key_value_pb2_grpc, central_management_pb2, central_management_pb2_grpc



class CentralClient():

    def __init__(self, host):
        self.host = host
        self.channel = grpc.insecure_channel(self.host)
        self.stub = central_management_pb2_grpc.CentralManagementStub(self.channel)

    def sendKeys(self, server, arr):
        message = central_management_pb2.ServerKeys(server_id = server, arr = arr)
        response = self.stub.register(message)
        print(str(response.number_of_keys))
        return response.number_of_keys
        


class KeyValueService(key_value_pb2_grpc.StorageServicer):

    def __init__(self, stop_event, host):
        self.host = host
        self.key_value_list = []
        self.stop_event = stop_event

    def insert(self, request, context):
        key = request.key
        value = request.value

        find = next((i for i, kv in enumerate(self.key_value_list) if kv[0] == key), None)
        
        reply = 0 if find == None else -1

        if reply == 0:
            self.key_value_list.append((key, value))

        return key_value_pb2.InsertReply(reply = reply)

    
    def get(self, request, context):
        key = request.key
        find = next((i for i, kv in enumerate(self.key_value_list) if kv[0] == key), None)
        value = "" if find == None else self.key_value_list[find][1]

        return key_value_pb2.Value(value = value)


    def activate(self, request, context):
        host = request.host
        central_client = CentralClient(host)
        keys_arr = []

        for key_value in self.key_value_list:
            keys_arr.append(key_value[0])

        number_of_keys = central_client.sendKeys(self.host, keys_arr)
        return key_value_pb2.NumberKeys(number_of_keys = number_of_keys)

    
    def finish(self, request, context):
        self.stop_event.set()
        return key_value_pb2.Finish(reply = 0)



def serve(port):
    host = socket.getfqdn() + ':' + port
    stop_event = threading.Event()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    key_value_pb2_grpc.add_StorageServicer_to_server(KeyValueService(stop_event = stop_event, host = host), server)
    server.add_insecure_port(host)
    server.start()
    
    stop_event.wait()
    server.stop(50)

if __name__ == '__main__':
    port = sys.argv[1]
    serve(port)