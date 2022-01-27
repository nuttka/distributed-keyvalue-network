from concurrent import futures
import threading

import grpc

import key_value_pb2, key_value_pb2_grpc, central_management_pb2, central_management_pb2_grpc



class CentralClient():

    def __init__(self, id):
        # self.host = id
        self.host = 'localhost:8080'
        self.channel = grpc.insecure_channel(self.host)
        self.stub = central_management_pb2_grpc.CentralManagementStub(self.channel)

    def findServer(self, server, arr):
        message = central_management_pb2.ServerKeys(server_id = server, arr = arr)
        response = self.stub.register(message)
        print(str(response.number_of_keys))
        return response.number_of_keys
        


class KeyValueService(key_value_pb2_grpc.StorageServicer):

    def __init__(self, stop_event):
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
        id = request.id
        central_client = CentralClient(id)
        keys_arr = []

        for key_value in self.key_value_list:
            keys_arr.append(key_value[0])

        central_client.findServer(self.host, keys_arr)
        return key_value_pb2.NumberKeys(number_of_keys = 0)

    
    def finish(self, request, context):
        self.stop_event.set()
        return key_value_pb2.Finish(reply = 0)



def serve():
    stop_event = threading.Event()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    key_value_pb2_grpc.add_StorageServicer_to_server(KeyValueService(stop_event = stop_event), server)
    server.add_insecure_port('localhost:50051')
    server.start()
    
    stop_event.wait()
    server.stop(50)

if __name__ == '__main__':
    serve()