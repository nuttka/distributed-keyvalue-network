from concurrent import futures
import threading

import grpc

import key_value_pb2, key_value_pb2_grpc

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