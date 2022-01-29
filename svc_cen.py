from concurrent import futures
import sys
import threading
import socket

import grpc

import central_management_pb2, central_management_pb2_grpc

class CentralManagementService(central_management_pb2_grpc.CentralManagementServicer): # classe que dita serviços que o cliente pode convocar

    def __init__(self, stop_event, host):
        self.host = host
        self.stop_event = stop_event # thread responável pelo termino do servidor
        self.central_list = dict() # dicionário para relação chave valor


    def register(self, request, context):
        server_id = request.server_id
        arr = request.arr

        for item in arr: # para o array de chaves que o servidor de par envia, guardamos a relação chave,servidor
            self.central_list[item] = server_id


        return central_management_pb2.RegisterReply(number_of_keys = len(arr)) # retorna para o servidor o numero de chaves enviado no tipo definido no arquivo .proto

    
    def find(self, request, context):
        key = request.key

        value = self.central_list[key] if key in self.central_list else "" # caso a chave exista, envia o servidor que a possui, caso contrario envia a string vazia

        return central_management_pb2.Server(server = value) # retorna para o servidor a string no tipo definido no arquivo .proto

    
    def finish(self, request, context):
        self.stop_event.set() # disparo da thread
        return central_management_pb2.FinishReply(number_of_keys = len(self.central_list)) # retorno do número de keys no servidor no tipo corretamente definido no .proto

def serve(port):
    host = socket.getfqdn() + ':' + port # nome do dominio + porta

    stop_event = threading.Event() # evento criado para a finalização do servidor, o qual a thread fica em wait até ser disparada 
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    central_management_pb2_grpc.add_CentralManagementServicer_to_server(CentralManagementService(stop_event = stop_event, host = host), server)
    server.add_insecure_port(host)
    server.start()
    
    stop_event.wait() # thread em espera para finalização do servidor
    server.stop(50) # finalização do servidor

if __name__ == '__main__':
    port = sys.argv[1] # recebe a porta como arg
    serve(port)