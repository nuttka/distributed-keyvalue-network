from concurrent import futures

import grpc

import key_value_pb2, key_value_pb2_grpc

class KeyValueService(key_value_pb2_grpc.StorageServicer):

    def __init__(self, *args, **kwargs):
        self.key_value_list = []

    def insert(self, request, context):
        key, value = request

        find = next((i for i, kv in enumerate(self.key_value_list) if kv[0] == key), None)

        reply = 0 if find == None else -1

        if reply == 0:
            self.key_value_list.append((key, value))

        return key_value_pb2.InsertReply(reply=reply)

    
    def get(self, request, context):
        key = request.key

        find = next((i for i, kv in enumerate(self.key_value_list) if kv[0] == key), None)

        value = "" if find == None else self.key_value_list[find]

        return key_value_pb2.Value(value=value)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    key_value_pb2_grpc.add_StorageServicer_to_server(KeyValueService(), server)
    server.add_insecure_port('localhost:8888')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()