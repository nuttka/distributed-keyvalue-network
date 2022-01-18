from concurrent import futures

import grpc

import key_value_pb2, key_value_pb2_grpc

class KeyValueService(key_value_pb2_grpc.StorageServicer):

    key_value_list = []

    def insert(self, request, context):
        key, value = request

        find = next((i for i, kv in enumerate(key_value_list) if kv[0] == key), None)

        return key_value_pb2.InsertReply(reply=reply)

    
    def get(self, request, context):
        print("Grpc server say_hello_again, pid = ", str(request.pid))
        return hello_pb2.HelloReply(retval='Hello again, %s' % str(request.pid))

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    key_value_pb2_grpc.add_StorageServicer_to_server(KeyValueService(), server)
    server.add_insecure_port('localhost:8888')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()