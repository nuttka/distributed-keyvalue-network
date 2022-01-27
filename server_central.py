from concurrent import futures
import threading

import grpc

import central_management_pb2, central_management_pb2_grpc

class CentralManagementService(central_management_pb2_grpc.CentralManagementServicer):

    def __init__(self, stop_event):
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
        self.stop_event.set()
        return central_management_pb2.FinishReply(reply = 0)

def serve():
    stop_event = threading.Event()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    central_management_pb2_grpc.add_StorageServicer_to_server(CentralManagementService(stop_event = stop_event), server)
    server.add_insecure_port('localhost:8080')
    server.start()
    
    stop_event.wait()
    server.stop(50)

if __name__ == '__main__':
    serve()